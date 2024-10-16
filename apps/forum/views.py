from django.shortcuts import render, redirect
from django.utils import timezone
from random import choice
from .utils import getNameChoices
from ..footer.utils import getContact, getAllInformations 
from .models import Post, Comment, PopularTopic, TopImage, PageDescription

def forum(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    popular_topics = PopularTopic.objects.all()
    top_images = TopImage.objects.all()
    description = PageDescription.objects.first()
    current_date = timezone.now()

    comentarios_por_post = {}

    for comment in comments:
        if comment.post.id not in comentarios_por_post:
            comment.quantity_comments = comment.post.comentarios.count()

            difference = current_date - comment.date
            if difference.days > 0:
                comment.difference_dates = f"{difference.days} dia(s) atrás"
            elif difference.seconds // 3600 > 0:
                comment.difference_dates = f"{difference.seconds // 3600} hora(s) atrás"
            else:
                comment.difference_dates = f"{difference.seconds // 60} minuto(s) atrás"

            comentarios_por_post[comment.post.id] = comment

    comentarios = list(comentarios_por_post.values())

    for post in posts:
        difference = current_date - post.date
        if difference.days > 0:
            post.difference_dates = f"{difference.days} dia(s) atrás"
        elif difference.seconds // 3600 > 0:
            post.difference_dates = f"{difference.seconds // 3600} hora(s) atrás"
        else:
            post.difference_dates = f"{difference.seconds // 60} minuto(s) atrás"

        post.comentado_por = list({comment.userNameComment for comment in comments if comment.post.id == post.id})

    context = {
        'footerContact': getContact(),
        'footerInformations': getAllInformations(),
        'posts': posts,
        'comments': comentarios,  
        'popular_topics': popular_topics,
        'top_images': top_images,
        'description': description,
    }

    return render(request, 'forum.html', context)

def criar_post(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        post = request.POST.get("comment")
        user_name = choice(getNameChoices()[0])

        post = Post(
            title=title,
            userName=user_name,
            description=post
        )

        post.save()

    return redirect("/forum")

    
