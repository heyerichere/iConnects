
from flask import render_template, flash, jsonify, request, redirect, url_for
from app import db
from app.posts import posts
from app.posts.forms import PostForm
from app.models import Post
from datetime import datetime

@posts.route('/', methods=['GET', 'POST'])
def post_page():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash("Post created!", "SUCCESS!")
        return redirect(url_for('posts.post_page'))

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('posts/templates/post.html', form=form, posts=posts)

@posts.route('/create_ajax', methods=['POST'])
def create_post_ajax():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400
    
    post = Post(title=title, content=content, timestamp=datetime.utcnow())
    db.session.add(post)
    db.session.commit()

    return jsonify({
        "message": "Post created successfully!",
        "post": {
            "title": post.title,
            "content": post.content,
            "timestamp": post.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
    })

@posts.route('/notifications')
def notifications():
    return render_template('posts/notification.html')
