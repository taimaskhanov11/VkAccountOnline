# Create your views here.
from django.db.models import Max, Count, Sum, Q
from django.views.generic import ListView, UpdateView

from app_answer.forms import InputForm
from app_answer.models import Category


class AnswerListView(ListView):
    model = Category
    queryset = Category.objects.prefetch_related('inputs', 'outputs')
    form_class = InputForm

    def post(self, request, *args, **kwargs):
        print(request)

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        more_inputs = Category.objects.annotate(inputs_count=Count('inputs')).order_by('-inputs_count')[0]

        context['info'] = {
            # 'Всего категорий':'',
            # 'Всего входов':'',
            # 'Всего выходов':'',
            'Больше всего входов': (more_inputs.title, more_inputs.inputs_count),
            # 'Больше всего выходов':Category.objects.values('title','inputs').annotate(max_name = Max('inputs')),
        }
        return context
