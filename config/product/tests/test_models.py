import pytest 
from product.models import Product

# тест 1 проверяем создание продукта 
@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name = "Apples",
        price = 999.99,
        in_stock = True
    )
    assert product.name == "Apples"
    assert product.price == 999.99
    assert product.in_stock == True
    