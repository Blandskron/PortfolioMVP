from django.shortcuts import render, get_object_or_404
from .models import Post

# Vista para mostrar todos los artículos
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Lista de todos los artículos, ordenados por fecha
    return render(request, 'blog/post_list.html', {'posts': posts})

# Vista para mostrar el detalle de un artículo
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
