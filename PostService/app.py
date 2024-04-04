from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (to be replaced with database)
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

# Endpoint to get all posts
@app.route('/post/all-posts', methods=['GET'])
def get_all_posts():
    return jsonify(posts)

# Endpoint to add a new post
@app.route('/post/add-post', methods=['POST'])
def add_post():
    data = request.get_json()
    # Generate a unique ID for the new post
    new_id = max(post['id'] for post in posts) + 1 if posts else 1
    data['id'] = new_id
    posts.append(data)
    return jsonify({"message": "Post added successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
