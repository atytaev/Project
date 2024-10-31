from flask import Flask, render_template, request, redirect, url_for
import db
app = Flask(__name__, template_folder='templates')

def validate_name(val):
    return isinstance(val, str) and len(val) > 0

def validate_prep_time(val):
    return isinstance(val, int) and val > 0 and val < 999

def post_data_to_dict(post_data):
    return {
        key: post_data[index]
        for index, key in enumerate(('id',) + tuple(REQUIRED_DIELDS))
    }

def comments_data_to_dict(comments):
    return [{
        key: comment_data[index]
        for index, key in enumerate(('id', 'post_id', 'author', 'content', 'created_at'))
    } for comment_data in comments]

REQUIRED_DIELDS = {
    'title': validate_name,
    'content': validate_name,
    'author': validate_name,
}

ORDERING_QUERY_KEY = 'ordering'
@app.route('/')
def redirect_to_posts():
    return redirect(url_for('posts'))

@app.route('/api/posts', methods = ['GET', 'POST'])
def posts():
    if request.method == 'GET':
        ordering = 'id'
        if ORDERING_QUERY_KEY in request.args:
            ordering = request.args[ORDERING_QUERY_KEY]
        return sorted(
            [
                post_data_to_dict(post)
                for post in db.all_post()
            ],
            key=lambda x:x[ordering],
            reverse=ordering.startswith('-')
        )

    elif request.method == 'POST':
        for key in REQUIRED_DIELDS:
            if key not in request.json:
                return {'error': f'{key} is required'}, 400
            elif not REQUIRED_DIELDS[key](request.json[key]):
                return {'error': f'{key} is invalid'}, 400

        db.add_post(**request.json)
        return {'message': 'Post added successfully'}, 201

@app.route('/api/posts/<int:post_id>/', methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
def post(post_id):
    post_data = db.get_post_by_id(post_id)
    if not post_data:
        return {'error': 'Post not found'}, 404
    if request.method == "GET":
        post_dict = post_data_to_dict(post_data)
        post_dict['comment'] = (
            comments_data_to_dict(db.get_post_comments(post_id))
        )
        return post_dict

    elif request.method == 'PUT':
        for key in REQUIRED_DIELDS:
            if key not in request.json:
                return {'error': f'{key} is required'}, 400
            elif not REQUIRED_DIELDS[key](request.json[key]):
                return {'error': f'{key} is invalid'}, 400

        db.update_post(post_id, **request.json)
        return {'message': 'Recipe update successfully'}, 200

    elif request.method == 'PATCH':
        for key in request.json:
            if key not in REQUIRED_DIELDS:
                return {'error': f'{key} is not allowed'},400
            elif not REQUIRED_DIELDS[key](request.json[key]):
                return {'error': f'{key} is invalid'},400

        post_dict = post_data_to_dict(post_data)
        post_dict.update(request.json)
        db.update_post(**post_dict)
        return {'message': 'Recipe update successfully'}, 200
    elif request.method == 'DELETE':
        db.delete_post(post_id)
        return {'message': 'Post deleted successfully'}, 204


@app.route('/', methods = ['POST'])
def index():

    return render_template(
        'index.html',
        posts = db.all_post()
    )

if __name__ == '__main__':
    app.run(debug=True)
    # from db import all_post, viewing_article1, viewing_article
    # breakpoint()