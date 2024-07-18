from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse


def jwt_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        jwt_authenticator = JWTAuthentication()
        try:
            auth_result = jwt_authenticator.authenticate(request)
            if auth_result is None:
                return JsonResponse({"error": "Invalid token"}, status=401)
            user, token = auth_result
            request.user = user
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=401)

        return view_func(request, *args, **kwargs)

    return _wrapped_view