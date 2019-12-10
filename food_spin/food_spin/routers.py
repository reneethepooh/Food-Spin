NUM_LOGICAL_SHARDS = 16
NUM_PHYSICAL_SHARDS = 2

LOGICAL_TO_PHYSICAL = (
    'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 
    'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
)

def bucket_users_into_shards(user_ids):
    d = {}
    for id in user_ids:
        shard = logical_shard_for_user(id)
        if not shard in d:
            d[shard] = []
        d[shard].append(id)
    return d

def set_user_for_sharding(query_set, user_id):
    if query_set._hints == None:
        query_set._hints = {'user_id': user_id}
    else:
        query_set._hints['user_id'] = user_id

def logical_to_physical(logical):
    if logical >= NUM_LOGICAL_SHARDS or logical <0:
        raise Exception('Shard out of bounds: %d' %logical)
    return LOGICAL_TO_PHYSICAL[logical]

def logical_shard_for_user(user_id):
    return user_id % NUM_LOGICAL_SHARDS

class UserRouter(object):
    def _database_of(self, user_id):
        return logical_to_physical(logical_shard_for_user(user_id))

    def _db_for_read_write(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        
        if model._meta.app_label == 'sessions':
            return 'auth_db'
        
        db = None

        try:
            instance = hints['instance']
            db = self._database_of(instance.user_id)
        except AttributeError: 
            db = self._database_of(instance.id)
        except KeyError:
            try:
                db = self._database_of(int(hints['user_id']))
            except KeyError:
                print('No instance in hints')
        return db

    def db_for_read(self, model, **hints):
        return self._db_for_read_write(model, **hints)
    
    def db_for_write(self, model, **hints):
        return self._db_for_read_write(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == 'auth' and obj2._meta.app_label == 'contenttypes') or (obj1._meta.app_label == 'contenttypes' and obj2._meta.app_label == 'auth'):
            return True
        if (obj1._meta.app_label == 'auth' and obj2._meta.app_label != 'auth') or (obj1._meta.app_label != 'auth' and obj2._meta.app_label == 'auth'):
            print("Rejecting cross-table relationship", obj1._meta.app_label, obj2._meta.app_label, obj1._meta.db_table, obj2._meta.db_table, obj1._meta.label_lower, obj2._meta.label_lower)
            return False
        return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        return True
