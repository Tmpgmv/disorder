from django.utils.timezone import now
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views import generic
from weasyprint import HTML

from educational_facilities.models import EducationalFacility
from tasks.forms import TaskFormForPrinting
from tasks.models import Task


class PrintableTaskDetailView(generic.View):

    template_name = "tasks/printabletask_detail.html"

    def get_context_data(self, **kwargs):
        context = {}
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        context['form'] = TaskFormForPrinting()
        context['current_year'] = now().year
        return context

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.get_context_data(),
        )

    def post(self, request, *args, **kwargs):
        educational_facility = get_object_or_404(EducationalFacility, pk=request.POST.get('educational_facility'))
        task = get_object_or_404(Task, pk=request.POST.get('task'))

        context = {}
        if educational_facility.pk == 2:
            self.template_name = "tasks/pkgh_task_front_page.html"
            context["facility"] = educational_facility
            context["task"] = task

        html_string = render_to_string(
            self.template_name,
            context,
            request,
        )


        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf = html.write_pdf()


        response = HttpResponse(pdf, content_type='application/pdf')

        response['Content-Disposition'] = 'inline; filename="task.pdf"'

        return response

        # return render(request, self.template_name, context)