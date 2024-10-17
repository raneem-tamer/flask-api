from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Endpoint 1: Welcome message
@app.route('/', methods=['GET'])
def home():
    """
    Welcome message
    ---
    responses:
      200:
        description: A welcome message
    """
    return "Welcome to my API!"

# Endpoint 2: Get all items
@app.route('/items', methods=['GET'])
def get_items():
    """
    Get all items
    ---
    responses:
      200:
        description: A list of items
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
    """
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return jsonify(items)

# Endpoint 3: Get a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Get a specific item by ID
    ---
    parameters:
      - name: item_id
        in: path
        type: integer
        required: true
        description: The ID of the item to retrieve
    responses:
      200:
        description: A specific item
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
      404:
        description: Item not found
    """
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    item = next((item for item in items if item['id'] == item_id), None)
    return jsonify(item) if item else ("Item not found", 404)

# Endpoint 4: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    """
    Create a new item
    ---
    parameters:
      - name: item
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The name of the item
              example: New Item
    responses:
      201:
        description: The created item
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
    """
    new_item = request.json
    return jsonify(new_item), 201

# Endpoint 5: Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Update an item
    ---
    parameters:
      - name: item_id
        in: path
        type: integer
        required: true
        description: The ID of the item to update
      - name: item
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: The updated name of the item
    responses:
      200:
        description: The updated item
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
    """
    updated_item = request.json
    return jsonify(updated_item)

# Error handler for 404 - route not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
