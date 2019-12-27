from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Photo(models.Model):


    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='user_photo')
    # on_delete=models.CASCAD -> 삭제가되면 하위객체도 같이 삭제
    photo = models.ImageField(upload_to="photo/%Y%m%d", default='photos/no_image.png')
    text = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)  # 글 작성 일을 저장하기 위한 날짜시간 필드, auto_now_add 옵션을 설정하면 객체가 추가될 때 자동으로 값을 설정
    updated = models.DateTimeField(auto_now=True)    # 글 수정일을 저장하기 위한 날자시간 필드 auto_now 옵션을 설정하면 객체가 수정될 때마다 자동으로 값을 설정합니다.

    class Mata:
        ordering = ['-updated'] # 업데이트 된 시간의 내림차순으로 정렬


    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d%H:%M%S") # 관리자 페이지의 제목에 보여줄 것 설정

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])