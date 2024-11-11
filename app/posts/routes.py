from flask import render_template, url_for, redirect, flash, request
from . import posts
from app import db
from app.posts.models import Post
from flask_login import current_user, login_required
from datetime import datetime
import os
from werkzeug.utils import secure_filename

@posts.route('/posts', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        # Parse form data directly from request.form
        title = request.form.get('title')
        content = request.form.get('content')
        event_name = request.form.get('event_name')
        event_description = request.form.get('event_description')
        
        # Parse event_date as a date object
        event_date_str = request.form.get('event_date')
        event_date = datetime.strptime(event_date_str, "%Y-%m-%d").date() if event_date_str else None
        
        # Create a new Post instance with data from the form
        post = Post(
            title=title,
            content=content,
            timestamp=datetime.utcnow(),
            user_id=current_user.get_id(),
            event_name=event_name,
            event_date=event_date,
            event_description=event_description
        )

        # # Handle image file upload if provided
        # image = request.files.get('image')
        # if image and image.filename != '':
        #     image_filename = secure_filename(image.filename)
        #     image_path = os.path.join('static/images', image_filename)
        #     image.save(image_path)
        #     post.image_path = image_path

        # # Handle video file upload if provided
        # video = request.files.get('video')
        # if video and video.filename != '':
        #     video_filename = secure_filename(video.filename)
        #     video_path = os.path.join('static/videos', video_filename)
        #     video.save(video_path)
        #     post.video_path = video_path

        # Save post to the database
        db.session.add(post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for('posts.create_post'))

    # Fetch and display existing posts, ordered by timestamp
    all_posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('post.html', posts=all_posts)