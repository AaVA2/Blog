from flask_restful import Resource, reqparse
from models.posts import PostModel
from models.authors_register import AuthorModel
from flask_jwt import jwt_required


class Post(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author_id', type=int, required=True)
    parser.add_argument('post', type=str, required=True)


    def get(self):
        return {'posts': list(map(lambda x: x.json(), PostModel.query.all()))}


    def post(self):
        data = Post.parser.parse_args()

        if AuthorModel.find_by_id(data['author_id']):
            post = PostModel(**data)
            post.save_to_blog()
            return {'message': "Post successfully created."}
        else:
            return {'message': "Post Author doesn't exist."}, 404
