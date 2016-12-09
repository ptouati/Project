from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

app_name = 'chain'

urlpatterns = [

    # Basic Things For User
    url(r'^$', login_required(views.index) , name='index'),
    url(r'^sensors/$', login_required(views.sensors) , name='sensors'),
    url(r'^sensor/(?P<pk>[0-9]+)/$', login_required(views.sensor) , name='sensor'),
    url(r'^datas/$', login_required(views.datas) , name='datas'),
    url(r'^data/(?P<pk>[0-9]+)/$', login_required(views.data) , name='data'),

    # test -- Will Remove after Completing Project
    url(r'^test/$', login_required(views.test) , name='test'),

    #for User To getting Permission for our website
    url(r'^login/$', views.login_user , name='login'),
    url(r'^logout/$', login_required(views.logout_user) , name='logout'),
    url(r'^register/$', views.Register_User.as_view() , name='register'),

    # for managing node
    url(r'^AddNode/$', login_required(views.new_node) , name='AddNode'),
    url(r'^UpdateNode/(?P<pk>[0-9]+)/$', login_required(views.UpdateNode.as_view()) , name='UpdateNode'),
    url(r'^(?P<pk>[0-9]+)/DeleteNode/$', login_required(views.DeleteNode.as_view()) , name='DeleteNode'),

    # For user
    url(r'^AddUser/$', login_required(views.AddUser) , name='AddUser'),
    url(r'^UpdateUser/(?P<pk>[0-9]+)/$', login_required(views.UpdateUser.as_view()) , name='UpdateUser'),

    # for managing Sensor
    url(r'^AddSensor/$', login_required(views.new_sensor) , name='AddSensor'),
    url(r'^UpdateSensor/(?P<pk>[0-9]+)/$', login_required(views.UpdateSensor.as_view()) , name='UpdateSensor'),
    url(r'^(?P<pk>[0-9]+)/DeleteSensor/$', login_required(views.DeleteSensor.as_view()) , name='DeleteSensor'),

    # for managing data
    url(r'^AddData/$', login_required(views.AddData.as_view()) , name='AddData'),
    url(r'^(?P<pk>[0-9]+)/DeleteData/$', login_required(views.DeleteData.as_view()) , name='DeleteData'),

]
