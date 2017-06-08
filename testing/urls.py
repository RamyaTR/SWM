from django.conf.urls import url
from testing import views

urlpatterns = [
    url(r'^$', views.HomePageView),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', views.register_page),
    url(r'^logout/$', views.logout_page),
    # url(r'^$', views.save_book),
]
