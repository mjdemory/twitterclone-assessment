from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from notification.models import Notification

# Create your views here.

# def notification_view(request):
#     notifications = Notification.objects.filter(receiver=request.user)
#     notifications_count = 0
#     new_notifications = []
#     for notify in notifications:
#         if notify.notification_flag == False:
#             notifications_count += 1
#             new_notifications.append(notify.msg_content)
#         notify.notification_flag = True
#         notify.save()
#     return render(request, 'notification.html', {'new_notifications': new_notifications, "notifications_count": notifications_count})

class notification_view(LoginRequiredMixin,TemplateView):
    def get(self, request):
        notifications = Notification.objects.filter(receiver=request.user)
        notifications_count = 0
        new_notifications = []
        for notify in notifications:
            if notify.notification_flag == False:
                notifications_count += 1
                new_notifications.append(notify.msg_content)
            notify.notification_flag = True
            notify.save()
        return render(request, 'notification.html', {'new_notifications': new_notifications, "notifications_count": notifications_count})