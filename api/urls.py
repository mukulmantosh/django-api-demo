from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import api.v1.category.views as category_views
import api.v1.product.views as product_views

app_name = 'api'

router = DefaultRouter()
router.register(r'category', category_views.CategoryAPI, base_name='category')

urlpatterns = [

    url(r'^', include(router.urls, namespace="category")),
    url(r'^product/', product_views.ProductAPI.as_view(), name='product'),

]
