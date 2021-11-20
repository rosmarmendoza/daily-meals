# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework import routers

# Views
from . import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'meals', views.MealViewSet, basename='meals')
router.register(r'foods', views.FoodViewSet, basename='foods')
router.register(r'users-daily-meals', views.UserDailyMealViewSet, basename='users-daily-meals')

urlpatterns = [
    path('', include(router.urls)),
]