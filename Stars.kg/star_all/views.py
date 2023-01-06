from collections import OrderedDict

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Star, StarWork, StarComment, StarCategory, Toast, ToastCategory, Orders
from .serializers import StarCategorySerializer, StarSerializer, ToastCategorySerializer, ToastSerializer, \
    OrderSerializer


class StarPaginationClass(PageNumberPagination):
    page_size = 15
    # page_size_query_param = 'page_size'
    # max_page_size = 50
    #
    # def get_paginated_response(self, data):
    #     return Response(OrderedDict([
    #         ('total_pages', self.page.paginator.num_pages),
    #         ('page', self.page.number),
    #         ('next', self.get_next_link()),
    #         ('previous', self.get_previous_link()),
    #         ('results', data),
    #         ('results_count', len(data)),
    #         ('total_results', self.page.paginator.count),
    #     ]))


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
            kwargs['name__icontains'] = title

        category = request.query_params.get('category')
        if category:
            kwargs['category__slug'] = category

        star = star.filter(**kwargs)

        page = self.paginate_queryset(star)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


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
        kwargs = {}
        title = request.query_params.get('title')
        if title:
            kwargs['title__icontains'] = title

        category = request.query_params.get('category')
        if category:
            kwargs['category__slug'] = category

        toast = toast.filter(**kwargs)

        page = self.paginate_queryset(toast)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


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


class OrderListView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    pagination_class = StarPaginationClass
