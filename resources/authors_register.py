from flask_restful import Resource, reqparse
from models.authors_register import AuthorModel


class AuthorRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str, required=True, help="Author name required.")

    def post(self):
        data = AuthorRegister.parser.parse_args()
        user = AuthorModel(**data)
        user.save_to_blog()
        return {'message': 'author successfully created.'}


