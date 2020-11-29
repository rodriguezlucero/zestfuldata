from ZestfulDAO import ZestfulDAO
from Ingredients import Ingredients


# Author    : Lucero Rodriguez
# Date      : Wednesday November 25, 2020
# Purpose   : This file is used to parse through the returned json from
#             the 'Zestfuldata API' request. It then POSTS that data into the db

class Requests:
    __RESULTS = "results"
    __INGREDIENT_RAW = "ingredientRaw"
    __INGREDIENT_PARSED = "ingredientParsed"
    __QUANTITY = "quantity"
    __UNIT = "unit"
    __USDA_INFO = "usdaInfo"
    __CATEGORY = "category"
    __DESCRIPTION = "description"
    __FDC_ID = "fdcId"
    __MATCH_METHOD = "matchMethod"

    __zestful_dao = None

    def __init__(self):
        self.__zestful_dao = ZestfulDAO()

    # Purpose    :  parses json request and then POSTs data to db
    # Params     :  request, zestfuldata json
    # Returns    :  N/A
    def insert_zestful_data(self, request):
        zestful_data = request
        ingredients = Ingredients()

        for results in zestful_data[self.__RESULTS]:
            ingredients.set_raw_ingredient(results[self.__INGREDIENT_RAW])

            ingredient_parsed = results[self.__INGREDIENT_PARSED]
            if ingredient_parsed is not None:
                ingredients.set_quantity(ingredient_parsed[self.__QUANTITY])
                ingredients.set_unit(ingredient_parsed[self.__UNIT])

            usda_info = ingredient_parsed[self.__USDA_INFO]
            if usda_info is not None:
                ingredients.set_ingredient_category(usda_info[self.__CATEGORY])
                ingredients.set_description(usda_info[self.__DESCRIPTION])
                ingredients.set_fdc_id(usda_info[self.__FDC_ID])
                ingredients.set_match_method(usda_info[self.__MATCH_METHOD])

            self.__zestful_dao.post_ingredients(ingredients)
