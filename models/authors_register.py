from ct import blog


class AuthorModel(blog.Model):
    __tablename__ = 'authors'

    id = blog.Column(blog.Integer, primary_key=True)
    author = blog.Column(blog.String(50))
    password = blog.Column(blog.String(50))

    def __init__(self, author, password):
        self.author = author
        self.password = password

    def save_to_blog(self):
        blog.session.add(self)
        blog.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(author=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
