from rest_framework import serializers

from .models import *


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:        
#       model = tblProducts
#       fields = ['id', 'product_name', 'price_out','product_image','product_created']

# class CategoriesSerializer(serializers.ModelSerializer):
#     class Meta:        
#       model = Category
#       fields = ['id', 'category_name', 'category_image','date_created']

# class SlidesSerializer(serializers.ModelSerializer):
#     class Meta:        
#       model = tblSlides
#       fields = ['id', 'slideName', 'slideImage','slideDescription','active']