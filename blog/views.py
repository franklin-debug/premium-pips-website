from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog


# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs,}
    return render(request,'blog.html',context)


def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog,id=blog_id)

    context = {
        'blog':blog,
    }
    return render(request, 'blog_detail.html', context)