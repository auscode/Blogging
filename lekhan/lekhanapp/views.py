from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib import messages
from notifications.signals import notify


from .models import *
from .forms import *


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']
    # ordering =['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(
        request,
        'categories.html',
        {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts},
    )

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff =get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        notifications = self.request.user.notifications.filter(
            action_object_object_id=stuff.id,
            verb='added a new post',
        )

        context['cat_menu'] = cat_menu
        context["total_likes"] =total_likes
        context["liked"] = liked
        context["notifications"] = notifications 
        print(f"context {context}")
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title',  'body')
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        # Create and send a notification
        notify.send(
            self.request.user,
            recipient=self.request.user,  # You can change the recipient based on your requirements
            verb='added a new post',
            action_object=self.object,
        )

        messages.success(self.request, 'Post successfully added!')
        print(f"response {response}")
        return response


class AddCommentView(CreateView):
    model = Comment 
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    # fields = ('title',  'body')
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title',  'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']


class DeletePostView(DeleteView):
    model = Post
    # form_class = EditForm
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
