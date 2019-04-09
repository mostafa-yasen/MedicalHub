from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from profiles.models import Doctor, Patient
from communities.models import Community


class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120, null=True, blank=True, default="No Title")
    content = models.TextField()
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    likes = models.IntegerField(default=0, null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.pk, self.title)


class Comment(models.Model):
    content = models.CharField(max_length=300, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Question(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    asked_to = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    answered = models.BooleanField(default=False, null=False)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return "%s - %s" % (self.creator.__str__(), self.asked_to.__str__())


class Answer(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content    


class Reply_on_Answer(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Reply_on_Comment(models.Model):
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time = models.TimeField(default=datetime.now, null=False, blank=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.content