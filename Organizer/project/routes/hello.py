from flask import Blueprint

hello = Blueprint("hello", __name__)


@hello.route("/")
def index():
    """Renders a sample page."""
    return "Hello, World!"
