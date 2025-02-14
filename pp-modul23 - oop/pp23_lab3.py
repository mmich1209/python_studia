class Product:
    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0

    def set_discount_percent(self, percent):
        self.__discount_in_percent = percent

    def get_current_price(self):
        result = self.__price * (1 - self.__discount_in_percent / 100)
        return round(result, 2)

    def is_category(self, category):
        return self.__category == category

    def __str__(self):
        return f'{self.__name} - {self.__category} - {self.get_current_price()} zł'


def show_products(product):
    for product in products:
        print(product)


def special_offers(products, category, discount):
    for product in products:
        if product.is_category(category):
            product.set_discount_percent(discount)



products = []
products.append(Product("mleko", "spożywcze", 3.99))
products.append(Product("masło", "spożywcze", 9.99))
products.append(Product("płyn do naczyń", "chemia", 4.49))

show_products(products)
special_offers(products, "spożywcze", 50)
print("-" * 30)
print("Promocja!!!")
show_products(products)
