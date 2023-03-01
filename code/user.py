from werkzeug.security import check_password_hash


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'
    
    def is_active(self):
        return True
    def find_by_username(username):
            # This is just an example implementation, you will need to replace this
            # with your own logic to retrieve a user from a database or some other storage
            # based on the given username.
            users = [
                User(1, 'john', 'password'),
                User(2, 'jane', 'password'),
                User(3, 'bob', 'password'),
            ]
            for user in users:
                if user.username == username:
                    return user
            return None
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id):
        users = User.get_all()
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def get_all():
        return [
            User(1, 'john', 'password'),
            User(2, 'jane', 'password'),
            User(3, 'bob', 'password')
        ]
        
