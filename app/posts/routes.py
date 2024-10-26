from flask import render_template
from . import posts

@posts.route('/<int:post_id>')
def post(post_id):
    return render_template('posts/post.html', post_id=post_id)

@posts.route('/<int:post_id>')
def post(post_id): 
    return render_template('posts/post.html', post_id=post_id)

@posts.route('/notifications')
def notifications():
    return render_template('posts/notification.html')