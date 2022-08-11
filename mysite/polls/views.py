from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def detail(request, question_id, time):
    """
        Next Days Work 11/08/2022
    """
    time = "abc"
    return HttpResponse("You're looking at question %s, and current tim is: %s " %question_id %time )

def result(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" %question_id)