from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.




def create(request):
    return render(request, 'blog.html')




def save_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        post = request.POST['content']
        image = request.FILES.get('bimgs', False)
        print('image', image)
        print('title', title)
        print('post', post)

        post = Post(title=title, post=post)
        if image:
            post.image = image 
        post.save()
        

        return httpResponse('Post saved successfully')
    else:
        return HttpResponse('Invalid method')
    
    

def feed(request):
    post = Post.objects.all()
    return render(request, 'feed.html', {'post':post})





        