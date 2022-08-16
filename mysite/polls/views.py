from audioop import reverse
from re import template
import re
from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


"""Create your views here."""


# def index(request):
#     latest_question_list =Question.objects.order_by('-publication_date')[:5]
#     output = ','.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-publication_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:5]
    context = {'latest_question_list': latest_question_list}   
    return render(request,'polls/index.html', context)

# def detail(request, question_id): 
#     try: 
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question Does not Found")
#     return render(request, 'polls/details.html', {'question' : question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/details.html', {'question' : question})
          

def result(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})

#Voting Funtion
def vote(request, question_id):
    question =get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Rapidly the question voting form
        return render(request, 'polls/details.html', {'question': question, 'error_massage' : "Alert ! You Don't select a choice !!!",})
    else:
        """Always return an HttpResponseRedirect after succesfilly dealing 
        with POST data . This prevents data from being posted twice if a user hit Back button"""
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))