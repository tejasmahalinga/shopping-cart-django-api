from .serializers import CartItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import CartItem
from django.shortcuts import get_object_or_404

# Create your views here.
class CartItemViews(APIView):
    def post(self,request):
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        #get by id
        if id:
            try:
                item = CartItem.objects.get(id=id)
                print("item>>>",item)
                serializer=CartItemSerializer(item)
                return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)    
            except:
                return Response({"status":"error","data":"No data found!"},status=status.HTTP_400_BAD_REQUEST)
                
        # get list
        items = CartItem.objects.all()
        serializer=CartItemSerializer(items,many=True)
        return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
    
    
    def patch(self,request,id=None):
        item = CartItem.objects.get(id=id)
        serializer=CartItemSerializer(item,data=request.data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        item = get_object_or_404(CartItem,id=id)
        item.delete()
        return Response({"status":"success","data":"Item deleted"})