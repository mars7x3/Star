from rest_framework import serializers
from star_all.models import StarCategory, Star, StarComment, StarWork, ToastCategory, Toast


class StarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StarCategory
        fields = '__all__'


class RecommendationStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = StarCommentSerializer(instance.star_comments.all(),
                                                           many=True, context=self.context).data
        representation['works'] = StarWorkSerializer(instance.star_works.all(),
                                                     many=True, context=self.context).data
        representation['recommendations'] = RecommendationStarSerializer(instance.category.stars.all(),
                                                     many=True, context=self.context).data

        return representation


class StarCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarComment
        fields = '__all__'


class StarWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarWork
        fields = '__all__'


class ToastCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ToastCategory
        fields = '__all__'


class ToastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toast
        fields = '__all__'
