from django.views.generic import TemplateView


class PointTrackerView(TemplateView):
    template_name = 'pointtracker/pointtracker.html'
