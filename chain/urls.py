from django.conf.urls import url
from . import views
app_name = 'chain'

urlpatterns = [



    url(r'^$', views.index , name='index'),
    url(r'^sensors/$', views.sensors , name='sensors'),
    url(r'^sensor/(?P<pk>[0-9]+)/$', views.sensor , name='sensor'),
    url(r'^datas/$', views.datas , name='datas'),
    url(r'^data/(?P<pk>[0-9]+)/$', views.data , name='data'),

    # test
    url(r'^test/$', views.test , name='test'),
    url(r'^tests/$', views.tests , name='tests'),

    #for User

    url(r'^login/$', views.login_user , name='login'),
    url(r'^logout/$', views.logout_user , name='logout'),
    url(r'^register/$', views.UserFormView.as_view() , name='register'),

    # for managing node

    url(r'^AddNode/$', views.new_node , name='AddNode'),
    url(r'^UpdateNode/(?P<pk>[0-9]+)/$', views.UpdateNode.as_view() , name='UpdateNode'),
    url(r'^(?P<pk>[0-9]+)/DeleteNode/$', views.DeleteNode.as_view() , name='DeleteNode'),

    # for managing Sensor

    url(r'^AddSensor/$', views.new_sensor , name='AddSensor'),
    url(r'^UpdateSensor/(?P<pk>[0-9]+)/$', views.UpdateSensor.as_view() , name='UpdateSensor'),
    url(r'^(?P<pk>[0-9]+)/DeleteSensor/$', views.DeleteSensor.as_view() , name='DeleteSensor'),

    # for managing data

    url(r'^AddData/$', views.AddData.as_view() , name='AddData'),
    url(r'^(?P<pk>[0-9]+)/DeleteData/$', views.DeleteData.as_view() , name='DeleteData'),


]
