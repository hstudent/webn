from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from models import Question, Answer
from forms import AskForm, AnswerForm
from django.http import Http404
from django.core.paginator import Paginator

def answer_view(request):
        if request.method == "POST":
                form = AnswerForm(request.POST)
                if form.is_valid():
                        answer = form.save()
                        url = '/question/' + str(answer.question_id)
                        return HttpResponseRedirect(url)
        else:
                form = AnswerForm()

        return render(request, '/home/box/web/ask/qa/templates/answer.html', 
                {
                'form':form
                })


def ask_view(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = '/question/' + str(question.id)
			return HttpResponseRedirect(url)
	else:
		form = AskForm()

	return render(request, '/home/box/web/ask/qa/templates/ask.html', 
		{
		'form':form
		})

def popular_view(request, *args, **kwargs):
        try:
                page = int(request.GET.get('page', 1))
        except:
                page = 1

        questions = Question.objects.all().order_by('-rating')

        paginator = Paginator(questions, 10)
        paginator.base_url = '/question/'
        questions = paginator.page(page)
        return render(request, 
                '/home/box/web/ask/qa/templates/questions.html',
                {
                        'questions':questions,
                        'paginator':paginator
                })
        #return HttpResponse('page' + str(page))


def page_view(request, *args, **kwargs):
	try:
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	#questions = []
	#for i in range(55):
        #	question = Question(title = 'title' + str(i), text='text1' + str(i), id = i)
	#	questions.append(question)

	questions = Question.objects.all().order_by('-id')

	paginator = Paginator(questions, 10)
	paginator.base_url = '/question/'
	questions = paginator.page(page)
	return render(request, 
		'/home/box/web/ask/qa/templates/questions.html',
		{
			'questions':questions,
			'paginator':paginator
		})
	#return HttpResponse('page' + str(page))

def test(request, *args, **kwargs):
        qid = int(args[0])

	try:
		question = Question.objects.get(id = qid)
	except Question.DoesNotExist:
		raise Http404

	answers = Answer.objects.filter(question = question)

	#question = Question(title = 'title1', text='text1', id = qid)
	#answers = []
	#for i in range(10):
	#	answer = Answer(text = 'answer_' + str(i), id = i)
	#	answer.question = question
	#	answers.append(answer)

	#question.id = 123
	return render(request, 
		'/home/box/web/ask/qa/templates/question.html', 
		{
			'question':question,
			'answers':answers
		})
	#return HttpResponse('OK')

