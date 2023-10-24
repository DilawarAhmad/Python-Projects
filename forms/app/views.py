from django.shortcuts import render
from forms import *
# Create your views here.
def homeview(request):
    context={}
    form=inputform()
    context={"form":form}
    return render(request,"app/home.html",context)
