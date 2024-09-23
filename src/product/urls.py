from ninja import Router
from django.http import HttpRequest
from config.response import response

from config.response import ObjectResponse
from product.models import Product, ProductStatus
from product.response import ProductDetailResponse, ProductListResponse


router = Router(tags=["Products"])

@router.get(
    "",
    response={
        200: ObjectResponse[ProductListResponse]
    },
)
def product_list_handler(request: HttpRequest):
    return 200, response(
        ProductListResponse(products=Product.objects.filter(status=ProductStatus.ACTIVE).values("id", "name", "price"))
    )