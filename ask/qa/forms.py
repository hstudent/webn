from models import Question, Answer
from django import forms

class AskForm(forms.Form):
	title = forms.CharField(max_length = 100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):

		pass

	def save(self):
		_title = self.cleaned_data['title']
		_text = self.cleaned_data['text']
		question = Question(title = _title, text = _text)
		question.save()
		return question

class AnswerForm(forms.Form):
        text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

        def clean(self):
                pass

        def save(self):
                _question_id = self.cleaned_data['question']
                _text = self.cleaned_data['text']
                answer = Answer(question_id = _question_id, text = _text)
                answer.save()
                return answer

