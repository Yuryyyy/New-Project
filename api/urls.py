from django.urls import path, include
from .views import CustomRouterView, PutUserHandler, DeleteUserHandler

urlpatterns = [
    path('<str:route>/', CustomRouterView.as_view(), name='custom_router'),
    path('user/<int:pk>/', PutUserHandler.as_view(), name='user_update'),
    path('user/<int:pk>/delete/', DeleteUserHandler.as_view(), name='user_delete'),
]
