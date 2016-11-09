=====
Django Clusters
=====

Django clusters is a django app that use multidimensional scaling to group articles, blogs or any kind of document to cluster by similarity. 

The similarity is scaled down to two dimensions
 
D3.js is used to draw the articles on a 2D HTML5 canvas. 


Warning
-----------

This app is in very alpha version, and therefore I have not included a setup.py packaging. 

However, the app contains extensive unit testing, particularly probabilistic unit testing. Therefore, feel free to browse docs and see how various components can be tested at various level. 

Demo
-----------
A typical output looks like the image below:
 
![Output from django clusters](http://i.imgur.com/Tugs7FC.png)

As you can see, similar articles are grouped together in a two-dimensional view. The rectangles are manually drawn to show how the algorithm groups articles together. 
![Output from django clusters](http://i.imgur.com/4mqZ1ek.png)



Quick start
-----------
1. Add "djano_clusters" in your root project folder.

2. Add "django_clusters" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_cluster',
    ]

3. Include the polls URLconf in your project urls.py like this::

    url(r'^django_cluster/', include('django_cluster.urls')),

4. Start the development server and visit http://127.0.0.1:8000/dcluster/blogs/view/ to visualize. 

5. Visit http://127.0.0.1:8000/dcluster/blogs/json/ to view the json that d3.js used to draw data on the canvas. 



Settings
-----------
Your settings.py file (or whatever you use as your main settings file) need to contain the following settings. DC_TITLE_FIELD is the main title field that shows up as the titles in the visualization.  DC_CONTENT_FIELD is the main content field. DC_MODEL is the model that will contain the above two fields. 
  
    DC_MODEL = 'blog.Blog' # app.model
    DC_CONTENT_FIELD = 'content'
    DC_TITLE_FIELD = 'title'
    DC_SLUG_FIELD = 'slug'
    DC_SVG_WIDTH = 1000
    DC_SVG_HEIGHT = 400