from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body'] #[사용자에게 입력받을 필드]
# model post의 fields 중에서 사용자가 직접 데이터를 입력,전송하는 fields를 밝혀줌
# 시간은 auto로 등록했기 때문에 따로 필드로 만들어 줄 필요가 없음