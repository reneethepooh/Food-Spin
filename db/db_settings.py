DATABASES = {
  'default': { },
  'auth_db': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'foodspin',
    'USER': 'fsadmin',
    'PASSWORD': 'CxkCiNMN*3Su',
    'HOST': '34.208.1.163',
    'PORT': '3306',
  },
  'db1': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'foodspin',
    'USER': 'fsadmin',
    'PASSWORD': 'CxkCiNMN*3Su',
    'HOST': '18.236.134.177',
    'PORT': '3306',
  },
  'db2': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'foodspin',
    'USER': 'fsadmin',
    'PASSWORD': 'CxkCiNMN*3Su',
    'HOST': '54.245.5.200',
    'PORT': '3306',
  },
}
# Database routers go here:
DATABASE_ROUTERS = ['food_spin.routers.UserRouter']

