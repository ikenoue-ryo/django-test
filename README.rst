=======================
django-torina-tutorial1
=======================
.. image:: https://travis-ci.org/naritotakizawa/django-torina-tutorial1.svg?branch=master
    :target: https://travis-ci.org/naritotakizawa/django-torina-tutorial1

.. image:: https://coveralls.io/repos/github/naritotakizawa/django-torina-tutorial1/badge.svg
    :target: https://coveralls.io/github/naritotakizawa/django-torina-tutorial1

ここは説明です


Requirement
===========

:Python: 3.4以上
:Django: 1.10以上
 

Quick start
===========
1. pipでインストールする。::

    pip install -U https://github.com/naritotakizawa/django-torina-tutorial1/archive/master.tar.gz


2. あなたのDjangoプロジェクトのINSTALLED_APPSに、"myapp" を足す。::

    INSTALLED_APPS = [
        ...
        'myapp',
    ]

3. urls.pyに以下のようにしてincludeしてください。::

    url(r'^', include('myapp.urls')),

4. `python manage.py migrate`

5. `python manage.py runserver`

6. http://127.0.0.1:8000 へアクセス!
