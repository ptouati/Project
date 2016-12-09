from django.conf.urls import url,include
from django.contrib import admin
from chain import views

urlpatterns = [

    # For Admin
    url(r'^admin/', admin.site.urls),

    # for Root 
    url(r'^$', views.login_user , name='login'),

    # For App
    url(r'^chain/', include('chain.urls' , namespace="chain")),

    # for overwriting login_required decorators
    url(r'^accounts/login/$', views.login_user , name='login'),
]
