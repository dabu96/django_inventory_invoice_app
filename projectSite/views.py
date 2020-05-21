from django.http import HttpResponse
from django.shortcuts import  render
from django.contrib.auth.decorators import login_required


posts = [
    {
        'make': 'Honda',
        'name': 'Civic',
        'publisher': 'Pub1',
        'date_posted': '1 January, 2020',
        'content': 'This is where the content will go'
    },
    {
        'make': 'Nissan',
        'name': 'Qashqai',
        'publisher': 'Pub2',
        'date_posted': '1 January, 2018',
        'content': 'More content to give extra information'
    }
]

@login_required
def dashboard(request):
    context = {
        'title': 'title',
        'posts': posts
    }
    return render(request, 'homepage.html', context)

