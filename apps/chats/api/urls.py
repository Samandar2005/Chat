from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.chats.api.v1.urls'))
]