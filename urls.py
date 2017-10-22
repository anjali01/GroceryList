from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^groceryList/$', views.GroceryListGets.as_view())
]