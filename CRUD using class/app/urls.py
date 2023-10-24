from django.urls import path
from . views import GeeksCreate,GeeksList,GeeksDetail,GeeksUpdate,GeeksDelete
urlpatterns = [
    path('',GeeksCreate.as_view()),
    path("list",GeeksList.as_view()),
    path("<pk>",GeeksDetail.as_view()),
    path("update/<pk>",GeeksUpdate.as_view()),
    path("delete/<pk>",GeeksDelete.as_view())


]
