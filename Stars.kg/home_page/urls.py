from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('banners', BannerView)
router.register('populars', PopularView)
router.register('catalogs', CatalogView)
router.register('comments', CommentHomePageView)
router.register('reactions', ReactionView)

urlpatterns = [
    path('', include(router.urls)),

]
