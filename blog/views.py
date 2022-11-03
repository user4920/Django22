from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    #템플릿 모델명_list.html : post_list.html
    #파라미터 모델명_list : post_list

class PostDetail(DetailView):
    model = Post
    #템플릿 모델명_detail.html : post_detail.html
    #파라미터 모델명 : post

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(request, 'blog/post_list.html', {
        'tag': tag,
        'post_list' : post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.object.filter(category=None).count
    })

#def index(request):
#    posts = Post.objects.all().order_by('-pk')
#    return render(request, 'blog/index.html', {'posts':posts})

#def single_post_page(request, pk):
#    post = Post.objects.get(pk=pk)
#    return render(request, 'blog/single_post_page.html', {'post':post})