from django.shortcuts import render, redirect
from django import forms
from ghostpost.models import RoastBoast
from ghostpost.forms import RoastBoastAdd


def index(request):
    html = "index.html"
    recipe = RoastBoast.objects.order_by("-posttime")
    
    return render(request, html, {'data':recipe})


def roastboastaddview(request):
    html = "getschwifty.html"
    form = None
    if request.method == "POST":
        form = RoastBoastAdd(request.POST)

        if form.is_valid():
            data= form.cleaned_data
            RoastBoast.objects.create(
                roast=data['roast'],
                content=data['content'],
                
                
            )
            return redirect("/")
    else:
        form = RoastBoastAdd()
    return render(request, html, {"form": form})


def roasts(request):
    # filter for true in the boolean
    html = "roasts.html"
    roasts = RoastBoast.objects.filter(roast=True).order_by("-posttime")
    
    return render(request, html, {'data':roasts})

def boasts(request):
    # filter false for boolea
    html = "boasts.html"
    boasts = RoastBoast.objects.filter(roast=False).order_by("-posttime")
    return render(request, html, {"data": boasts})

def popular(request):
    #  filter by upvote count
    html = "popular.html"
    popular = RoastBoast.objects.all()
    popular = sorted(list(popular), key=lambda post: post.total_votes, reverse=True)
    return render(request, html, {"data": popular})

def upvote(request, id):
        roast_post = RoastBoast.objects.filter(id=id).first()
        roast_post.upvotes += 1
        roast_post.save()
        return redirect("/")


def downvote(request, id):
        roast_post = RoastBoast.objects.filter(id=id).first()
        roast_post.downvotes += 1
        roast_post.save()
        return redirect("/")

