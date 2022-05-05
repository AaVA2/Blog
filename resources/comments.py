from flask_restful import Resource, reqparse
from models.comments import CommentModel
from models.authors_register import AuthorModel
from flask_jwt import jwt_required


class Comment(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author_id', type=int, required=True)
    parser.add_argument('post_id', type=int, required=True)
    parser.add_argument('comment', type=str, required=True)

    def post(self):
        data = Comment.parser.parse_args()

        if AuthorModel.find_by_id(data['author_id']):
            comment = CommentModel(**data)
            comment.save_to_blog()
            return {"message": "Commented successfully."}
        else:
            return {'message': "Comment Author doesn't exist."}, 404
