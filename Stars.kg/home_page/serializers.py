from rest_framework import serializers

from home_page.models import Banner, Popular, Catalog, CommentHomePage, Reaction


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class HomeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentHomePage
        fields = '__all__'


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'


