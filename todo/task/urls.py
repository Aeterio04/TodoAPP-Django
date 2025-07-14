from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.register, name="signup"),
    path("add", views.add, name="add"),
    path("incomplete/<int:taskID>",views.incomplete, name="incomplete"),
    path("complete/<int:taskID>",views.complete,name="complete"),
    path("delete/<int:taskID>",views.delete,name="delete"),
    path("update/<int:taskID>",views.update,name="delete"),
    path("logout", views.logoutcall, name="logout"),
]