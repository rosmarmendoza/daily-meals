# Django Rest Framework
from rest_framework import viewsets
# Models
from .models import User, Meal, Food, UserDailyMeal
# Serializers
from .serializers import UserSerializer, MealSerializer, FoodSerializer, UserDailyMealSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()    


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class UserDailyMealViewSet(viewsets.ModelViewSet):
    serializer_class = UserDailyMealSerializer
    queryset = UserDailyMeal.objects.all()
