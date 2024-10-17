from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint 1: Welcome message
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my API!"

# Endpoint 2: Get all items
@app.route('/items', methods=['GET'])
def get_items():
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return jsonify(items)

# Endpoint 3: Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ("Item not found", 404)

# Endpoint 4: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    return jsonify(new_item), 201

# Endpoint 5: Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    return jsonify(updated_item)

# Error handler for 404 - route not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
