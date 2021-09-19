def swe_officers_context(request):
    context = {
        'swe_president': {
            'first_name': 'Sarah',
            'last_name': 'Young',
            'major': 'Chemical Engineering',
            'title': 'President',
            'email': 'sarahanyoung@gmail.com',
            'linkedin': 'http://linkedin.com/in/sarah-young-87b2b0193',
            'headshot': 'about/officers/sarah.png'
        },
        'swe_vp': {
            'first_name': 'Gracie',
            'last_name': 'Courville',
            'title': 'Vice-President',
            'major': 'Chemical Engineering',
            'email': 'gracie.courville1@louisiana.edu',
            'linkedin': '',
            'headshot': 'about/officers/gracie.png'
        },
        'swe_secretary': {
            'first_name': 'Camryn',
            'last_name': 'Adamson',
            'title': 'Secretary',
            'major': 'Chemical Engineering',
            'email': '',
            'linkedin': '',
            'headshot': 'about/officers/camryn.jpeg'
        },
        'swe_treasurer': {
            'first_name': 'April',
            'last_name': 'Bourlet',
            'title': 'Treasurer',
            'major': 'Chemical Engineering',
            'email': '',
            'linkedin': '',
            'headshot': 'about/officers/april.jpeg'
        },
        'swe_outreach_coordinator': {
            'first_name': 'Mary',
            'last_name': 'Nguyen',
            'title': 'Outreach Coordinator',
            'major': 'Chemical Engineering',
            'email': '',
            'headshot': 'about/officers/mary.jpeg'
        },
        'swe_fundraising_chair': {
            'first_name': 'Kayla',
            'last_name': 'Richard',
            'title': 'Fundraising Chair',
            'major': 'Chemical Engineering',
            'email': 'kayla.richard1@louisiana.edu',
            'headshot': 'about/officers/kayla.jpg'
        },
        'swe_technical_director': {
            'first_name': 'Te Anne',
            'last_name': 'Yap',
            'title': 'Technical Director',
            'major': 'Computer Science',
            'email': 'te-anne.yap1@louisiana.edu',
            'linkedin': 'https://www.linkedin.com/in/tnyap/',
            'headshot': 'about/officers/anne.jpeg'
        },
        'swe_adviser': {
            'first_name': 'Ling (Jessica)',
            'last_name': 'Fei, Ph.D.',
            'title': 'Adviser',
            'major': 'Ph.D. Chemical Engineering',
            'email': 'ling.fei@louisiana.edu',
            'headshot': 'about/officers/ling.png'
        },
        'swe_co_adviser': {
            'first_name': 'Melanie',
            'last_name': 'Sanders',
            'title': 'Co-Adviser',
            'major': 'M.S. Chemical Engineering',
            'email': 'msanders@louisiana.edu',
            'headshot': 'about/officers/sanders.jpg'
        },
        'swe_student_adviser': {
            'first_name': 'Kenedi',
            'last_name': 'Habetz',
            'title': 'Student Adviser',
            'major': 'Chemical Engineering',
            'email': 'kenedi@games2geaux.com',
            'headshot': 'about/officers/kenedi.jpg'
        }

    }

    return context
