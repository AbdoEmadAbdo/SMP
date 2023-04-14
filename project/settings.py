import os
#from environ import Env 
#env = Env()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#pip install pymongo[srv] 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%%8@%epwc!vass7)aa@ju*kng361hlxmjovuy68h(xm-16(buz' #! Not sharable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    # !!  if fulse   must type   ['Our-domain.com']  inside   ALLOWED_HOSTS

ALLOWED_HOSTS = []


FMP_API_KEY = 'api_key'
AUTH_USER_MODEL = 'pages.CustomUser'


# Application definition

INSTALLED_APPS = [
    
    
    'pages.apps.PagesConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #'crispy_forms',
    
    'django.contrib.auth',  # Core authentication framework and its default models.
    'django.contrib.contenttypes',  # Django content type system (allows permissions to be associated with models).
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',   # Manages sessions across requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Associates users with requests using sessions.
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'django.template.backends.jinja2.Jinja2',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME':'FTKP_DB',
        'HOST': 'localhost',
        'PORT': 27017,
              }
        'CLIENT': {
            'host': 'mongodb://localhost:27017/' #localhost:27017
                  },
}
'''

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


    #? Static files (CSS, JavaScript, Images) :-
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR , 'static')

STATICFILES_DIRS = [  os.path.join(BASE_DIR , 'Project/static')  ]



#MEDIA Activates

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR , 'media')




# Default primary key field type      IDs.
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




LOGIN_REDIRECT_URL = '/'   #To Redirect to home URL after login (Default redirects to /accounts/profile/)





