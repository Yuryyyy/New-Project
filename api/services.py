from .models import User

class UserService:
    @staticmethod
    def get_all_users():
        return list(User.objects.all().values())

    @staticmethod
    def create_user(data):
        User.objects.create(username=data.get('username'), email=data.get('email'))

    @staticmethod
    def update_user(data):
        user = User.objects.get(id=data.get('id'))
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.save()

    @staticmethod
    def delete_user(user_id):
        user = User.objects.get(id=user_id)
        user.delete()
