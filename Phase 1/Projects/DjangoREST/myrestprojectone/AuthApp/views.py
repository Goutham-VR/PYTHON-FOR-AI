from django.shortcuts import render

# Create your views here.
# Authentication is for login
# Authorization is for "What can this user do?"

# flow is roughly

# Request
#    ↓
# Authentication
#    ↓
# Identify user
#    ↓
# Permission check
#    ↓
# Allowed?
#    ↓
# View

#====================================================================================================
# Authentication vs Permission
# Eg:
# Goutham logs in
#        ↓
# Authentication 
#        ↓
# DRF knows request.user = Goutham
#        ↓
# Permission check
#        ↓
# Is Goutham allowed to access this API?

#====================================================================================================
# DRF Authentication Methods
#====================================================================================================

# 1. SessionAuthentication
# 2. BasicAuthentication
# 3. TokenAuthentication

# Eg Structure:
from rest_framework.authentication import SessionAuthentication # import authentication
from rest_framework.permissions import IsAuthenticated # import permission
from rest_framework.generics import ListAPIView # import concrete generic apiview 
from api.models import Employee # import model
from AuthApp.serializers import EmployeeSerializer # import serializer

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all() # define qry set
    serializer_class = EmployeeSerializer # define serializer class
    authentication_classes = [SessionAuthentication] # define authentication class, How should DRF identify the user?
    permission_classes = [IsAuthenticated] # define permission class, Only allow the request if a user has been authenticated.

# Request -> SessionAuthentication -> Is there an authenticated Django session? -> Yes -> request.user -> IsAuthenticated -> Allowed -> EmployeeListView
# othervice: 
# Request -> SessionAuthentication -> No authenticated user -> IsAuthenticated? No -> 401/403 response


#================================================================================================================================================================
# SessionAuthentication
#================================================================================================================================================================
# step 1 : Create a Django User:
            # python manage.py createsuperuser
            # add details like username gmail password

# step 2 : Start the server:
            # python manage.py runserver

# step 3 : Why are we doing this?:
            # Because SessionAuthentication works with Django's authenticated user/session.

# step 4 : Then our DRF API can require login:
            # code ............................
            # You must be authenticated through a Django session to access this view.

