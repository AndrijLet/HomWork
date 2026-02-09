from flask import Blueprint, jsonify, request

from models import (
    get_all_listings,
    get_listing,
    add_listing,
    update_listing,
    delete_listing,
)

api = Blueprint('api', __name__, url_prefix='/api') #url_prefix="/api" → всі маршрути автоматично та префікс/api
#/listings для всіх ДІЙ вказаний один шлях

@api.route("/listings", methods=["GET"]) #GET всі лістинги
def api_get_listings():
    listings = get_all_listings()
    return jsonify(listings)

@api.route("/listings/<int:listing_id>", methods=["GET"]) #GET один лістинг
def api_get_listing(listing_id):
    listing = get_listing(listing_id)

    if not listing:
        return jsonify({"error": "listing not found"}), 404
    return jsonify(listing)

@api.route("/listings", methods=["POST"]) #додавання товарів
def api_add_listing():
    data = request.get_json()

    title = data.get("title") # АРІ товару
    description = data.get("description") #додано через AP
    price = data.get("price")

    if not title or not price:
        return jsonify({"error": "title or price is required"}), 400

    listing_id = add_listing(title, description, price)

    return jsonify({
        "message": "Listing created",
        "id": listing_id
    }), 201

@api.route("/listings/<int:listing_id>", methods=["PUT"]) #ОНОВЛЕННЯ
def api_update_listing(listing_id):
    data = request.get_json()

    title = data.get("title")
    description = data.get("description")
    price = data.get("price")

    if not title or not price:
        return jsonify({"error": "Title and price are required"}), 400

    update_listing(listing_id, title, description, price)

    return jsonify({"message": "Listing updated"})

@api.route("/listings/<int:listing_id>", methods=["DELETE"]) #DELETED
def api_delete_listing(listing_id):
    delete_listing(listing_id)
    return jsonify({"message": "Listing deleted"})



