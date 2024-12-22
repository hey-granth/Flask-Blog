from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint("main", __name__)


# route for the home(main/index) page
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    # This will get the page number from the URL, if it does not exist it will default to 1

    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


# route for the about page
@main.route("/about")
def about():
    return render_template("about.html", title="About")
