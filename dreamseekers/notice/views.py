from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render

from datetime import timedelta

from user.models import Users
from .models import Image, Notice
from .forms import NoticeForm

# 게시글 목록
def index(request):
    # 모든 Notice를 불러오고 페이지에 가져옴
    list = Notice.objects.order_by('-created_at')
    page = request.GET.get('page') # 페이지

    # 출력하는 Notice수 제한
    paginator = Paginator(list,10)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: # 페이지가 지정되지 않았을때
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage: # 페이지 범위를 초과할때
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page) -5)
    if leftIndex <1:
        leftIndex = 1
    rightIndex = (int(page) +5)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    return render(request, 'notice_index.html',{'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range})

# 게시글 자세히 보기
def detail(request, pk):
    # 게시글에서 pk(primary_key)로 해당 게시글 검색
    post = Notice.objects.get(pk=pk)

    # 시간 차이 측정
    time_difference = post.updated_at - post.created_at
    show_updated_at = time_difference > timedelta(seconds=1)

    return render(request, 'notice_detail.html',{'post':post,'show_updated_at':show_updated_at,})

# 게시글 작성
def write(request):
    # 로그인 여부 확인
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    elif request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            user = Users.objects.get(pk = user_id)

            new_post = Notice.objects.create(
                title     = form.cleaned_data['title'],
                contents  = form.cleaned_data['contents'],
                author    = user
            )
            # 여러 개의 이미지를 처리합니다.
            for f in request.FILES.getlist('photo'):
                    image = Image.objects.create(image=f)
                    new_post.photo.add(image)
            new_post.save()

            return redirect('notice:detail',pk=new_post.pk)
        else:
            # 폼이 유효하지 않을 경우, 사용자가 입력한 데이터를 폼에 다시 채워 넣습니다.
            form = NoticeForm(request.POST)
    else:
        form = NoticeForm()
        
    return render(request, 'notice_write.html', {'form':form})

# 게시글 수정
def update(request,pk):
    # 로그인 여부 확인
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = Notice.objects.get(pk=pk)

    # 작성자가 아닌 경우 접근 불가
    if request.user != post.author:
        return redirect('notice:detail', pk=pk)
    
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=post)
        if form.is_valid():
            # 이미지 용량 제한
            total_image_size = 0
            for image in request.FILES.getlist('photo'):
                total_image_size += image.size
                print("이미지 용량")
                print(total_image_size)
            
            # MB 단위로 변환
            total_image_size_mb = total_image_size / 1048576

            if total_image_size_mb > settings.MAX_IMAGE_SIZE:
                return HttpResponseBadRequest('총 이미지 용량이 너무 큽니다.')
            
            # 기존 이미지 삭제
            for image in Image.objects.filter(notice=post):
                # 이미지 리스트 비교
                if image.id in [int(id) for id in request.POST.getlist('images')]:
                    # 체크된 파일은 삭제하지 않음
                    continue
                image.delete()

            # 새 이미지 저장
            for f in request.FILES.getlist('photo'):
                image = Image.objects.create(image=f)
                post.photo.add(image)
            post.save()
            return redirect('notice:detail', pk=post.pk)
        
    else:
        form = NoticeForm(instance=post)
    return render(request, 'notice_update.html', {'form': form, 'post': post})

# 게시글 삭제
def delete(request,pk):
    post = Notice.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('notice:index')
    return render(request, 'notice_detail.html',{'post':post})

