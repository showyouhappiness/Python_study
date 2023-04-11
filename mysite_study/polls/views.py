from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):  # 一个通用视图
    """
    使用<app name>/<model name>_detail.html 的模板
    例子中，它将使用 "polls/question_detail.html" 模板。 该模板将使用一个名为 "question" 的上下文变量来访问问题对象。
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):  # 重写get_queryset方法
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):  # 一个通用视图
    """
    DetailView期望从 URL 中捕获名为 "pk" 的主键值, 使用<app name>/<model name>_detail.html 的模板
    例子中，它将使用 "polls/question_detail.html" 模板。 该模板将使用一个名为 "question" 的上下文变量来访问问题对象。
    """
    model = Question
    template_name = '/polls/detail.html'


class ResultsView(generic.DetailView):  # 一个通用视图
    model = Question
    template_name = '/polls/results.html'


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
