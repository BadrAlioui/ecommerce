from django.shortcuts import render

def post(request):
    title = 'My Blog Post'
    content = 'This is my blog post content.'
    return render(request, 'blog/post.html', {'title': title, 'content': content})



