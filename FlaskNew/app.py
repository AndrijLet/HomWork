from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 🔧 Конфігурація БД
db_config = {
    'host': "localhost",
    'port': '3306',   # перевір у OpenServer, може бути 3307
    'database': 'market',
    'user': 'root',
    'password': 'usbw'
}

# Універсальна функція для запитів
def query_db(query, args=(), one=False):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, args)
        rv = cursor.fetchall()
        connection.commit()
        return (rv[0] if rv else None) if one else rv
    finally:
        cursor.close()
        connection.close()

# --- Базові сторінки ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/seo")
def seo():
    return render_template("seo.html")

@app.route("/api-test")
def api_test():
    return render_template("api_test.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = {
            "name": request.form.get("name"),
            "age": request.form.get("age"),
            "email": request.form.get("email"),
            "subscribe": request.form.get("subscribe"),
            "topic": request.form.get("topic"),
            "message": request.form.get("message")
        }
        return render_template("form.html", submitted=True, data=data)
    return render_template("form.html", submitted=False)

# --- CRUD для listing_csv ---
@app.route("/listings")
def listings():
    data = query_db("SELECT * FROM listing_csv")
    return render_template("listings.html", data=data)

@app.route("/listings/add", methods=["GET", "POST"])
def add_listing():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        price = request.form.get("price")
        query_db("INSERT INTO listing_csv (title, description, price) VALUES (%s, %s, %s)",
                 (title, description, price))
        return redirect(url_for("listings"))
    return render_template("add_listing.html")

@app.route("/listings/edit/<int:id>", methods=["GET", "POST"])
def edit_listing(id):
    listing = query_db("SELECT * FROM listing_csv WHERE id = %s", (id,), one=True)
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        price = request.form.get("price")
        query_db("UPDATE listing_csv SET title=%s, description=%s, price=%s WHERE id=%s",
                 (title, description, price, id))
        return redirect(url_for("listings"))
    return render_template("edit_listing.html", listing=listing)

@app.route("/listings/delete/<int:id>", methods=["POST"])
def delete_listing(id):
    query_db("DELETE FROM listing_csv WHERE id = %s", (id,))
    return redirect(url_for("listings"))

# --- Інші таблиці ---
@app.route("/views")
def views():
    data = query_db("SELECT * FROM Views")
    return render_template("views.html", data=data)

@app.route("/favorites")
def favorites():
    data = query_db("SELECT * FROM Favorites")
    return render_template("favorites.html", data=data)

@app.route("/orders")
def orders():
    data = query_db("SELECT * FROM Orders")
    return render_template("orders.html", data=data)

@app.route("/revenue")
def revenue():
    data = query_db("SELECT * FROM Revenue")
    return render_template("revenue.html", data=data)

# --- API для тестування ---
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.route("/items", methods=["GET", "POST"])
def items_route():
    if request.method == "GET":
        return jsonify(items)
    elif request.method == "POST":
        new_item = request.json
        new_item["id"] = len(items) + 1
        items.append(new_item)
        return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=["PUT", "PATCH", "DELETE"])
def item_route(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    if request.method == "PUT":
        item.update(request.json)
        return jsonify(item)
    elif request.method == "PATCH":
        item.update(request.json)
        return jsonify(item)
    elif request.method == "DELETE":
        items.remove(item)
        return jsonify({"deleted": item_id})

if __name__ == "__main__":
    app.run(debug=True)