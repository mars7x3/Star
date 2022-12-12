from rest_framework import viewsets
from .models import Star, StarWork, StarComment, StarCategory
from .serializers import StarCategorySerializer, StarSerializer


class StarCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = StarCategory.objects.all()
    serializer_class = StarCategorySerializer


class StarView(viewsets.ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


