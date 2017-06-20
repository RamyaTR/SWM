from django.conf.urls import url
from testing import views

urlpatterns = [
    url(r'^$', views.HomePageView),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', views.register_page),
    url(r'^logout/$', views.logout_page),
    url(r'^profile/$', views.profile_view, name ='profile'),
    url(r'^editProfile/$',views.edit_profile, name = 'edit_profile'),
    url(r'^faq/$',views.faq),
    url(r'^download/$', views.download_page),
    url(r'^form1/$', views.frm1),
    url(r'^form2/$', views.download_page),
    url(r'^form3/$', views.frm3),
    url(r'^form4/$', views.frm1),
    url(r'^form5/$', views.frm1),
    url(r'^form6/$', views.frm1),
    # url(r'^$', views.save_book),
]

