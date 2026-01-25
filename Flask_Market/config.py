import os

class Config:
    SECRET_KEY = 'glass_shop_secret'
    DB_CONFIG = {
        'host': "localhost",
        'port': '3306',
        'database': 'market',
        'user': 'root',
        'password': 'usbw'
    }

# підключення до MySQL
"""Flask тримання та надання даних SQL https://jsonplaceholder.typicode.com/ API мають відображатися в цьому форматі
перетворюємо дані з нашої бази і перетворюємо в формат json 
після чого надаємо 
https://www.postman.com/ """