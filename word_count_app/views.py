from django.shortcuts import render, redirect
from .forms import WordCountForm
from .models import WordCountModel

# Create your views here.
def word_count_view(request):
    form = WordCountForm(request.POST)
    count_words = 0
    if request.method == "POST":
        if form.is_valid():
            wordcount = form.save(commit=False)
            count_words = len(wordcount.text.split())
            wordcount.total_words = count_words
            wordcount.save()
    
    form = WordCountForm()
    return render(request, "word_count_app/index.html", { "form": form, "count_words": count_words})
