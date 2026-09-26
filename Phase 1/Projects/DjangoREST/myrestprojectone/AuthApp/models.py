# Some important information about django models creation
# models.Model -> Just a model
# AbstractUser -> Ready-made Django User + customize it
# AbstractBaseUser -> Basic authentication foundation + build the User system yourself

# 1. class User(models.Model):

# 2. class User(AbstractUser):
    #  │
    #  ├── username
    #  ├── password
    #  ├── first_name
    #  ├── last_name
    #  ├── email
    #  ├── is_staff
    #  ├── is_active
    #  ├── is_superuser
    #  ├── groups
    #  └── permissions

# 3. class User(AbstractBaseUser):
    #    │
    #    └── You build the rest
    #          │
    #          ├── email
    #          ├── name
    #          ├── is_staff
    #          ├── is_active
    #          ├── UserManager
    #          └── permissions setup

# | Feature                              | models.Model | AbstractUser | AbstractBaseUser |
# |--------------------------------------|--------------|--------------|------------------|
# | Normal DB model                      | Yes          | Yes          | Yes              |
# | Can be used as auth user             | No           | Yes          | Yes              |
# | Password handling                    | No           | Yes          | Yes              |
# | request.user with Django auth        | No           | Yes*         | Yes*             |
# | is_staff built in                    | No           | Yes          | No*              |
# | is_superuser built in                | No           | Yes          | No*              |
# | Username system                      | No           | Yes          | You decide       |
# | UserManager required                 | No           | Usually no   | Usually yes      |
# | Customization                        | Basic        | Easy         | Maximum          |
# | Complexity                           | Low          | Medium       | High             |

from django.db import models
from django.contrib.auth.models import User # import auth user model

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)