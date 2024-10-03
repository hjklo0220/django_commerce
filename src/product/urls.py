from typing import List
from ninja import Router
from django.http import HttpRequest
from config.response import response

from config.response import ObjectResponse
from product.models import Category, Product, ProductStatus
from product.response.category_response import CategoryListResponse
from product.response.product_response import ProductDetailResponse, ProductListResponse


router = Router(tags=["Products"])

@router.get(
    "",
    response={
        200: ObjectResponse[ProductListResponse]
    },
)
def product_list_handler(request: HttpRequest, category_id: int | None = None):
    if category_id:
        category: Category | None = Category.objects.filter(id=category_id).first()
        if not category:
            products = []
        else:
            category_ids: List[int] = [category.id] + list(category.children.values_list("id", flat=True))
            products = Product.objects.filter(
                category_id__in=category_ids, status=ProductStatus.ACTIVE
            ).values("id", "name", "price")
    else:
        products = Product.objects.filter(status=ProductStatus.ACTIVE).values("id", "name", "price")

    return 200, response(ProductListResponse(products=products))

@router.get(
    "/categories",
    response={
        200: ObjectResponse[CategoryListResponse],
    },
)
def categories_list_handler(request: HttpRequest):
    return 200, response(
        CategoryListResponse.build(categories=Category.objects.filter(parent=None))
    )