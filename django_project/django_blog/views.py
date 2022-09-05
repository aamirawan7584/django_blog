from django.shortcuts import render

posts = [

    {
        'author':'aamir',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'August 17, 2022'
    },
    {
        'author':'aamir',
        'title':'Blog Post 2',
        'content':'First post content',
        'date_posted':'August 17, 2022'
    },
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request=request,template_name='blog/home.html',context=context)

def about(request):
    return render(request=request,template_name='blog/about.html',context={'title':'about'})