def swe_volunteer(request):
    context = {
        'conference_abbreviation': 'WE20',
        'conference_website': 'https://partnerguide.swe.org/conferences/',
        'points_needed': '20',
        'students_taking': '30'
    }
    return context
