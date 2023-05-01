from django.db import models
from apps.account.models import Account

class Chat(models.Model):
    user_one = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_one_chats')
    user_two = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_two_chats')
    
    class Meta:
        unique_together = ['user_one', 'user_two']

    def __str__(self):
        return f"{self.user_one.email} - {self.user_two.email}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email} - {self.chat.user_one.email} - {self.chat.user_two.email}"
