from django.contrib import admin
from home.models import Post, LikeRelation, CommentsModel

admin.site.register(Post)
admin.site.register(LikeRelation)
admin.site.register(CommentsModel)