from .models import People
from django.views.generic import ListView
from django.shortcuts import render
from django.http import JsonResponse

class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'peoples'
    model = People
    paginate_by = 50
    ordering = ['id']
    
def search(request):
    return render(request, 'people/search.html')


def searchResult(request):
    if request.is_ajax():
        body = request.body.decode('UTF-8')
        if body != "":
            qs = People.objects.filter(bio__icontains=body)
            data = []
            for q in qs:
                item = {
                    'pk':q.pk,
                    'name': q.name,
                    'e_mail': q.e_mail,
                    'bio':q.bio,
                    'location':q.location,
                    'hireable':q.hireable,
                    'user_url':q.user_url,
                    'avatar_url':q.avatar_url
                }
                data.append(item)
            res = data
            return JsonResponse({'data':res})
    return JsonResponse({})



            