from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    # path('playground/hello', views.say_hello)
    path('results/',views.no_results),
    path('mean/',views.mean),
    path('median/',views.median),
]