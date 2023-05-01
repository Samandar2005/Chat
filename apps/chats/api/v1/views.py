from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.chats.models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def get_queryset(self):
        user = self.request.user
        chats = Chat.objects.filter(user_one=user) | Chat.objects.filter(user_two=user)
        return chats


class ChatCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(user_one=self.request.user)


class ChatDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        user = self.request.user
        if chat.user_one != user and chat.user_two != user:
            return Message.objects.none()
        messages = Message.objects.filter(chat=chat)
        return messages


class MessageCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        serializer.save(sender=self.request.user, chat=chat)

