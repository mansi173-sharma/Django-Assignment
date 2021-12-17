from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponseRedirect
import operator
import django_filters

from api_project.serializers import UserSerializer
from api_project.models import User

#Function to check whether pattern is present in string
def isContains(string, pattern):
   string = string.lower()
   pattern = pattern.lower()
   if pattern in string:
      return True
   return False

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   
   filter_fields = (
      'first_name',
      'last_name',
      'company_name',
      'age',
      'id'
   )

   def get_queryset(self):
      sort = self.request.query_params.get('sort')
      name = self.request.query_params.get('name')
      page = self.request.query_params.get('page')
      limit = self.request.query_params.get('limit')
      queryset = User.objects.all()
      

      #limit & page are automatically handled by django rest framework
      if name:
         print("name" + name)
         updatedQueryset = []
         for x in queryset:
            if (isContains(x.first_name, name) or isContains(x.last_name, name)):
               updatedQueryset.append(x)
         queryset = updatedQueryset
      
      if sort:
         isReverse = False
         if (sort[0] == '-'):
            isReverse = True
            sort = sort[1:]
         queryset = sorted(queryset, key=lambda x: getattr(x, sort), reverse=isReverse) 
      return queryset

   serializer_class = UserSerializer


#This view is made to redirect the current url to api/users: currently it is our default view
def redirectView(request):
    ...
    return HttpResponseRedirect("/api/users")
