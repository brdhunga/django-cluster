from django.conf.urls import include, url

from .views import home_view, json_view


urlpatterns = [
    # Examples:
    # url(r'^$', 'dCluster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blogs/view/', home_view, name="home"),
    url(r'^blogs/json/', json_view, name="json"),

]