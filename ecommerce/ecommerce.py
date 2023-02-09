from flask import Flask

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def home():
    return "Welcome to our e-commerce site!"


products = [
    {"id": 1, "name": "T-Shirt", "price": 19.99},
    {"id": 2, "name": "Sweater", "price": 29.99},
    {"id": 3, "name": "Hoodie", "price": 39.99},
]

@app.route("/products")
def products_list():
    return str(products)
@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = [p for p in products if p["id"] == product_id][0]
    return str(product)
@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    product = [p for p in products if p["id"] == product_id][0]
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product)
    return f"Product '{product['name']}' added to cart."


@app.route("/checkout")
def checkout():
    purchase = session.get("cart", [])
    session["cart"] = []
    return "Purchase complete! Thank you for your order.\n\n" + str(purchase)


@app.route("/cart")
def view_cart():
    return str(session.get("cart", []))



if __name__ == "__main__":
    app.run()
