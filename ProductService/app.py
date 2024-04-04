from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (to be replaced with database)
products = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 20.49}
]

# Endpoint to get all products
@app.route('/product/all-products', methods=['GET'])
def get_all_products():
    return jsonify(products)

# Endpoint to add a new product
@app.route('/product/add-product', methods=['POST'])
def add_product():
    data = request.get_json()
    # Generate a unique ID for the new product
    new_id = max(product['id'] for product in products) + 1 if products else 1
    data['id'] = new_id
    products.append(data)
    return jsonify({"message": "Product added successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
