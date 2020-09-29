def swe_volunteer(request):
    context = {
        'conference_abbreviation': 'WE20',
        'conference_website': 'https://we20.swe.org/',
        'points_needed': '20',
        'students_taking': '30'
    }
    return context
