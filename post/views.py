from django.shortcuts import render, HttpResponse
from .models import Post
from users.models import User

# Create your views here.




def create(request):
    return render(request, 'blog.html')




def save_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        post = request.POST['content']
        image = request.FILES.get('bimgs', False)
        # get current user id
        user = request.user
        author_id = user.user_id
        print('author_id', author_id)
        # print('author_id', author_id)
        print('image', image)
        print('title', title)
        print('post', post)
        

        post = Post(title=title, post=post, author_id=author_id)
        if image:
            post.image = image 
        post.save()
        

        return HttpResponse('done')
    else:
        return HttpResponse('Invalid method')
    
    

def feed(request):
    post = Post.objects.all()
    return render(request, 'feed.html', {'post':post})





        