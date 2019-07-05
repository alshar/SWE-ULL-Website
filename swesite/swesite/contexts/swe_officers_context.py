def swe_officers_primary(request):
    context = {
        'swe_president': {
            'first_name': 'Adhwa',
            'last_name': 'Al Uraimi',
            'major': 'Chemical Engineering',
            'title': 'President',
            'email': 'adhwaa.alaremy@outlook.sa',
            'linkedin': 'https://www.linkedin.com/in/adhwa-al-uraimi-563562149/',
            'headshot': 'about/officers/adhwa.jpg'
        },
        'swe_vp': {
            'first_name': 'Kenedi',
            'last_name': 'Habetz',
            'title': 'Vice-President',
            'major': 'Chemical Engineering',
            'email': 'kenedi@games2geaux.com',
            'linkedin': 'https://www.linkedin.com/in/kenedi-habetz-5a9701138/',
            'headshot': 'about/officers/kenedi.jpg'
        },
        'swe_secretary': {
            'first_name': 'Alyssa',
            'last_name': 'DeLattre',
            'title': 'Secretary',
            'major': 'Chemical Engineering',
            'email': 'amd100198@gmail.com',
            'headshot': 'about/officers/alyssa.jpg'
        },

    }

    return context


def swe_officers_secondary(request):
    context = {
        'swe_treasurer': {
            'first_name': 'Reece',
            'last_name': 'Frederick',
            'title': 'Treasurer',
            'major': 'Chemical Engineering',
            'email': 'rpf7981@gmail.com',
            'headshot': 'about/officers/reece.png'
        },
        'swe_outreach_coordinator': {
            'first_name': 'Spencer',
            'last_name': 'Kowalski',
            'title': 'Outreach Coordinator',
            'major': 'Chemical Engineering',
            'email': 'spencer.kowalski@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/spencerkowalski/',
            'headshot': 'about/officers/spencer.jpg'
        },
        'swe_fundraising_chair': {
            'first_name': 'Emma',
            'last_name': 'Armato',
            'title': 'Fundraising Chair',
            'major': 'Chemical Engineering',
            'email': 'eea1998@gmail.com',
            'headshot': 'about/officers/emma.png'
        },

    }
    return context


def swe_officers_tertiary(request):
    context = {
        'swe_technical_director': {
            'first_name': 'Al',
            'last_name': 'Sharairi',
            'title': 'Technical Director',
            'major': 'Computer Science',
            'email': 'asharairi@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/al-sharairi/',
            'headshot': 'about/officers/al.jpg'
        },
        'swe_adviser': {
            'first_name': 'Ashley',
            'last_name': 'Picou Mikolajczyk',
            'title': 'Adviser',
            'major': 'Chemical Engineering',
            'email': 'mikolajczyk@louisiana.edu',
            'headshot': 'about/officers/ashley.png'
        },
        'swe_co_adviser': {
            'first_name': 'Ling (Jessica)',
            'last_name': 'Fei, Ph.D.',
            'title': 'Co-Adviser',
            'major': 'Ph.D. Chemical Engineering',
            'email': 'ling.fei@louisiana.edu',
            'headshot': 'about/officers/ling.png'
        },

    }
    return context
