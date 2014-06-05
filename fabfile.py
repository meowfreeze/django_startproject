import os

from fabric.api import *

env.hosts = ['']

# CONFIG

STAGING_DIR = ''
STAGING_WWW = ''

PRODUCTION_DIR = ''
PRODUCTION_WWW = ''

# DEPLOYMENT
        
def deploy(repo):
    # tests?
    
    if repo == 'production':
        # git
        local('git push origin master')
        with cd(PRODUCTION_DIR):
            run('git pull origin master')
            
        # collectstatic
        with cd(os.path.join(PRODUCTION_DIR, 'still_room')):
            run('workon [env name] && python manage.py collectstatic --settings=still_room.settings.production')
        
        # restart server
    
    elif repo == 'staging':
        # git
        local('git push origin staging')
        with cd(STAGING_DIR):
            run('git pull origin staging')
        
        # collectstatic
        with cd(os.path.join(STAGING_DIR, 'still_room')):
            run('workon [env name] && python manage.py collectstatic --settings=still_room.settings.staging')
        
        # restart server
    
    else:
        print 'enter a valid repo'