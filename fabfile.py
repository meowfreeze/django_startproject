import os

from fabric.api import *

env.hosts = ['']

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

# USAGE:
# fab deploy:[branch]
        
def deploy(branch):
    
    # tests?
    
    if branch == 'production':
        
        # push master to repo
        local('git push origin master')
        
        # pull master to production repo
        with cd(PRODUCTION_ROOT):
            run('git pull origin master')
            
        with cd(PRODUCTION_DJANGO_ROOT), \
            prefix('workon %s' % PRODUCTION_ENV):
            
            # collectstatic
            run('python manage.py collectstatic --settings=%s' \
                % PRODUCTION_SETTINGS)
            
            # run migrations
            run('python manage.py migrate --settings=%s' % PRODUCTION_SETTINGS)
        
        # restart application
        with cd(PRODUCTION_SRV):
            run('touch %s' % PRODUCTION_FCGI)
    
    elif branch == 'staging':
        
        # push staging branch to repo
        local('git push origin staging')
        
        # pull staging branch to staging repo
        with cd(STAGING_ROOT):
            run('git pull origin staging')
        
        with cd(STAGING_DJANGO_ROOT), \
            prefix('workon %s' % STAGING_ENV):
            
            # collectstatic
            run('python manage.py collectstatic --settings=%s' \
                % STAGING_SETTINGS)
            
            # run migrations
            run('python manage.py migrate --settings=%s' % STAGING_SETTINGS)
        
        # restart application
        with cd(STAGING_SRV):
            run('touch %s' % STAGING_FCGI)
    
    else:
        print 'enter a valid branch'