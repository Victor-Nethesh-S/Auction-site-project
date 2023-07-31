from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("item/<int:pk>/", views.item, name="item"),
    path("bid/<int:pk>/", views.bid, name="bid"),
    path("comment/<int:pk>/", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path('category/', views.category, name='category'),
    path('category/<str:selected_category>/',
         views.category_selected, name='category_selected'),
    path('close/<int:pk>/', views.close, name='close'),
    path('closelist', views.closelist, name='closelist'),


]
