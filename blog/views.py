from django.shortcuts import render


posts = [
    {
        'author':'paata',
        'title': 'blog1',
        'content': '1post',
        'date_posted': '27.12.24'
    },
    {
        'author':'paata',
        'title': 'blog2',
        'content': '1post2',
        'date_posted': '27.11.24'
    }
]


def home(req):
    context = {
        'posts': posts
    }
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html', {'title': 'About'})
