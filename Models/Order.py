class Order:

    def __init__(self, supplier, client, expected_delivery_date, products, payment_type):
        self.__supplier = supplier
        self.__client = client
        self.__expected_delivery_date = expected_delivery_date
        self.__products = products
        self.__payment_type = payment_type
        
    def get_supplier(self):
        return self.__supplier
    
    def set_supplier(self, supplier):
        self.__supplier = supplier

    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def get_expected_delivery_date(self):
        return self.__expected_delivery_date

    def set_expected_delivery_date(self, expected_delivery_date):
        self.__expected_delivery_date = expected_delivery_date
        
    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products
        
    def get_payment_type(self):
        return self.__payment_type

    def set_payment_type(self, payment_type):
        self.__payment_type = payment_type