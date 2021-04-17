from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


USER_RELATIONSHIP_CHOICES = (
    (0, 'Friends'),
    (1, 'Unfriended by One'),
    (2, 'unfriended by Two'),
)

FRIEND_REQUEST_STATUS_CHOICES = (
    (0, 'Pending'),
    (1, 'Accepted'),
    (2, 'Rejected')
)


class UserRelationship(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends_with')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_of')
    relationship = models.PositiveIntegerField(choices=USER_RELATIONSHIP_CHOICES)
    created_on = models.DateTimeField("creation time", default=timezone.now)
    modified_on = models.DateTimeField("modified time", default=timezone.now)


class FriendRequests(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    request_status = models.PositiveIntegerField(choices=FRIEND_REQUEST_STATUS_CHOICES)
    created_on = models.DateTimeField("creation time", default=timezone.now)
    modified_on = models.DateTimeField("modified time", default=timezone.now)


class BlockedUsers(models.Model):
    blocked_by_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocker')
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked')
    created_on = models.DateTimeField("creation time", default=timezone.now)

