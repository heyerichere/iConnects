from flask import render_template, url_for, redirect
from . import posts

@posts.route('/posts')
# @login_required
def show_posts():
    return render_template('post.html')


# from flask import render_template, flash, jsonify, request, redirect, url_for
# from flask_login import current_user, login_required
# from app import db
# from app.posts import posts
# from app.posts.forms import PostForm
# from app.auth.models import Alum  
# from app.posts.models import Post 
# from datetime import datetime

# @posts.route('/', methods=['GET', 'POST'])
# # @login_required  # Ensure the user is logged in to create a post
# def post_page():
#     form = PostForm()
#     if form.validate_on_submit():
#         post = Post(
#             title=form.title.data,
#             content=form.content.data,
#             timestamp=datetime.utcnow(),
#             user_id=current_user.alum_id  # Set user_id to the logged-in user's ID
#         )
#         db.session.add(post)
#         db.session.commit()
#         flash("Post created!", "success")
#         return redirect(url_for('posts.post_page'))

#     # Query all posts ordered by timestamp
#     posts = Post.query.order_by(Post.timestamp.desc()).all()
#     return render_template('posts/post.html', form=form, posts=posts)

# @posts.route('/create_ajax', methods=['POST'])
# # @login_required  # Ensure the user is logged in to create a post via AJAX
# def create_post_ajax():
#     data = request.get_json()
#     title = data.get('title')
#     content = data.get('content')
    
#     if not title or not content:
#         return jsonify({"error": "Title and content are required"}), 400
    
#     # Create a new post with the logged-in user's ID
#     post = Post(
#         title=title,
#         content=content,
#         timestamp=datetime.utcnow(),
#         user_id=current_user.alum_id  # Set user_id to the logged-in user's ID
#     )
#     db.session.add(post)
#     db.session.commit()

#     return jsonify({
#         "message": "Post created successfully!",
#         "post": {
#             "title": post.title,
#             "content": post.content,
#             "timestamp": post.timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         }
#     })

# @posts.route('/notifications')
# # @login_required
# def notifications():
#     return render_template('posts/notification.html')