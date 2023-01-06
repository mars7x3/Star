from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *

router = DefaultRouter()
router.register('categories', StarCategoryView)
router.register('stars', StarView)
router.register('toasts-categories', ToastCategoryView)
router.register('toasts', ToastView)
router.register('orders', OrderListView)

urlpatterns = [
    path('', include(router.urls)),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('name-and-id/', StarNameAndIdView.as_view()),
    path('toast-and-id/', ToastNameAndIdView.as_view()),
    path('order-create/', OrderCreateView.as_view()),

]
