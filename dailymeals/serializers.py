# Django Rest Framework
from rest_framework import serializers
# Models
from .models import User, Meal, Food, UserDailyMeal


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'description')        


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'description', 'image')   


class UserDailyMealSerializer(serializers.ModelSerializer):
    user_id = UserSerializer( source='id', read_only=True)
    meal_id = MealSerializer( source='id', read_only=True)
    food_id = FoodSerializer( source='id', read_only=True)
    
    class Meta:
        model = UserDailyMeal
        fields = ('id', 'user_id', 'meal_id', 'food_id', 'image', 'note', 'date')