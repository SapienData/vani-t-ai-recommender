from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Sample VANI-T products
products_db = [
    {"name": "Wonder Balm Melting Cleanser", "skin_type": ["dry","sensitive","all"], "category":"cleanser", "url":"https://nationalsalonsupplies.com.au/shop/beauty/skincare/cleansers/vani-t-wonder-balm-melting-cleanser-80gm/"},
    {"name": "Face Base Glazing Milk", "skin_type": ["dry","all"], "category":"serum", "url":"https://vani-t.com/products/face-base-glazing-milk"},
    {"name": "Mineral Powder Foundation", "skin_type": ["oily","all"], "category":"moisturizer", "url":"https://trade.vani-t.com/products/mineral-powder-foundation"},
    {"name": "Glow Filter HD Sheer Foundation", "skin_type": ["all"], "category":"serum", "url":"https://trade.vani-t.com/products/glow-filter-hd-sheer-foundation"},
    {"name": "Tan Eraser Mousse", "skin_type": ["all"], "category":"sunscreen", "url":"https://vani-t.com/products/tan-eraser-tan-removal-mousse-200ml-1"},
    {"name": "Glow+ Self Tan Drops", "skin_type": ["all"], "category":"sunscreen", "url":"https://www.ebay.com.au/itm/167642975524"}
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to VANI-T AI Recommender API "})

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    skin_type = data.get("skin_type", "").lower()
    category = data.get("category", "").lower()

    recs = [
        p for p in products_db
        if (skin_type in p["skin_type"] or "all" in p["skin_type"])
        and (p["category"] == category or category == "")
    ]

    if not recs:
        recs = products_db[:2]

    return jsonify(recs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)