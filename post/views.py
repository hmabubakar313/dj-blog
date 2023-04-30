from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.




def post(request):
    return render(request, 'blog.html')




def save_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.POST['bimgs']
        post = request.POST['content']
        
        # save data to database
        post = Post(title=title, image=image, post=post)
        post.save()
        return HttpResponse('Post saved successfully')
    else:
        return HttpResponse('Invalid method')
        