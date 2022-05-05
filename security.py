from models.authors_register import AuthorModel
from hmac import compare_digest


def authenticate(username, password):
    user = AuthorModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    author_id = payload['identity']
    return AuthorModel.find_by_id(author_id)
