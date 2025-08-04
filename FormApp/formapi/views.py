from django.shortcuts import render, redirect
from formapi.forms import ProfileForm
from formapi.models import Profile


def home(request):
    candidates = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'formapi/home.html', {'form': form, 'candidates': candidates})


def candidate_detail(request, pk):
    candidate = Profile.objects.get(pk=pk)
    return render(request, 'formapi/candidate.html', {'candidate': candidate})
