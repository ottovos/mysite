from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Choice # importing the classes from models.py makes them available in views


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] #import class objects
#     template = loader.get_template('polls/index.html') # variable to retrieve  template index.html
#     context = {
#         'latest_question_list': latest_question_list,
#     } #context is dict to allow for multiple variables in the template.
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
