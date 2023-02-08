from django.shortcuts import render

def index(request):
    """Home Page of app Learning Log"""
    return render(request, 'learning_logs/index.html')
