from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class User_Details(forms.Form):
    def __init__(self, *args, **kwargs):
        #self._user = kwargs.pop('user')
        super(User_Details, self).__init__(*args, **kwargs)

class Addrecord(View):
    #template_name = 'home.html'
    def post(self,request,*args,**kwargs):
        form = MyForm(data=request.POST)
        return 200 

class Editrecord(View):
    #template_name = 'home.html'
    
    def get(self,self,request,*args,**kwargs):
        # to get record
        form = MyForm(data=request.GET)
        return record
    
    def post(self,request,*args,**kwargs):
        #to update record
        form = MyForm(data=request.POST)
        return 200 

    
urlpatterns = patterns('',
        (r'^addrecord/$', Addrecord.as_view()),
        (r'^editrecord/$',Editrecord.as_view()), # for post
        (r'^editrecord/$',Editrecord.as_view()), # for Get
    )