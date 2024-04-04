from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (to be replaced with database)
users = [
    {"id": 1, "name": "John Doe", "age": 30},
    {"id": 2, "name": "Jane Smith", "age": 25}
]

# Endpoint to get all users
@app.route('/user/all-users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# Endpoint to add a new user
@app.route('/user/add-user', methods=['POST'])
def add_user():
    data = request.get_json()
    # Generate a unique ID for the new user
    new_id = max(user['id'] for user in users) + 1 if users else 1
    data['id'] = new_id
    users.append(data)
    return jsonify({"message": "User added successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
