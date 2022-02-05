from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def post_list(request):
  posts = Post.objects.all()
  comments = Comment.objects.all()
  ctx = {'posts': posts, 'comments': comments}
  return render(request, template_name='post_list.html', context=ctx)


def post_create(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save()
      post.likes = 0
      post.save()
      return redirect('pirostagram:post_detail', post.id)
  else:
    form = PostForm()
    ctx = {'form': form}
    return render(request, template_name='post_form.html', context=ctx)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.all()
    ctx = {'post': post, 'comments': comments}
    return render(request, template_name='post_detail.html', context=ctx)


def post_update(request, pk):
  post = get_object_or_404(Post, id=pk)
  current_likes = post.likes

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save()
      post.likes = current_likes
      post.save()
      return redirect('pirostagram:post_detail', post.id)

  else:
    form = PostForm(instance=post)
    ctx = {'form': form, 'post': post}
    return render(request, template_name='post_form.html', context=ctx)


def post_delete(request, pk):
  post = get_object_or_404(Post, id=pk)
  post.delete()
  return redirect('pirostagram:post_list')


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
  req = json.loads(request.body)
  post_id = req['id']

  post = Post.objects.get(id=post_id)
  post.likes += 1
  post.save()
  likes = post.likes

  return JsonResponse({'id': post_id, 'likes': likes})


@csrf_exempt
def comment_ajax(request):
  req = json.loads(request.body)
  post_id = req['id']
  comment_content = req['comment']
  post = Post.objects.get(id=post_id)

  comment = Comment.objects.create(post=post, comment=comment_content)
  comment.save()
  return JsonResponse({'post_id': post_id, 'comment_id': comment.id})


@csrf_exempt
def comment_delete_ajax(request):
  req = json.loads(request.body)
  comment_id = req['id']
  comment = Comment.objects.get(id=comment_id)
  comment.delete()
  return JsonResponse({'comment_id': comment_id})