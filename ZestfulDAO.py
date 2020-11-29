import mysql.connector


# Author    : Lucero Rodriguez
# Date      : Wednesday November 25, 2020
# Purpose   : This file is used to connect to the zestful db
#             and perform the POST operation

class ZestfulDAO:
    # omitted for security
    __USER = ""
    __PW = ""
    __HOST = ""
    __DB = ""

    __SCHEMA = ""
    __INGREDIENTS_TABLE_NAME = ""
    __INSERT_INTO = "INSERT INTO"

    def __init__(self):
        pass

    # Purpose    :  POSTs Ingredients data to db using the 'Ingredients' object
    # Params     :  in_ingredients, 'Ingredients' object which holds data from zestful request
    # Returns    :  N/A
    def post_ingredients(self, in_ingredients):
        connection = mysql.connector.connect(
            user=self.__USER,
            password=self.__PW,
            host=self.__HOST,
            database=self.__DB
        )
        cursor = connection.cursor()

        values = (
            in_ingredients.get_fdc_id(),
            in_ingredients.get_quantity(),
            in_ingredients.get_unit(),
            in_ingredients.get_ingredient_category(),
            in_ingredients.get_description(),
            in_ingredients.get_match_method(),
            in_ingredients.get_raw_ingredient())
        insert_statement = self.__INSERT_INTO + " " + self.__SCHEMA + "." + self.__INGREDIENTS_TABLE_NAME \
                           + "(fdc_id, quantity, unit, ingredient_category, description, match_method, raw_ingredient) " \
                             "VALUES (%s, %s, %s, %s, %s, %s, %s)"

        try:
            cursor.execute(insert_statement, values)
            connection.commit()
            print("Inserted Ingredients with fdc_id=" + in_ingredients.get_fdc_id())

        except:
            # roll back if exception occurs
            print("Failed to insert Ingredients with fdc_id=" + in_ingredients.get_fdc_id())
            connection.rollback()

        connection.close()
