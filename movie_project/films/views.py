from django.shortcuts import render, redirect
from .models import Film

def create_film(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        review = request.POST.get('review')
        Film.objects.create(title=title, description=description, review=review)
        return redirect('film_list')
    return render(request, 'create_film.html')

def film_list(request):
    films = Film.objects.all()
    return render(request, 'film_list.html', {'films': films})