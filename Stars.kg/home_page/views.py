from rest_framework import viewsets

from home_page.models import Banner, Popular, Catalog, CommentHomePage, Reaction
from home_page.serializers import BannerSerializer, PopularSerializer, CatalogSerializer, HomeCommentSerializer, \
    ReactionSerializer


class BannerView(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class PopularView(viewsets.ReadOnlyModelViewSet):
    queryset = Popular.objects.all()
    serializer_class = PopularSerializer


class CatalogView(viewsets.ReadOnlyModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


class CommentHomePageView(viewsets.ReadOnlyModelViewSet):
    queryset = CommentHomePage.objects.all()
    serializer_class = HomeCommentSerializer


class ReactionView(viewsets.ReadOnlyModelViewSet):
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer


