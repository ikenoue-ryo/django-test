=======================
django-torina-tutorial1
=======================

ここは説明です


Requirement
===========

:Python: 3.6
:Django: 1.11
 

Quick start
===========
1. "myapp" を、INSTALLED_APPS に足す。::

    INSTALLED_APPS = [
        ...
        'myapp',
    ]

2. urls.pyに以下のようにしてincludeしてください。::

    url(r'^', include('myapp.urls')),

3. `python manage.py migrate`

4. `python manage.py runserver`

5. http://127.0.0.1:8000 へアクセス!