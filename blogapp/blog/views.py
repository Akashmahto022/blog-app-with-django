from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'blog_form.html', {'form':form})

def blog_edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog_form.html', {'form':form})
    
    
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user = request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    
    return render(request, 'blog_confir_delete.html', {'blog':blog})
    