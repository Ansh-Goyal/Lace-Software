import mysql.connector as mysql
def sql_con():

    c = mysql.connect(host="localhost", user="root", password="ZQ10pm29", database="lace")
    return c
