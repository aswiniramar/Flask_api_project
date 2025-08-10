from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.get_json()
    new_user["id"] = users[-1]["id"] + 1 if users else 1
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    for user in users:
        if user["id"] == user_id:
            data = request.get_json()
            user.update(data)
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# DELETE - Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)