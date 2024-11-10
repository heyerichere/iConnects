from flask import render_template, url_for, redirect, flash, request
from . import posts
from app import db
from app.posts.forms import PostForm
from app.posts.models import Post
from flask_login import current_user
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from flask_login import login_required

@posts.route('/posts', methods=['GET', 'POST'])
@login_required 
def create_post():
    form = PostForm()

    if request.method == 'POST' and form.validate_on_submit():
        form.title = request.form.get('title')
        form.content = request.form.get('content')
        form.event_name = request.form.get('event_name')
        form.event_date = request.form.get('event_date')
        form.event_description = request.form.get('event_description')
        
        post = Post(
            title=form.title,
            content=form.content,
            timestamp=datetime.utcnow(),
            user_id=current_user.id,
            event_name=form.vent_name,
            event_date=form.event_date,
            event_description=form.event_description
        )

        if 'image' in request.files:
            form.image = request.files['image']
            if form.image.filename != '':
                image_filename = secure_filename(form.image.filename)
                image_path = os.path.join('static/uploads/images', image_filename)
                form.image.save(image_path)
                post.image_path = image_path

        if 'video' in request.files:
            form.video = request.files['video']
            if form.video.filename != '':
                video_filename = secure_filename(form.video.filename)
                video_path = os.path.join('static/uploads/videos', video_filename)
                form.video.save(video_path)
                post.video_path = video_path

        # Save post to the database
        db.session.add(post)
        db.session.commit()
        flash("Post created successfully!", "success")
        return redirect(url_for('posts.create_post'))

    # Fetch and display existing posts, ordered by timestamp
    all_posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template('post.html', form=form, posts=all_posts)