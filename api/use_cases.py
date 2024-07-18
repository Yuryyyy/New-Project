from django.http import JsonResponse
from .models import User
from .services import UserService

class GetUser:
    def handle(self, request):
        users = UserService.get_all_users()
        return JsonResponse(users, safe=False)

class PostUser:
    def handle(self, request):
        data = request.POST
        UserService.create_user(data)
        return JsonResponse({"message": "User created"}, status=201)

class PutUser:
    def handle(self, request):
        data = request.POST
        UserService.update_user(data)
        return JsonResponse({"message": "User updated"}, status=200)

class DeleteUser:
    def handle(self, request):
        user_id = request.path.split('/')[-2]
        if not user_id:
            return JsonResponse({"error": "User ID is required"}, status=400)

        success = UserService.delete_user(user_id)
        if success:
            return JsonResponse({"message": "User deleted"}, status=204)
        else:
            return JsonResponse({"error": "User not found"}, status=404)
