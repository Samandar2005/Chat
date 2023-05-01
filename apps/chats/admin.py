from django.contrib import admin
from apps.chats.models import Chat, Message

# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)