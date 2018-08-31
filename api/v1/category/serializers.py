from rest_framework import serializers
from data.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """ Accepting name field. """
    __doc__ = "Category Serializer"

    class Meta:
        fields = ('name',)
        model = Category


