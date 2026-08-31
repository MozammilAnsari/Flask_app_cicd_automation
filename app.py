from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "secretkey"

# Sample product data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "description": "A lightweight laptop with fast performance, long battery life, and a sharp display for work and entertainment.",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "name": "Phone",
        "price": 20000,
        "description": "A modern smartphone with a vibrant display, powerful camera, and smooth performance for daily use.",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000,
        "description": "Wireless headphones with immersive sound quality, deep bass, and a comfortable over-ear design.",
        "image": "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=600&q=80"
    },
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:id>')
def product(id):
    product = next((p for p in products if p["id"] == id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:id>')
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for item_id in session["cart"]:
            product = next((p for p in products if p["id"] == item_id), None)
            if product:
                cart_items.append(product)
                total += product["price"]

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        session.pop("cart", None)
        return "Order Placed Successfully!"

    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)