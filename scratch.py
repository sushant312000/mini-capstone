import pymysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Sushant@03',
                             database='crime_data')

print(connection)