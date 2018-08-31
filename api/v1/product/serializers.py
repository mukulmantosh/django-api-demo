from rest_framework import serializers
from data.models import Category
from django.core.validators import ValidationError

class ProductSerializer(serializers.Serializer):
    """ Accepting name, category, code, price and quantity field. """

    category = serializers.CharField(required=True, max_length=255)
    code = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=50, required=True)
    price = serializers.FloatField(required=True)
    quantity = serializers.IntegerField(min_value=0, required=True)

    def validate_category(self, category):
        if Category.objects.filter(name=category).exists():
            return category
        else:
            raise ValidationError("This is not a valid category.")