#code:
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeListViewSA(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

# step 6 : Without Login = Test with browser becouse(Handle session cookies but for postman u need to pass it becouse it doesnt have session cookie) then you will get "Authentication credentials were not provided." 
           # http://127.0.0.1:8000/AuthApp/SessionAuthApi/

#================================================================================================================================================================
# BasicAuthentication
#================================================================================================================================================================
# Username + Password
#         ↓
# BasicAuthentication
#         ↓
# Django checks credentials
#         ↓
# request.user
#         ↓
# IsAuthenticated
#         ↓
# API access

# Basic Authentication sends the user's username and password with the API request.
# basic authentication is used by credentials Username + password
# Basic Authentication should normally be used with HTTPS, because credentials are transmitted in every request (Base64 encoding is not encryption).
# no session required here

#code:
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeListViewBA(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


#================================================================================================================================================================
# Token Authentication
#================================================================================================================================================================
# Username + Password -> Login once -> Token -> Every API request uses the token

# Step 1 — Enable Token Authentication
    # Add 'rest_framework.authtoken' in installed apps
    # run 'py manage.py migrate -> This creates the database table where DRF will store tokens. You don't need to create a new model for this part
    # The token acts like an API key for that user.
# Step 2 — Create a Token for Your User
    # use terminal
    # python manage.py drf_create_token YOUR_USERNAME
    # token is generated and stored in db use it for further cases


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeeListViewTA(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

# Thing to remeber of 3 DRF authentication:
# SESSION AUTHENTICATION
# → Authentication based on Django sessions/cookies
# → Client input is session cookie
# → mostly browser

# BASIC AUTHENTICATION
# → Authentication using username + password
# → Client input is username + password
# → can be browser, but mainly useful for simple API access/testing

# TOKEN AUTHENTICATION
# → Authentication using an API token
# → API clients
# → This is useful when the client isn't relying on Django's browser session.likeReact frontend, Mobile application, Postman, External API client

#==========================================================================Authentication End============================================================================================
# Session Authentication
# Browser automatically handles the sessionid cookie.
# In Postman/API tools, we have to add the sessionid manually in Cookies option.
# Example: Domain=127.0.0.1, Name=sessionid, Value=YOUR_SESSION_ID


# Basic Authentication
# Uses username and password.
# Browser may show a popup to enter username and password.
# In Postman: Authorization -> Basic Auth -> enter username and password.


# Token Authentication
# Uses a token in the Authorization header option.
# Example: Authorization: Token YOUR_TOKEN
# For testing, token can be created using:
# python manage.py drf_create_token admin
# This command is mainly for creating a token manually; we don't run it every time.


# JWT Authentication not needed here just for understanding
# Commonly used for token-based authentication in production applications.
# Login API verifies username and password and returns JWT tokens.
# Example: Authorization: Bearer YOUR_ACCESS_TOKEN
# JWT is different from DRF's built-in TokenAuthentication.


#====================================================================================================================================
# Permission - Built-in
#====================================================================================================================================
# Authentication is like → Who are you? 
# But Permissions is like → What are you allowed to do?
# permission_classes = [IsAuthenticated] : It means Only logged-in/authenticated users can access this API.
# Built-in permission classes are: AllowAny, IsAuthenticated, IsAdminUser, and IsAuthenticatedOrReadOnly

# AllowAny : Authentication required? No, Permission check? Everyone allowed
# IsAuthenticated : Authentication required? Yes, Permission check? Only authenticated users allowed
# IsAdminUser : Authentication required? Yes, Permission check? Only staff/admin users allowed
# IsAuthenticatedOrReadOnly : Authentication required? 
# GET / HEAD / OPTIONS → Permission allows everyone
# POST / PUT / PATCH / DELETE → User must be authenticated

# Result:
    # → Everyone can read
    # → Only authenticated users can modify

from rest_framework.authentication import BasicAuthentication # for authentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class EmployeeListViewApiPermissionSA(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]



#.....

#====================================================================================================================================
# Permission - Custom
#====================================================================================================================================
# In Built-in permission: IsAdminUser → Only admin can enter but in custom We can decide exactly who can enter
# Custom permissions become useful when the same API supports different actions for different users.

# For example, suppose you have Course API with:
# GET     → View courses
# POST    → Create course
# PUT     → Update course
# DELETE  → Delete course

# And your requirement is:

# Admin
#   → GET ✅
#   → POST ✅
#   → PUT ✅
#   → DELETE ✅

# Normal User
#   → GET ✅
#   → POST ❌
#   → PUT ❌
#   → DELETE ❌

# Now simply using ListAPIView isn't enough because you actually want POST/PUT/DELETE to exist, but only certain users should be allowed to perform them.'
# 'That's where custom permission comes in.

# Step 1 — Create permissions.py
# Step 2 — Create a custom permission and create custom permission class
# step 3 - Complete View

from rest_framework.generics import ListCreateAPIView # imported for concrete generic api view
from SearchAPIView.models import Course # imported from SearchAPIView app models.py file 
from AuthApp.serializers import CourseSerializer # imported from serializers.py file
from AuthApp.permissions import IsAuthenticatedUser # imported from permissions.py file

#==================================CourseListView with Custom permission using has_permission method=====================================================
# Only Auth user can access this
class CourseListView(ListCreateAPIView):
    queryset = Course.objects.all() # Queryset
    serializer_class = CourseSerializer # Serializer
    # We can specify authentication_classes here.
    # If we don't specify them, DRF uses the configured default authentication classes from settings.py.
    permission_classes = [IsAuthenticatedUser] # Permission class

from AuthApp.permissions import MyCustomPermissionTwo # imported from permissions.py file

# Auth user can create(POST) and get(LIST) and others can only get(LIST)
class CourseListViewTwo(ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer
    permission_classes=[MyCustomPermissionTwo]

# here auth_user table is checked 
# if we want custom user table create model with abstractuser or abstractbaseuser in models.py

#==================================Notes CreateView with Custom permission using has_permission method======================================================

# | Operation      | Example            |  has_object_permission()  |
# | -------------- | ------------------ | ------------------------- |
# | GET one object | `GET /notes/5/`    | Yes                       |
# | PUT            | `PUT /notes/5/`    | Yes                       |
# | PATCH          | `PATCH /notes/5/`  | Yes                       |
# | DELETE         | `DELETE /notes/5/` | Yes                       |
# | GET list       | `GET /notes/`      | Normally no               |
# | POST/create    | `POST /notes/`     | Normally no               |

# create a Createview to insert data in Notes Table by user
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from AuthApp.serializers import NoteSerializer
from AuthApp.models import Note
from AuthApp.permissions import NoteCreateCustomPermission

class NotesCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NoteCreateCustomPermission]
    # here we need to pass user/owner as fk so create a perform_create to override
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# has_object_permission apiview (GET one/PUT/PATCH/DELETE/)
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from AuthApp.permissions import NoteManageCustomPermission

class NotesGetOneAPIView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NoteManageCustomPermission]

class NotesGetAllAPIView(ListAPIView):
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
    serializer_class = NoteSerializer
    permission_classes = [NoteManageCustomPermission]

class NotesUpdateAPIView(UpdateAPIView):
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
    serializer_class = NoteSerializer
    permission_classes = [NoteManageCustomPermission]
    
