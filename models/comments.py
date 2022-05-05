from ct import blog


class CommentModel(blog.Model):
    __tablename__ = 'comments'

    id = blog.Column(blog.Integer, primary_key=True)
    comment = blog.Column(blog.String(500))

    ca = blog.relationship('AuthorModel')
    comment_author_id = blog.Column(blog.Integer, blog.ForeignKey('authors.id'))
    post_id = blog.Column(blog.Integer, blog.ForeignKey('posts.id'))

    def __init__(self, author_id, post_id, comment):
        self.comment_author_id = author_id
        self.post_id = post_id
        self.comment = comment

    def json(self):
        return {'comment_id': self.id, 'comment': self.comment,
                'comment_author': self.ca.author}

    def save_to_blog(self):
        blog.session.add(self)
        blog.session.commit()
