from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    achivements = models.CharField(max_length=30)

CREATE TABLE app_user (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "password" varchar(20) NOT NULL,
    "achievements" varchar(30),
);

class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    posts = models.CharField(max_length=20)
    estimate_time = models.CharField(max_length=10)
    keywords = models.CharField(max_length=30)

CREATE TABLE app_routes (
    "id" serial NOT NULL PRIMARY KEY,
    "posts" varchar(20) NOT NULL,
    "estimate_time" varchar (10) NOT NULL,
    "keywords" varchar(30) NOT NULL,
);
class Achievements(models.Model):
    name = models.CharField(max_length=20)
    points = models.CharField(max_length=5)
    description = models.CharField(max_length=250)
    requirement = models.CharField(max_length=140)
    post_validated = models.CharField(max_length=5)

CREATE_TABLE app_achievements (
    "name" varchar(20) NOT NULL PRIMARY KEY,
    
    
    
    
    

