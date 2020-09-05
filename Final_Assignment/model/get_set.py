class SaveRegistration:
    def __init__(self, username, password):
        self.username= username
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password


class Product:
    def __init__(self, product_name, brand, price, category, mfd, exp):
        self.product_name = product_name
        self.brand = brand
        self.price = price
        self.category - category
        self.mfd=mfd
        self.exp=exp

    def set_product_name(self, product_name):
        self.product_name = product_name

    def get_product_name(self):
        return self.product_name

    def set_brand(self, brand):
        self.brand = brand
    def get_brand(self):
        return self.brand

    def set_price(self, price):
        self.price = price
    def get_price(self):
        return self.price

    def set_category(self, category):
        self.category = category
    def get_category(self):
        return self.category

    def set_mfd(self, mfd):
        self.mfd = mfd
    def get_mmfd(self):
        return self.mfd

class Order:
    def __init__(self, quantity,amount,contact, payment_method):
        self.quantity = quantity
        self.contact =contact
        self.amount = amount
        self.payment_method = payment_method

    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_amount(self, amount):
        self.amount = amount
    def get_amount(self):
        return self.amount

    def set_contact(self, contact):
        self.contact = contact
    def get_contact(self):
        return self.contact

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method
    def get_payment_method(self):
        return self.payment_method
