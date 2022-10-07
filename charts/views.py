from django.shortcuts import render
from django.views.generic import TemplateView
from apps.students.models import Student

# Creating views
class EditorChartView(TemplateView):
    template_name = 'charts/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        allObjects = Student.objects.all()
        # onlyRoes

        context = {
            "qs" : allObjects,
            # "ks" : 
        }

        return context
        # print(context)

    # def testing(request):
    #     myData = Student.objects.filter()