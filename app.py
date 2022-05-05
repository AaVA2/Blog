from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.posts import Post
from resources.comments import Comment
from resources.authors_register import AuthorRegister
from ct import blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'aava'
api = Api(app)

blog.init_app(app=app)


@app.before_first_request
def create_tables():
    blog.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Post, "/posts")
api.add_resource(AuthorRegister, "/author")
api.add_resource(Comment, '/comments')
app.run(port=6000, debug=True)
