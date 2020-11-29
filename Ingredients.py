# Author    : Lucero Rodriguez
# Date      : Wednesday November 24, 2020
# Purpose   : This class will be used to store the deserialized version
#             of the JSON returned from the 'Zestfuldata API' request

class Ingredients:
    __fdc_id = None
    __quantity = None
    __unit = None
    __ingredient_category = None
    __description = None
    __match_method = None
    __raw_ingredient = None

    def __init__(self):
        pass

    def get_fdc_id(self):
        return self.__fdc_id

    def set_fdc_id(self, fdc_id):
        self.__fdc_id = fdc_id

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_unit(self):
        return self.__unit

    def set_unit(self, unit):
        self.__unit = unit

    def get_ingredient_category(self):
        return self.__ingredient_category

    def set_ingredient_category(self, ingredient_category):
        self.__ingredient_category = ingredient_category

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_match_method(self):
        return self.__match_method

    def set_match_method(self, match_method):
        self.__match_method = match_method

    def get_raw_ingredient(self):
        return self.__raw_ingredient

    def set_raw_ingredient(self, raw_ingredient):
        self.__raw_ingredient = raw_ingredient
