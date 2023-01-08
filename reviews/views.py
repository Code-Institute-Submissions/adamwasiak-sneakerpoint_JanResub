from django.shortcuts import render
from .forms import ReviewForm


def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user
            form.save()
            return render(request, 'reviews/successreview.html')
    form = ReviewForm()
    context = {'form': form}
    return render(request, 'reviews/review.html', context)
