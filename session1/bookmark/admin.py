from django.contrib import admin
from .models import Bookmark

# Register your models here.

class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title", "url")

admin.site.register(Bookmark, BookmarkAdmin)  #실제 사이트에서 북마크 모델을 표시하겠다!!
                                              #이렇게 등록을 하면 sqlbrowser 이용할 필요 없이 데이터가 잘 들어갔는지 확인 가능
