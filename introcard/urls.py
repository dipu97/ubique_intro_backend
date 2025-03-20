from django.urls import path
from . import views


urlpatterns = [
    path("register_user/", views.register_user, name="register_user"),
    path("create_card/", views.create_card, name="create_card"),
    path("card_list/", views.card_list, name="card_list"),
    path("cards/<str:pk>", views.get_card, name="get_card"),
    path("update_card/<str:pk>/", views.update_card, name="update_card"),
    path("delete_card/<str:pk>/", views.delete_card, name="delete_card"),
    path("update_user/", views.update_user_profile, name="update_user"),
    path("get_username/", views.get_username, name="get_username"),
    path("get_userinfo/<str:username>", views.get_userinfo, name="get_userinfo"),
    path("get_user/<str:email>", views.get_user, name="get_user")
]