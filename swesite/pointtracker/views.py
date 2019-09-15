from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from pointtracker.forms import PointTrackerLoginForm
from swesite.contexts.swe_social_context import swe_social
from users.spreadsheet import points_sheet


class PointTrackerLoginView(FormView):
    template_name = 'pointtracker/pointtracker.html'
    form_class = PointTrackerLoginForm
    success_url = reverse_lazy('pointtracker')

    def get_context_data(self, **kwargs):
        context = super(PointTrackerLoginView, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=PointTrackerLoginView)
        return context

    def form_valid(self, form):
        return super(PointTrackerLoginView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        ulid = request.POST['ulid'].strip().lower()
        first_name = request.POST['first_name'].strip().lower()
        last_name = request.POST['last_name'].strip().lower()

        if self.member_exists(ulid=ulid, first_name=first_name, last_name=last_name):
            member_row = self.get_member_row(ulid=ulid)
            member_data = points_sheet.get_all_records()[member_row - 2]

            context = self.get_context_data(**kwargs)
            context['member_data'] = member_data

            return render(request, 'pointtracker/member_point_sheet.html', context=context)
        else:

            context = self.get_context_data(**kwargs)
            return render(request, 'pointtracker/member_not_found.html', context=context)

    def member_exists(self, **kwargs):
        ulid = kwargs['ulid']
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']

        try:
            points_sheet.find(ulid)
            points_sheet.find(first_name)
            points_sheet.find(last_name)
            return True
        except:
            return False

    def get_member_row(self, **kwargs):
        return points_sheet.find(kwargs['ulid']).row

# points_sheet.get_all_records()[points_sheet.find("c00004424").row - 2]
