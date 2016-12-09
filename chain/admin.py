from django.contrib import admin
from .models import Gateway, Node, Sensor,Data

# registering So we can access all data from Admin account,
admin.site.register(Gateway),
admin.site.register(Node),
admin.site.register(Sensor),
admin.site.register(Data),
