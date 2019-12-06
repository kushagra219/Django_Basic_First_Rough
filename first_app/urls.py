from django.conf.urls import url
from first_app import views

urlpatterns = [
     url(r'^$',views.users,name="index"),
     url(r'^help/',views.help,name="help"),
     url(r'^users/',views.users,name="users")
]
