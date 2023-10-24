from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from .forms import GeeksForm
from .models import Geeks
from django.views.generic.edit import CreateView

# Create your views here.
def create(request):
    form=GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={"form":form}
    return render(request,"create.html",context)
def list(request):
    form=Geeks.objects.all()
    context={"form":form}
    return render(request,"list.html",context)
def detail(request,id):
    details=Geeks.objects.get(id=id)
    context={"details":details}
    return render(request,"detail.html",context)
def update(request,id):
    context={}
    obj=get_object_or_404(Geeks,id=id)
    form=GeeksForm(request.POST or None ,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context={"form":form}
    return render(request,"update.html",context)
def delete(request,id):
    context={}
    obj=get_object_or_404(Geeks,id=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request,"delete.html")

