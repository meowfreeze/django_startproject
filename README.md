# KEEP IT SIMPLE STUPID

## project install

    mkvirtualenv [ project name ]

or, for python 3:
    
    mkvirtualenv --python=`which python3` [ project name ]

next:

    pip install Django==1.7
    django-admin.py startproject --template=https://github.com/meowfreeze/django_startproject/archive/1.7.x.zip project_name --extension=py,json
    pip install -r requirements/local.txt
