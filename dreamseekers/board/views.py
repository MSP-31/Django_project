from django.shortcuts import redirect, render
from user.models import Users
from .models import Post
from .forms import BoardForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    # 모든 Post를 불러오고 페이지에 가져옴
    post_list = Post.objects.order_by('-created_dt')
    page = request.GET.get('page') # 페이지

    # 출력하는 Post수 제한
    paginator = Paginator(post_list,5)

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

    return render(request, 'index.html',{'page_obj':page_obj, 'paginator':paginator, 'custom_range':custom_range})

def posting(request, pk):
    # 게시글에서 pk(primary_key)로 해당 게시글 검색
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html',{'post':post})

# 글쓰기
def board_write(request):
    # 로그인 여부 확인
    if not request.session.get('user'):
        return redirect('/user/login')

    elif request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_Post = Post(
                title = form.cleaned_data['title'],
                contents = form.cleaned_data['contents'],
                author = user
            )
            new_Post.save()
            return redirect('/board')
        else:
            # 폼이 유효하지 않을 경우, 사용자가 입력한 데이터를 폼에 다시 채워 넣습니다.
            form = BoardForm(request.POST)
    else:
        form = BoardForm()
        
    return render(request, 'board_write.html', {'form':form})

