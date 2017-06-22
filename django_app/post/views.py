from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'post/post_list.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        post.delete()
    return redirect('post:post_list')


def post_modify(request, post_pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            post.comment = comment
            post.save()
            return redirect('post:post_list')
    else:
        context = {
            'form': CommentForm()
        }
        return render(request, 'post/post_modify.html', context)
