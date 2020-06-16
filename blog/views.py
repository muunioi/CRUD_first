from django.shortcuts import render, redirect, get_object_or_404 #장고에 내장된 기능
from .models import Post
from .forms import PostForm
# Create your views here.

def main(request):
    posts = Post.objects #Post.objects를(모델 Post의 모든것들을) posts 변수에 담기
    return render(request, 'posts.html', {'posts':posts}) 
    #3개의 인자, template에서 호출할 내용들을 context부분의 dictionary안에 밝혀주세요!

def create(request):
    if request.method == 'POST': #post방식
        form = PostForm(request.POST)
        if form.is_valid(): #유효성 검증을 통과한다면
            form.save() #저장하시오
            return redirect('main') #main화면으로 되돌아가기
    else:
        form = PostForm() #get방식
    
    return render(request, 'create.html', {'form':form})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('main') #main화면으로 되돌아가기
    else:
        form = PostForm(instance=post) #수정하기 창만 열었을 때
    
    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')