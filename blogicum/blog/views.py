from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category
from . import constants


def get_published_posts():
    return Post.objects.select_related(
        'category', 'author', 'location').filter(
            pub_date__lte=timezone.now(),
            category__is_published=True,
            is_published=True,
    )


def index(request):
    template = 'blog/index.html'
    post_list = get_published_posts()[:constants.POSTS_LIMIT]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post_list = get_object_or_404(
        get_published_posts(),
        id=post_id
    )
    context = {'post': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True
    )
    posts = get_published_posts().filter(category=category)
    context = {'post_list': posts, 'category': category}
    return render(request, template, context)
