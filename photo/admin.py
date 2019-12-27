from django.contrib import admin
from .models import Photo
# 관리자 페이지 커스텀 마이징

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated'] # 목록에 보일 필드를 설정
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    search_fields = ['text', 'created']  # 왜래키는 검색 설정을 할 수 없다
    ordering = ['-updated', '-created']  # 모델의 기본 정렬값이 아닌 관리자 사이트에서 기본으로 사용할 정렬값을 설정


admin.site.register(Photo, PhotoAdmin)