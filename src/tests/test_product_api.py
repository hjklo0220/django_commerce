from schema import Schema
import pytest

from product.models import Product

@pytest.mark.django_db
def test_get_product_list(api_client):
    
    Product.objects.create(name="테스트", price="1", status="active")

    response = api_client.get("/products")

    assert response.status_code == 200
    assert len(response.json()["results"]["products"]) == 1
    assert Schema(
        {
            "results": {
                "products": [
                    {"id": int, "name": "테스트", "price": 1}
                ]
            }
        }
    ).validate(response.json())