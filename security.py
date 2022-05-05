from models.authors_register import AuthorModel
from hmac import compare_digest


def authenticate(username, password):
    author = AuthorModel.find_by_username(username)
    if author and compare_digest(author.password, password):
        return author


def identity(payload):
    author_id = payload['identity']
    return AuthorModel.find_by_id(author_id)
