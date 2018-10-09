class Partner:
    
    def __init__(self, partner_type, company):
        self.__partner_type = partner_type  
        self.__company = company
        
    def get_partner_type(self):
        return self.__partner_type
    
    def set_partner_type(self, partner_type):
        self.__partner_type = partner_type

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company
