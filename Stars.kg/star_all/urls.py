from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', StarCategoryView)
router.register('stars', StarView)


urlpatterns = [
    path('', include(router.urls)),

]
