from django.shortcuts import render
from django.http import HttpResponse, Http404
from poll.models import *
# Create your views here.


def home(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)
    # return HttpResponse('HELLO POLLS HOME PAGE')

def details(request, id=None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
        
    context['question'] = question
    return render(request, 'polls/details.html', context)

def poll(request, id=None):
    if (request.method == "GET"):
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request, 'polls/poll.html', context)
    if (request.method == "POST"):
        data = request.POST
        print(f'MY DATA ===> {data}')
        user_id = 1
        # achoice = Choice.objects.get(data.choice)
        # print(f'A CHOICE ===> {achoice}')        
        # si tu souhaite instancier lobjet directement sans etre obligeé de faire 
        # une requete model.objects.get(id=x), utilise _id
        ret = Answer.objects.create(user_id=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Your vote is successuf")
        else:
            return HttpResponse("Your vote have been broken")