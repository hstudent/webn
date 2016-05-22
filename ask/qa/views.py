from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from models import Question, Answer
from django.http import Http404
from django.core.paginator import Paginator

def page_view(request, *args, **kwargs):
	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	questions = []
	for i in range(55):
        	question = Question(title = 'title' + str(i), text='text1' + str(i), id = i)
		questions.append(question)

	paginator = Paginator(questions, 10)
	paginator.base_url = '/question/'
	questions = paginator.page(page)
	return render(request, 
		'/home/box/web_/ask/qa/templates/questions.html',
		{
			'questions':questions,
			'paginator':paginator
		})
	#return HttpResponse('page' + str(page))

def test(request, *args, **kwargs):
	qid = int(args[0])
	if qid > 100:
		raise Http404

	question = Question(title = 'title1', text='text1', id = qid)
	answers = []
	for i in range(10):
		answer = Answer(text = 'answer_' + str(i), id = i)
		answer.question = question
		answers.append(answer)

	#question.id = 123
	return render(request, 
		'/home/box/web_/ask/qa/templates/question.html', 
		{
			'question':question,
			'answers':answers
		})
	#return HttpResponse('OK')

