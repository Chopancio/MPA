from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path("index/",login_required(views.index), name="index"),
    path("insert/", login_required(views.insert), name="insert"),
    path("update", login_required(views.update), name="update"),
    path("update/<int:task_id>", login_required(views.update_form), name="update_form"),
    path("delete/<int:task_id>", login_required(views.delete), name="delete"),
    path("",views.homepage, name="home"),
    path("registro/", views.registro, name="registro"),
]