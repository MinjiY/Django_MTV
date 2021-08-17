# 우리가 만든 models.py를 admin페이지에서 볼 수 있도록 등록
from django.contrib import admin
from .models import Post, Comment
# Register your models here.

#admin page 출력되는 내용을 변경(커스터마이징)할 것
# admin page에 보여지는 내용을 변경하고 싶을때 admin.ModelAdmin을 상속받음
class PostAdmin(admin.ModelAdmin):
    # model admin에 이미 들어있는 변수
    list_display = ['id', 'title', 'count_text']
    # id와 title이 둘다 보여지게 하겠다 어떤 필드에 링크를 걸어주겠다 (title/id)
    list_display_links = ['title']

    # 텍스트 필드가 몇 글자인지 반환, 
    def count_text(self, obj):       # obj에 해당 Post객체가 반환됨
        return '{}글자'.format(len(obj.text))
    count_text.short_description = '글내용 글자수'

admin.site.register(Post, PostAdmin)
#admin.site.register(Post)
admin.site.register(Comment)
