from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('delItem/<ID>', views.delItem),
    path('upItem/<ID>', views.upItem),
    path('toggleItem/<ID>', views.toggleItem),
    path('login/', views.login_page),
    path('register/', views.register_page),
    path('logout/',views.logout_page)
]