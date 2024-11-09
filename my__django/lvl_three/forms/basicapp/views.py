from django.shortcuts import render
from basicapp import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        
        if form.is_valid():
            print('Success Validation')
            print('Nama :', form.cleaned_data['name'])
            print('Email :', form.cleaned_data['email'])
            print('Alasan :', form.cleaned_data['text'])
            print('Password :', form.cleaned_data['password'])        
        

    return render(request, 'basicapp/form.html', {'form':form})
