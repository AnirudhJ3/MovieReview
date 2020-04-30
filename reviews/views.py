from django.shortcuts import render,  get_object_or_404
from movies.models import Movie
from reviews.models import Review
from . import forms
    

# Create your views here.
def review(request, id=None):
    instance = get_object_or_404(Movie, id=id)
    reviews = Review.objects.filter(movie_name__exact=instance.name)
    
    if request.method == 'POST':
        form = forms.CreateReview(request.POST)
        
        
        if form.is_valid():

            #save review to db
            inst=form.save(commit=False)
            inst.author = request.user
            inst.movie_name = instance.name
            inst.star = 5
            inst.save()

    else:
        form = forms.CreateReview()
    context = {
        "title" :instance.name,
        "instance":instance,
        "reviews":reviews,
        "form" : form
    }
    
    return render(request,'review.html',context)

 