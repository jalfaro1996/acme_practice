from acme import Product
from random import randint, uniform, choice

# Useful to use with random.sample or random.choice to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    random_a = choice(ADJECTIVES)
    random_n = choice(NOUNS)
    name = random_a + ' ' + random_n
    price = randint(5, 100)
    weight = randint(5, 100)
    flammability = uniform(0.0, 2.5)
    for i in range(num_products):
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):
    unique_names = len(set([i.name for i in products]))
    price_ave = sum([i.price for i in products]) / len(products)
    weight_ave = sum([i.weight for i in products]) / len(products)
    flammability_ave = sum([i.flammability for i in products]) / len(products)
    return (unique_names, price_ave, weight_ave, flammability_ave)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
