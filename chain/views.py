from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate,login, logout
from .forms import UserForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        mynodes = Node.objects.filter(owner=request.user)
        return render(request, 'chain/index.html' , { 'mynodes' : mynodes})

def test(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        return render(request, 'chain/base1.html' )

def tests(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        return render(request, 'chain/base2.html' )

class UserFormView(View):
    form_class = UserForm
    template_name = 'chain/reg.html'

    def get(self,request):
        form = self.form_class(None)
        return render (request,self.template_name , {'form' :form })

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # normalised data_set
            username = form.cleaned_data ['username']
            password = form.cleaned_data ['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username,password=password)
            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect ('chain:index')
        return render(request, self.template_name , {'form': form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                mynodes = Node.objects.filter(owner=request.user)
                return render(request, 'chain/index.html', {'mynodes' : mynodes})
            else:
                return render(request, 'chain/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'chain/login.html', {'error_message': 'Invalid login'})
    return render(request, 'chain/login.html')

def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        logout(request)
        return render(request, 'chain/login.html')

class AddNode(CreateView):
        model= Node
        fields = ['gateway_name','name','owner']


class UpdateNode(UpdateView):
        model= Node
        fields = ['gateway_name','name','owner']

class DeleteNode(DeleteView):
        model= Node
        success_url = reverse_lazy('chain:index')


class AddSensor(CreateView):
        model= Sensor
        fields = ['node_name','name']

class UpdateSensor(UpdateView):
        model= Sensor
        fields = ['node_name','name']

class DeleteSensor(DeleteView):
        model= Sensor
        success_url = reverse_lazy('chain:index')

def sensors(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        mynodes = Node.objects.filter(owner=request.user)
        return render(request, 'chain/sensors.html' , { 'mynodes' : mynodes})

def sensor(request,pk):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        mynodes = Node.objects.filter(pk=pk)
        return render(request, 'chain/sensor.html' , { 'mynodes' : mynodes})

def data(request,pk):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        mysensors = Sensor.objects.filter(pk=pk)
        return render(request, 'chain/data.html' , { 'mysensors' : mysensors})

def datas(request):
    if not request.user.is_authenticated():
        return render(request, 'chain/login.html')
    else:
        mynodes = Node.objects.filter(owner=request.user)
        return render(request, 'chain/datas.html' , { 'mynodes' : mynodes})



class AddData(CreateView):
        model= Data
        fields = ['sensor_name','data' ]

class DeleteData(DeleteView):
        model= Data
        success_url = reverse_lazy('chain:index')

def new_node(request):
    if request.method == "POST":
        form = NodeForm(request.POST or None )
        if form.is_valid():
            temp_node = form.save(commit=False)
            temp_node.owner = request.user
            temp_node.save()
            mynodes = Node.objects.filter(owner=request.user)
            return render(request, 'chain/index.html' , { 'mynodes' : mynodes})
        else:
            form = NodeForm(initial={'owner': request.user})
            return render(request, 'chain/node_form.html', {'form': form})
    else:
        form = NodeForm()
        return render(request, 'chain/node_form.html', {'form': form})



def new_sensor(request):
    if request.method == "POST":
        form = SensorForm(request.user, request.POST or None )
        if form.is_valid():
            temp_sensor = form.save(commit=False)
            if temp_sensor.node_name.owner == request.user:
                temp_sensor.save()
                mynodes = Node.objects.filter(owner=request.user)
                return render(request, 'chain/index.html' , { 'mynodes' : mynodes})
            else:
                form = SensorForm( request.user)
                return render(request, 'chain/sensor_form.html', {'form': form ,'error_message': 'Not your node'})

        else:
            form = SensorForm( request.user)
            return render(request, 'chain/sensor_form.html', {'form': form})
    else:
        form = SensorForm( request.user)
        return render(request, 'chain/sensor_form.html', {'form': form})
