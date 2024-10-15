from django.shortcuts import render

def home(request):
    title = 'Title of the page'
    content = 'This is the content...'
    return render(request, 'home.html', {'title': title, 'content': content})

def contact(request):
    title = 'Contact Us'
    content = 'Here is how you can contact us...'
    return render(request, 'contact.html', {'title': title, 'content': content})
