from mongoengine import *
from datetime import datetime
import os
import json

connect("mongo-dev-db")

# Define documents


class User(Document):
    username = StringField(unique=True, required=True)
    email = EmailField(unique=True)
    password = BinaryField(required=True)
    age = IntField()
    bio = StringField(max_length=100)
    categories = ListField()
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "bio": self.bio,
            "categories": self.categories,
            "admin": self.admin,
            "registered": self.registered
        }
        return json.dumps(user_dict)

    meta = {
        "indexes": ["username", "email"],
        "ordering": ["-date_created"]
    }

# Dynamic documents


class BlogPost(DynamicDocument):
    title = StringField()
    content = StringField()
    author = ReferenceField(User)
    date_created = DateTimeField(default=datetime.utcnow)

    meta = {
        "indexes": ["title"],
        "ordering": ["-date_Created"]
    }

# Save a document

# Primeira forma de usar
# user = User(
#     username="Higor Souza 4",
#     email="higor.souza4@hotmail.com",
#     password=os.urandom(16),
#     age=29,
#     bio="Hello Povo",
#     admin=True
# ).save()
#
# BlogPost(
#     title="My first blog post 3",
#     content="MongoDB and Python is Awesome 3",
#     author=user,
#     tags=["Python", "MongoDB", "MongoEngine", "3"],
#     catgory="MongoDB 3",
#     name="Higor 3"
# ).save()
#
# print("Done")


# Segunda forma de usar

user = User(
    username="Higor Souza 5",
    email="higor.souza5@hotmail.com",
    password=os.urandom(16),
    age=30,
    bio="Hello Povo 5",
)

user.admin = True
user.registered = True

# try:
#     user.save()
# except NotUniqueError:
#     print("Username or mail is not unique")

# Querying database

# users = User.objects()
#
# for user in users:
#     print(user.username, user.email, user.bio)


# Filtering
# admin_users = User.objects(admin=True, registered=True)
#
# for a in admin_users:
#     print(a.username)

# try:
#     higor = User.objects(username="HigorSouza").get()
#     print(higor.username, higor.email)
# except DoesNotExist:
#     print("User not exist")

# higor = User.objects(username="HigorSouza").get()
#
# posts = BlogPost.objects(author=higor)
#
# for post in posts:
#     print(post.author.username)


# Query operators

# Less than & greater than

# uuusers = User.objects(age__lt=30)
# for user in uuusers:
#     print(user.username, user.age)

# user_older = User.objects(age__gte=30)
# for user in user_older:
#     print(user.username, user.age)

# Query a list

# posts_tagged_python = BlogPost.objects(tags="MongoEngine")
# posts_tagged_python = BlogPost.objects(tags__in=["MongoEngine"])
#
# for post in posts_tagged_python:
#     print(post.content)

# String queries

# python_posts = BlogPost.objects(content__icontains="MongoDB")
#
# for post in python_posts:
#     print(post.content)

# Limiting and skipping results

# Get the first

# first = BlogPost.objects().first()
# print(first.title)

# Get the first 2 documents
# first_2 = BlogPost.objects()[:2]
# for post in first_2:
#     print(post.title)

# Get the first 2 documents

# all_but = BlogPost.objects()[2:]
# for post in all_but:
#     print(post.title)


# sliced = BlogPost.objects()[2:4]
# for post in sliced:
#     print(post.title)

# Counting

# user_count = User.objects().count()
# print(user_count)


# Aggregation

# average = BlogPost.objects.average("rating")
# print(average)

# total_rating = BlogPost.objects.sum("rating")
# print(total_rating)


# user = User.objects(username="HigorSouza").get()
# print(user.json())