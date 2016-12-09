from django.db import models
import datetime
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from itertools import chain

class Profile(models.Model):
    first_name = models.CharField(max_length = 40)
    last_name = models.CharField(max_length = 40)
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    about = models.CharField(max_length = 400, blank=True)
    doc = models.DateTimeField(blank=True, default=datetime.datetime.now)
    image = models.CharField(max_length = 400, blank = True, default = "http://www.hit4hit.org/img/login/user-icon-6.png")
    def get_absolute_url(self):
        return reverse('chain:index')
    def __str__(self):
        return self.first_name

# For Gateway --
class Gateway(models.Model):
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400, blank=True)
    doc = models.DateTimeField(blank=True, default=datetime.datetime.now)
    def __str__(self):
        return self.name

# for Node --
class Node(models.Model):
    gateway_name = models.ForeignKey(Gateway,on_delete = models.CASCADE)
    name = models.CharField(max_length = 40)
    image = models.CharField(max_length = 400 , default = "https://d3s5r33r268y59.cloudfront.net/97443/products/thumbs/2016-08-30T16:15:27.419Z-IMG-20160823-WA0018.jpg.855x570_q85_pad_rcrop.jpg")
    owner = models.ForeignKey(User,on_delete = models.CASCADE)
    description = models.CharField(max_length = 400, blank=True)
    doc = models.DateTimeField(blank=True, default=datetime.datetime.now)
    def get_absolute_url(self):
        return reverse(request , 'chain/test.html')
    def __str__(self):
    #    str1 = str(self.owner) + ' -- ' + self.name
        return self.name

# For Sensor --
class Sensor(models.Model):
    node_name = models.ForeignKey(Node,on_delete = models.CASCADE)
    name = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400, blank=True)
    image = models.CharField(max_length = 400 , default = "https://upload.wikimedia.org/wikipedia/commons/0/09/CCD_Image_sensor.jpg")
    doc = models.DateTimeField(blank=True, default=datetime.datetime.now)
    def get_absolute_url(self):
        return reverse('chain:index')
    def __str__(self):
        return self.name

# For Data --
class Data(models.Model):
    sensor_name = models.ForeignKey(Sensor,on_delete = models.CASCADE)
    data = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400, blank=True)
    doc = models.DateTimeField(blank=True, default=datetime.datetime.now)
    def get_absolute_url(self):
        return reverse('chain:index')
    def __str__(self):
        return self.data

# For Node Form
class NodeForm(ModelForm):
    class Meta:
        model = Node
        exclude = ('owner', 'doc', 'image',)

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('owner', 'doc', 'image',)

# For Sensor to set that in form you can get only User nodes.
class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        exclude = ('doc', 'image',)
    def __init__(self, var=None, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        self.fields['node_name'].queryset = Node.objects.filter(owner=var)
