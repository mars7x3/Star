from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Star, StarWork, StarComment, StarCategory, Toast, ToastCategory, Orders
from .serializers import StarCategorySerializer, StarSerializer, ToastCategorySerializer, ToastSerializer


class StarPaginationClass(PageNumberPagination):
    page_size = 15


class ToastPaginationClass(PageNumberPagination):
    page_size = 7


class StarCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = StarCategory.objects.all()
    serializer_class = StarCategorySerializer


class StarView(viewsets.ReadOnlyModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    pagination_class = StarPaginationClass

    @action(detail=False, methods=['get'])
    def search(self, request, **kwargs):
        queryset = self.get_queryset()
        star = queryset
        title = request.query_params.get('title')
        if title:
            kwargs['title__icontains'] = title

        star = star.filter(**kwargs)

        serializer = StarSerializer(star if star.exists() else queryset, many=True)

        return Response(serializer.data)


class StarNameAndIdView(APIView):
    def get(self, request):
        star_list = []
        for s in Star.objects.all():
            star_list.append({s.id: s.name})
        return Response({'data': star_list}, status=status.HTTP_200_OK)


class ToastCategoryView(viewsets.ReadOnlyModelViewSet):
    queryset = ToastCategory.objects.all()
    serializer_class = ToastCategorySerializer


class ToastView(viewsets.ReadOnlyModelViewSet):
    queryset = Toast.objects.all()
    serializer_class = ToastSerializer
    pagination_class = StarPaginationClass

    @action(detail=False, methods=['get'])
    def search(self, request, **kwargs):
        queryset = self.get_queryset()
        toast = queryset
        title = request.query_params.get('title')
        if title:
            kwargs['title__icontains'] = title

        toast = toast.filter(**kwargs)

        serializer = ToastSerializer(toast if toast.exists() else queryset, many=True)

        return Response(serializer.data)


class ToastNameAndIdView(APIView):
    def get(self, request):
        star_list = []
        for s in Toast.objects.all():
            star_list.append({s.id: s.name})
        return Response({'data': star_list}, status=status.HTTP_200_OK)


class OrderCreateView(APIView):
    def post(self, request):
        request.data.get('')
        Orders.objects.create(star=Star.objects.get(id=request.data.get('star')),
                              first_name=request.data.get('first_name'),
                              last_name=request.data.get('last_name'), for_who=request.data.get('for_who'),
                              phone=request.data.get('phone'), email=request.data.get('email'),
                              text=request.data.get('text'),
                              price=request.data.get('price'))
        return Response({"detail": "Success!"}, status=status.HTTP_200_OK)


class StarSearchView(APIView):
    def post(self, request):
        data = Star.objects.filter(category__slug=request.data.get('category'))
        serializer = StarSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToastSearchView(APIView):
    def post(self, request):
        data = Toast.objects.filter(category__slug=request.data.get('category'))
        serializer = ToastSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

