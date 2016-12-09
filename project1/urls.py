from django.conf.urls import url,include
from django.contrib import admin
from chain import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

urlpatterns = [

    # For Admin
    url(r'^admin/', admin.site.urls),

    # for Root
    url(r'^$', login_required(views.index) , name='login'),

    # For App
    url(r'^chain/', include('chain.urls' , namespace="chain")),

    # for overwriting login_required decorators
    url(r'^accounts/login/$', views.login_user , name='login'),
]
