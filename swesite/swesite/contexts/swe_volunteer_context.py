def swe_volunteer(request):
    context = {
        'conference_abbreviation': 'WE19',
        'conference_website': 'https://we19.swe.org/',
        'points_needed': '30'
    }
    return context
