import random


class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        x = self.price/self.weight
        if x < 0.5:
            return "Not so stealable..."
        elif x >= 0.5 and x < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        y = self.flammability * self.weight
        if y < 10:
            return "...fizzle"
        elif y >= 10 and y < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        super().__init__(name, price=price, weight=weight,
                         flammability=flammability, identifier=identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
