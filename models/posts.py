from ct import blog


class PostModel(blog.Model):
    __tablename__ = 'posts'

    id = blog.Column(blog.Integer, primary_key=True)
    post = blog.Column(blog.String(500))

    post_author_id = blog.Column(blog.Integer, blog.ForeignKey('authors.id'))
    comments = blog.relationship('CommentModel', lazy='dynamic')

    def __init__(self, author_id, post):
        self.post = post
        self.post_author_id = author_id

    def json(self):
        return {'post_id': self.id, 'post': self.post,
                'post_author_id': self.post_author_id,
                 'comments': [x.json() for x in self.comments.all()]}

    def save_to_blog(self):
        blog.session.add(self)
        blog.session.commit()
