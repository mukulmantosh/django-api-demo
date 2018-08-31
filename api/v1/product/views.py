from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from data.models import Product, Category
from django.db import transaction, IntegrityError
from . import serializers


class ProductAPI(APIView):
    permission_classes = (AllowAny,)
    serializers_class = serializers.ProductSerializer

    def post(self, request):
        try:
            serializer = self.serializers_class(data=request.data)
            if serializer.is_valid():
                clean_data = serializer.data
                category = clean_data["category"]
                code = clean_data["code"]
                name = clean_data["name"]
                price = clean_data["price"]
                quantity = clean_data["quantity"]

                try:
                    with transaction.atomic():

                        category_model = Category.objects.get(name=category)
                        Product.objects.create(category=category_model, code=code,
                                               name=name, price=price, quantity=quantity)
                except IntegrityError:
                    transaction.rollback()
                    return Response({"status": False, "message": "We are facing some issues.", "data": None},
                                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                return Response({"status": True, "message": "New Product Added !", "data": None},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({"status": False, "message": serializer.errors, "data": None},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status": False, "message": "Internal Server Error", "data": None},
                            status == status.HTTP_500_INTERNAL_SERVER_ERROR)



class ProductListingAPI(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = serializers.ProductListSerializer