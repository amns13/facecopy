from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


class TimeLineView(LoginRequiredMixin, View):
    form_class = PostForm
    template_name = 'post/index.html'


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        posts = Post.objects.all()
        return render(request, self.template_name, {'form': form, 'posts': posts})


@login_required
@require_POST
def create_post_view(request):
    if request.is_ajax():
        content = request.POST['content']
        new_post = Post(content=content, user=request.user)
        new_post.save()
        response = {
            'message': 'Post added successfully!'
        }

        return JsonResponse(response)