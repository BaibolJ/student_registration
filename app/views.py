from django.shortcuts import render,redirect
from .forms import StudentForms

def st_registre(request):
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('st_registre')
    else:
        form = StudentForms()
    return render(request, 'app/st_registre.html', {'form': form})


