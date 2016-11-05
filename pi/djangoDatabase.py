from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length20)
    achivements = models.#unsure what to add here

CREATE TABLE app_user (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "password" varchar(20) NOT NULL,
    "achievements" multiset #unsure of exact implementation
);

class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    posts = models #unsure how to do
    estimate_time = models.IntegerField()
    keywords = models #unsure

CREATE TABLE app_routes (
    "id" serial NOT NULL PRIMARY KEY,
    "posts" #unsure
    "estimate_time" integer() NOT NULL,
    "keywords" multiset #dont know exact implementation
);
class Posts(models.Model):
    name = models.CharField(max_length=20)
    points = models.IntegerField()
    description = models.CharField(max_length=250)
    requirement = models.CharField(max_length=140)
    post_validated = models.BooleanField()

CREATE_TABLE 
    
    
    

