import mysql.connector

# Імпортуємо конфігурацію (параметри підключення до БД)
from config import Config


def execute_query(query, args=(), commit=False, one=False):
    """
    Універсальна функція для виконання SQL-запитів.

    query  — SQL-запит
    args   — параметри для запиту (%s)
    commit — чи потрібно зберігати зміни (INSERT, UPDATE, DELETE)
    one    — чи потрібно повернути лише один запис
    """

    # Підключаємося до бази даних
    connection = mysql.connector.connect(**Config.DB_CONFIG)

    # cursor з dictionary=True повертає дані у вигляді словника
    cursor = connection.cursor(dictionary=True)

    try:
        # Виконуємо SQL-запит
        cursor.execute(query, args)

        # Якщо це INSERT / UPDATE / DELETE
        if commit:
            connection.commit()
            # Повертаємо ID останнього доданого запису
            return cursor.lastrowid

        # Якщо потрібно отримати один запис
        if one:
            return cursor.fetchone()

        # Якщо потрібно отримати всі записи
        return cursor.fetchall()

    finally:
        # Закриваємо курсор і з'єднання з БД
        cursor.close()
        connection.close()


# функції   враховано захист "%s"
# READ — отримати всі лістинги
def get_all_listings():
    return execute_query("SELECT * FROM listing_csv2")


# READ — отримати один лістинг за ID
def get_listing(listing_id):
    return execute_query(
        "SELECT * FROM listing_csv2 WHERE id=%s",
        (listing_id,),
        one=True
    )


# CREATE — додати новий лістинг
def add_listing(title, description, price):
    return execute_query(
        "INSERT INTO listing_csv2 (title, description, price) VALUES (%s, %s, %s)",
        (title, description, price),
        commit=True
    )


# UPDATE — оновити існуючий лістинг
def update_listing(listing_id, title, description, price):
    execute_query(
        "UPDATE listing_csv2 SET title=%s, description=%s, price=%s WHERE id=%s",
        (title, description, price, listing_id),
        commit=True
    )

# DELETE
def delete_listing(listing_id):
    execute_query(
        "DELETE FROM listing_csv2 WHERE id=%s",
        (listing_id,),
        commit=True
    )