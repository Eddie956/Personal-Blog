from flask_login import UserMixin, current_user, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from datetime import datetime
from . import db, admin
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """ 
    class modelling the users by handling the login
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, index=True)
    email = db.Column(db.String, unique=True, index=True)

    posts = db.relationship('Post', backref='user', lazy='dynamic')
    is_admin = db.Column(db.Boolean)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    password_hash = db.Column(db.String)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User{self.username}'


class Post(UserMixin, db.Model):
    """ 
    class modelling the posts
    """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    post = db.Column(db.String)
    image_name = db.Column(db.String)
    image_url = db.Column(db.String)
    timeposted = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return f'Post{self.post}'


class Role(UserMixin, db.Model):
    """ 
    class modelling the role of each user
    """

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Post{self.name}'


class Comment(UserMixin, db.Model):
    """ 
    User comment model for each post
    """

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    commenter = db.Column(db.String)

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return f'Post{self.comment}'


class Subscribers(UserMixin, db.Model):

    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'Subscribers{self.email}'


class MyModelView(ModelView):
    def is_accessible(self):
        return False


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Subscribers, db.session))
