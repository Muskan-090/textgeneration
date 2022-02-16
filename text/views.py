from django.shortcuts import render
from django.http import HttpResponse
from .gnr import txtgen
from .forms  import Generation



def ds(request):
    
    if request.method == 'POST':
        fm = Generation( request.POST)
        if fm.is_valid():
            txt  = fm.cleaned_data['q_txt']
            seed_text = txtgen(txt)
            return render(request, 'txt.html', {'txt':seed_text})

    else:
        fm = Generation(label_suffix=' ')
        return render(request, 'home.html', {'form':fm})


















