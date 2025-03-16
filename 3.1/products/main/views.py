from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        ser = ProductDetailsSerializer(product)
        return Response(ser.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        mark = request.GET.get('mark')
        reviews = product.comments.all()
        if mark is not None:
            try:
                mark = int(mark)
                reviews = reviews.filter(mark=mark)
            except ValueError:
                return Response({'error': 'оценка должна быть от 1 до 5'}, status=400)

        ser = ReviewSerializer(reviews, many=True)
        return Response(ser.data)
