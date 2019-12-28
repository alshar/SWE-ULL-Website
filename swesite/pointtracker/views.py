from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from pointtracker.forms import PointTrackerLoginForm
from swesite.contexts.swe_social_context import swe_social
from swesite.contexts.swe_volunteer_context import swe_volunteer
from users.spreadsheet import points_sheet, client, creds


class PointTrackerLoginView(FormView):
    template_name = 'pointtracker/pointtracker.html'
    form_class = PointTrackerLoginForm
    success_url = reverse_lazy('pointtracker')

    def get_context_data(self, **kwargs):
        context = super(PointTrackerLoginView, self).get_context_data(**kwargs)
        context['swe_social'] = swe_social(request=PointTrackerLoginView)
        context['swe_volunteer'] = swe_volunteer(request=PointTrackerLoginView)
        return context

    def form_valid(self, form):
        return super(PointTrackerLoginView, self).form_valid(form)

    def post(self, request, *args, **kwargs):

        # clean data
        ulid = request.POST['ulid'].strip().lower()
        first_name = request.POST['first_name'].strip().lower()
        last_name = request.POST['last_name'].strip().lower()

        # re-validate token if it's expired
        if creds.access_token_expired:
            client.login()

        if self.member_exists(ulid=ulid, first_name=first_name, last_name=last_name):
            member_row = self.get_member_row(ulid=ulid)

            """
                get_all_records() doesn't include the heading, 
                and puts the first member at 0
                member_row is the member's actual row number in the spreadsheet, including the heading, 
                AND the rows start at 1
                so member_row - 2 must be used
                
                if confused, look at the values in debug mode
            """
            member_data = points_sheet.get_all_records()[member_row - 2]

            """
               (assumes a 0 in the event column means member did not attend event)
            """
            events_attended = {
                event: points_earned for event, points_earned in member_data.items()

                if points_earned != "" and
                   points_earned != 0 and
                   isinstance(points_earned, (int, float)) and
                   event != "total"
            }

            context = self.get_context_data(**kwargs)
            context['member_data'] = member_data
            context['events_attended'] = events_attended

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
