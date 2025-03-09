from django.urls import path,include
from tasks import views
urlpatterns = [
path("",views.index,name="index"),
]