
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import GeeksModel
# Create your views here.
class GeeksCreate(CreateView):
    model=GeeksModel
    fields=["title",'description']
    success_url="/"
    
class GeeksList(ListView):
    model=GeeksModel
class GeeksDetail(DetailView):
    model=GeeksModel
class GeeksUpdate(UpdateView):
    model=GeeksModel
    fields=['title','description']
    success_url="/"
class GeeksDelete(DeleteView):
    model=GeeksModel
    success_url="/"