from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint("posts", __name__)


# Creating a new post
@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Your Post has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template("create_post.html", title="New Post", form=form)


# Viewing a post
@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    # get_or_404 will return the post with the given id, if it does not exist it will return a 404.

    return render_template("post.html", title=post.title, post=post)


# Updating a post
@posts.route("/post/<int:post_id>/update")
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
        # Error 403 is a forbidden route, which means that the server understood the request, but the user is not allowed to access the route.

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        # we don't need to db.session.add(post) because the post is already in the database, we're just updating it

        flash("Your Post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        "create_post.html", title="Update Post", form=form, legend="Update Post"
    )


# Deleting a post
@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash("Your Post has been deleted!", "success")
    return redirect(url_for("main.home"))
