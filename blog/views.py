from django.shortcuts import render


posts =[
    {
        'author' : 'sarthak',
        'title'  : 'Blog post 1',
        'content': 'First post content',
        'date_posted'  : 'April 24,2020'
    },
      {
        'author' : 'sarth',
        'title'  : 'Blog post 2',
        'content': 'second post content',
        'date_posted'  : 'April 25,2020'
    },
]

# Create your views here.
def home(request):
    context ={
        'posts' : posts
    }
    return render(request,'blog/home.html', context)  

def about(request):
    return render(request,'blog/about.html',{ 'title' : 'About' })  