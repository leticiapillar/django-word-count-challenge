from django.shortcuts import render, redirect
from .forms import WordCountForm

# Create your views here.
def word_count_view(request):
    form = WordCountForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            wordcount = form.save(commit=False)
            wordcount.total_words = 1
            print("--- Debug: wordcount ---")
            print(wordcount)
            print("-----------")
            wordcount.save()
            return redirect("index")

    return render(
        request,
        "word_count_app/index.html",
        {"form": form},
    )
