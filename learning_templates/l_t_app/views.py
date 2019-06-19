from django.shortcuts import render

# Create your views here.
def index(request):
    index_dict = {'text': 'Hello World','number':100}
    return render(request, 'l_t_app/index.html', index_dict)

def other(request):
    return render(request, 'l_t_app/other.html')

def relative(request):
    return render(request, 'l_t_app/relative_url_templates.html')
