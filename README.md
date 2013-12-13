### setup local environment
- mkvirtualenv [env name]
- pip install django
- django-admin.py startproject --template=https://github.com/meowfreeze/django_startproject/archive/master.zip [project name]
- pip install -r requirements/local.txt
- createdb --username=[username] --owner=[username] [db]
- add db info to local settings file
- django-admin.py syncdb --settings=[project.settings.local]

### setup staging environment

### setup production environment