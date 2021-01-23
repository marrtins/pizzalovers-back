from django.urls import path
from .views import current_user, UserList, PizzaLoversView

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('pizzalovers/', PizzaLoversView.as_view()),
]