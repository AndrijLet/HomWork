from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/seo")
def seo():
    return render_template("seo.html")

'''додаю новий маршрут'''

@app.route("/form", methods=["GET", "POST"]) #маршрут приймає GET (показує) POST (обробляє)
def form():
    if request.method == "POST":
        name = request.form.get("name") #Отримання даних з HTML-форми
        age = request.form.get("age")
        email = request.form.get("email")
        subscribe = request.form.get("subscribe")
        topic = request.form.get("topic")
        message = request.form.get("message")
        return render_template("form.html", submitted=True, data={ #Передача даних назад у HTML
            "name": name,
            "age": age,
            "email": email,
            "subscribe": subscribe,
            "topic": topic,
            "message": message

        })
    return render_template("form.html", submitted=False) #

if __name__ == "__main__":
    app.run(debug=True)