from flask import Flask
from flask_restful import Api

from Resources.posts import Blog
from ct import blog

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    blog.create_all()


api.add_resource(Blog, "/posts")


app.run(port=6000, debug=True)
