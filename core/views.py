from django.shortcuts import render


def index(request):
    """
    Return the main page for website.
    """
    return render(request, 'core/index.html', {})
