=====
Django Clusters
=====

Django clusters is a django app that use multidimensional scaling to group articles, blogs or any kind of document to cluster by similarity. 

Detailed documentation is in the "docs" directory.


Warning
-----------

This app is in very alpha version, and therefore I have not included a setup.py packaging. 

However, the app contains extensive unit testing, particularly probabilistic unit testing. Therefore, feel free to browse docs and see how various components can be tested at various level. 

Demo
-----------
A typical output looks like the image below. 
 
![Output from django cluster](http://i.imgur.com/Tugs7FC.png "Output from django clusters")


Quick start
-----------
1. Add "djano_clusters" in your root project folder.

2. Add "django_clusters" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_clusters',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.

