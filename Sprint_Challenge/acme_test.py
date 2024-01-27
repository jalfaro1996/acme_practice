from acme import Product


def test_default_product_price():
    '''Test default product price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10


def test_stealability():
    assert Product.stealability(5.0) == "Very stealable!"


def test_explode():
    assert Product.explode(3) == "...fizzle"


def test_generate_products():
    assert Product.num_products == 30
