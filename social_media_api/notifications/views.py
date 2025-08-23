from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification

class NotificationListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated)

    def get(self, request, *args, **kwargs):
            notifications = Notification.objects.filter(recipient=request.user).order_by("-timestamp")
            data = [
            {
                "id": n.id,
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target),
                "timestamp": n.timestamp,
                "is_read": n.is_read,
            }
         for n in notifications
        ]
            return Response(data)

