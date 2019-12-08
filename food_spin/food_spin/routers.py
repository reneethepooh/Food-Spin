NUM_LOGICAL_SHARDS = 16
NUM_PHYSICAL_SHARDS = 2

LOGICAL_TO_PHYSICAL = (
    'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 
    'db1', 'db2', 'db1', 'db2', 'db1', 'db2', 'db1', 'db2',
)

def set_user_for_sharding(query_set, user_id):
    if query_set._hints == None:
        query_set._hints = {'owner': user_id}
    else:
        query_set._hints['owner'] = user_id

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
            db = self._database_of(instance.owner)
        except AttributeError: 
            db = self._database_of(instance.id)
        except KeyError:
            try:
                db = self._database_of(int(hints['owner']))
            except KeyError:
                print('No instance in hints')
        return db

    def db_for_read(self, model, **hints):
        return self._db_for_read_write(model, **hints)
    
    def db_for_write(self, model, **hints):
        return self._db_for_read_write(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == ‘auth’ and obj2._meta.app_label != ‘auth’) or (obj1._meta.app_label != ‘auth’ and obj2._meta.app_label == ‘auth’):
            print(“Rejecting cross-table relationship”, obj1._meta.app_label, obj2._meta.app_label)
            return False
        return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        return True
