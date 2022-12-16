from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('categories', StarCategoryView)
router.register('stars', StarView)
router.register('toasts-categories', ToastCategoryView)
router.register('toasts', ToastView)

urlpatterns = [
    path('', include(router.urls)),
    path('name-and-id/', StarNameAndIdView.as_view()),
    path('toast-and-id/', ToastNameAndIdView.as_view()),

]
