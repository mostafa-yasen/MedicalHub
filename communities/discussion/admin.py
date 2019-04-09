from django.contrib import admin
from .models import Post, Question
from .models import Answer, Comment
from .models import Reply_on_Answer, Reply_on_Comment


admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(Question)

admin.site.register(Answer)

admin.site.register(Reply_on_Answer)

admin.site.register(Reply_on_Comment)