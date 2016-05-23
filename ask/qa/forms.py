from models import Question, Answer
from django import forms

class AskForm(forms.Form):
	title = forms.CharField(max_length = 100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		title = self.cleaned_data.get('title')
		text = self.cleaned_data.get('text')

		if title == None:
                        raise forms.ValidationError('title is None')
		title = title.strip()
		if len(title) == 0:
			raise forms.ValidationError('title len == 0')

                if text == None:
                        raise forms.ValidationError('text is None')
		text = text.strip()
                if len(text) == 0:
                        raise forms.ValidationError('text len == 0')

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

