from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    text = request.POST.get('text', 'default')
    checked = request.POST.get('isChecked', 'off')
    caps = request.POST.get('full_caps','off')
    nlines = request.POST.get('newline-remover','off')
    spaces = request.POST.get('extraspaceremover','off')
    count1 = request.POST.get('char-count','off')
    punclists = '''!,;/().?:""-[]{}<>\@#$%^&*_~`!='+'''
    if checked == 'on':
        analyzed = ''
        for char in text:
            if char not in punclists:
                analyzed += char
        text = analyzed
    if caps == 'on':
        analyzed = ''
        for char in text:
            analyzed += char.upper()
        text = analyzed
    if nlines == 'on':
        analyzed = ''
        for char in text:
            if char != '\n' and char != '\r':
                analyzed += char
        text = analyzed
    if spaces == 'on':
        analyzed = ''
        for i,char in enumerate(text):
            if not(text[i] == " " and text[i+1] == " "):
                analyzed += char
        text = analyzed

    if count1 == 'on':
        count = f'Count of Characters in the text "{text}": {len(text)}'
        return render(request, 'analyze.html', {'value': text, 'count': count})
    else:
        return render(request, 'analyze.html',{'value': text, 'count': ''})


def about(request):
    return render(request, 'about.html')
