class Product:
    
    def __init__(self, reference, color, meter, price):
        self.__reference = reference
        self.__color = color
        self.__meter = meter
        self.__price = price
    
    def get_reference(self):
        return self.__reference

    def set_reference(self, reference):
        self.__reference = reference
    
    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
        
    def get_meter(self):
        return self.__meter

    def set_meter(self, meter):
        self.__meter = meter
        
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price