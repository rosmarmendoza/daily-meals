from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    class Meta:
        db_table = 'users'



class Meal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    class Meta:
        db_table = 'meals'


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)
    class Meta:
        db_table = 'foods'


class UserDailyMeal(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    note = models.TextField()
    date = models.DateField()
   
    class Meta:
        db_table = 'users_daily_meals'