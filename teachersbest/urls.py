
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView,LoginView
from teachersbest import views


urlpatterns = [

    path('', include('arg_essay.urls')),

    path('', include('basepersons.urls')),

    path('', include('quiz.urls')),

    path('teacher/',include('teacher.urls')),
    path('student/',include('student.urls')),

    path('', include('django.contrib.auth.urls')), 
    
    path('admin/', admin.site.urls),


]



