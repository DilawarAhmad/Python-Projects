from django.urls import path
from . import views
urlpatterns = [
    path("",views.list,name="list"),
    path("create",views.create,name="create"),
    path("<id>",views.detail,name="detail"),
    path("update/<int:id>",views.update,name="update"),
    path("delete/<int:id>",views.delete,name="delete"),
    
    
]
