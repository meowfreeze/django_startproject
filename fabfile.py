import os

from fabric.api import *

env.hosts = ['laislama@laislamarts.org']

# CONFIG

# project server structure
#
# srv
# └── {{ project_name }}
#     ├── production
#     │   ├── {{ project_name }}
#     │   ├── fabfile.py
#     │   ├── README.md
#     │   └── requirements
#     └── staging
#         ├── {{ project_name }}
#         ├── fabfile.py
#         ├── README.md
#         └── requirements

# location of manage.py file
STAGING_DJANGO_ROOT = '~/srv/{{ project_name }}/staging/{{ project_name }}'
STAGING_ENV = 'staging'
STAGING_FCGI = 'staging.fcgi'
STAGING_ROOT = '~/srv/{{ project_name }}/staging'
STAGING_SETTINGS = '{{ project_name }}.settings.staging'
STAGING_SRV = '~/public_html/staging'

# location of manage.py file
PRODUCTION_ENV = 'production'
PRODUCTION_DJANGO_ROOT = '~/srv/{{ project_name }}/production/{{ project_name }}'
PRODUCTION_FCGI = 'production.fcgi'
PRODUCTION_ROOT = '~/srv/{{ project_name }}/production'
PRODUCTION_SETTINGS = '{{ project_name }}.settings.production'
PRODUCTION_SRV = '~/public_html/production'


# DEPLOYMENT
        
def deploy(repo):
    
    # tests?
    
    if repo == 'production':
        
        # push master to repo
        local('git push origin master')
        
        # pull master to production repo
        with cd(PRODUCTION_ROOT):
            run('git pull origin master')
            
        # collectstatic
        with cd(PRODUCTION_DJANGO_ROOT), \
            prefix('workon %s' % PRODUCTION_ENV):
            
            run('python manage.py collectstatic --settings=%s' \
                % PRODUCTION_SETTINGS)
        
        # restart application
        with cd(PRODUCTION_SRV):
            run('touch %s' % PRODUCTION_FCGI)
    
    elif repo == 'staging':
        
        # push staging branch to repo
        local('git push origin staging')
        
        # pull staging branch to staging repo
        with cd(STAGING_ROOT):
            run('git pull origin staging')
        
        # collectstatic
        with cd(STAGING_DJANGO_ROOT), \
            prefix('workon %s' % STAGING_ENV):
            
            run('python manage.py collectstatic --settings=%s' \
                % STAGING_SETTINGS)
        
        # restart application
        with cd(STAGING_SRV):
            run('touch %s' % STAGING_FCGI)
    
    else:
        print 'enter a valid repo'