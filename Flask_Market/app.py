from flask import Flask, render_template, request, redirect, url_for, flash
from api import api

# Імпортуємо функції для роботи з базою даних
from models import (
    get_all_listings,   # отримати всі лістинги
    add_listing,        # додати новий лістинг
    get_listing,        # отримати один лістинг за ID
    update_listing,     # оновити лістинг
    delete_listing      # видалити лістинг
)

#  Flask
app = Flask(__name__)

# Підключаємо конфігурацію (SECRET_KEY, налаштування БД)
app.config.from_object('config.Config')

app.register_blueprint(api)

# ГОЛОВНА
@app.route("/")
def index():
    # Отримуємо всі лістинги з бази даних
    listings = get_all_listings()

    # Передаємо список лістингів у HTML-шаблон
    return render_template("listings.html", listings=listings)


# ДОДАВАННЯ
@app.route("/listings/add", methods=["GET", "POST"])
def add_listing_route():

    # Якщо форма була відправлена
    if request.method == "POST":
        # Отримуємо дані з форми
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]

        # Додаємо новий запис у базу даних
        add_listing(title, description, price)

        # Повідомлення користувачу
        flash("Лістинг додано успішно!")
        # Переадресація на головну сторінку
        return redirect(url_for("index"))
    return render_template("add_listing.html")

# РЕДАГУВАННЯ ЛІСТИНГУ
@app.route("/listings/edit/<int:listing_id>", methods=["GET", "POST"])
def edit_listing_route(listing_id):

    # Отримуємо поточний лістинг за ID
    listing = get_listing(listing_id)

    # Якщо форма була відправлена
    if request.method == "POST":
        # Отримуємо оновлені дані з форми
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]

        # Оновлюємо запис у базі даних
        update_listing(listing_id, title, description, price)

        # Повідомлення про успішне оновлення
        flash("Лістинг оновлено!")

        # Повертаємося на головну сторінку
        return redirect(url_for("index"))

    # Якщо GET-запит — показуємо форму з поточними даними
    return render_template("edit_listing.html", listing=listing)


#  ВИДАЛЕННЯ
@app.route("/listings/delete/<int:listing_id>", methods=["POST"])
def delete_listing_route(listing_id):
    # Видаляємо лістинг з бази даних
    delete_listing(listing_id)
    # Повідомлення про успішне видалення
    flash("Лістинг видалено!")
    # Повертаємося на головну сторінку
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)


"""meg keys для GET POST ТАКОЖ МОЖНА ВИКОРИСТАТИ"""
"""дати можливість для фроненду щоб він мав можливість вносити зміни, надсилає дані, видаляє дані
має можливість робити запити на API, паралельно папку для Фронтенду HTLM CSS JVAskript
fetch функція, """
