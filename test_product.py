"""
Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception.

Example:
    # Empty name
    Product("", price=1450, quantity=100)

    # Negative Price
    Product("MacBook Air M2", price=-10, quantity=100)
"""

import pytest
import products


def test_product_creation_with_invalid_name():
    """Test that creating a product with invalid name invokes an exception"""
    with pytest.raises(ValueError, match="The name must be a non-empty string."):
        products.Product("", 200, 2)


def test_product_creation_with_negative_price():
    """Test that creating a product with negative price invokes an exception"""
    with pytest.raises(ValueError, match="The price must be a non-negative number."):
        products.Product("MacBook", -10, 33)


def test_product_becomes_inactive_when_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = products.Product("Camera", 1000, 1)
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_total_price():
    """Test that product purchase modifies the quantity and returns the right output."""
    product = products.Product("Headphones", 200, 10)
    total_price = product.buy(3)
    assert total_price == 600
    assert product.get_quantity() == 7


def test_buying_larger_quantity_than_exists_invokes_exception():
    """Test that buying a larger quantity than exists invokes an exception."""
    product = products.Product("Tablet", 500, 5)
    with pytest.raises(Exception, match="There is not enough of this product in stock to complete the purchase."):
        product.buy(6)
