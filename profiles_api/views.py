from rest_framework.views import APIView
from rest_framework.response import Response

calss HelloApiView(APIView)
   """ Test API View"""

   def grt(self,request,format=None):
       """ Returns a list of APIView features"""

       an_apiview = [
       'Uses HTTP methods as function(get,post,patch,put,delete)'
       'Is similer to a traditonal django View',
       'Give you the most control over you application logic',
       'Is mapped maunlly to URLs'

       ]

       return Response({'message':'Hellow!','an_apiview': an_apiview})
