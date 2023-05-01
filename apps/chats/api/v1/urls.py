from django.urls import path
from .views import ChatList, ChatCreate, ChatDetail, MessageList, MessageCreate

urlpatterns = [
    path('chats/', ChatList.as_view(), name='chat-list'),
    path('chats/create/', ChatCreate.as_view(), name='chat-create'),
    path('chats/<int:pk>/', ChatDetail.as_view(), name='chat-detail'),
    path('chats/<int:chat_id>/messages/', MessageList.as_view(), name='message-list'),
    path('chats/<int:chat_id>/messages/create/', MessageCreate.as_view(), name='message-create'),
]