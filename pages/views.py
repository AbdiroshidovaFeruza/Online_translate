from django.shortcuts import render
from googletrans import Translator
# Create your views here.

def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')

def Contactus(request):
    return render(request,'contactus.html')

def Translated(request):
    text =request.GET.get('text')
    lang =request.GET.get('lang')
    # print('text:',text,'lang:',lang)


    translator = Translator()
    dt = translator.detect(text)
    dt2 = dt.lang
    translated = translator.translate(text, lang)
    tr = translated.text
    return render(request, 'translated.html', {'translated':tr, 'u_lang':dt2,'t_lang':lang})

