from django.http import JsonResponse
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication

from .custom_router import ROUTES
from .models import User
from .decorators import jwt_required
import json

class CustomRouterView(View):
    def dispatch(self, request, *args, **kwargs):
        response = self._check_jwt_token(request)
        if response:
            return response
        return super().dispatch(request, *args, **kwargs)

    def _check_jwt_token(self, request):
        jwt_authenticator = JWTAuthentication()
        try:
            auth_result = jwt_authenticator.authenticate(request)
            if auth_result is None:
                return JsonResponse({"error": "Invalid token"}, status=401)
            user, token = auth_result
            request.user = user
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=401)

    def _handle_request(self, request, *args, **kwargs):
        method = request.method
        route = kwargs.get('route')
        handler_class = ROUTES.get(method, {}).get(route)

        if not handler_class:
            return JsonResponse({"error": "Route not found"}, status=404)

        handler = handler_class()
        if hasattr(handler, 'handle'):
            return handler.handle(request)
        return JsonResponse({"error": "Handler does not have a handle method"}, status=500)

    def get(self, request, *args, **kwargs):
        return self._handle_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self._handle_request(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self._handle_request(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self._handle_request(request, *args, **kwargs)

class PutUserHandler(View):
    def put(self, request, pk):
        # Check JWT token here if needed
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')

            if not username or not email:
                return JsonResponse({"error": "Username and email are required"}, status=400)

            user = User.objects.get(id=pk)
            user.username = username
            user.email = email
            user.save()
            return JsonResponse({"message": "User updated successfully"}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)


class DeleteUserHandler(View):
    def dispatch(self, request, *args, **kwargs):
        response = self._check_jwt_token(request)
        if response:
            return response
        return super().dispatch(request, *args, **kwargs)

    def _check_jwt_token(self, request):
        jwt_authenticator = JWTAuthentication()
        try:
            auth_result = jwt_authenticator.authenticate(request)
            if auth_result is None:
                return JsonResponse({"error": "Invalid token"}, status=401)
            user, token = auth_result
            request.user = user
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=401)

    def delete(self, request, pk):
        try:

            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse({"message": "User deleted successfully"}, status=204)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)