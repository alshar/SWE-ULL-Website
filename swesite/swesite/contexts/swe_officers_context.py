def swe_officers_context(request):
    context = {
        'swe_president': {
            'first_name': 'Brianna',
            'last_name': 'Bruno',
            'major': 'Chemical Engineering',
            'title': 'President',
            'email': 'brianna.bruno1@louisiana.edu',
            'linkedin': '',
            'headshot': 'about/officers/bri.png'
        },
        'swe_vp': {
            'first_name': 'Melanie',
            'last_name': 'Toups',
            'title': 'Vice-President',
            'major': 'Chemical Engineering',
            'email': 'c00242174@louisiana.edu',
            'linkedin': '',
            'headshot': 'about/officers/mel.png'
        },
        'swe_secretary': {
            'first_name': 'Sarah',
            'last_name': 'Young',
            'title': 'Secretary',
            'major': 'Chemical Engineering',
            'email': 'sarahanyoung@gmail.com',
            'linkedin': 'http://linkedin.com/in/sarah-young-87b2b0193',
            'headshot': 'about/officers/sarah.png'
        },
        'swe_treasurer': {
            'first_name': 'Nhung (Anna)',
            'last_name': 'Nguyen',
            'title': 'Treasurer',
            'major': 'Chemical Engineering',
            'email': 'nhung.nguyen1@louisiana.edu',
            'linkedin': 'https://www.linkedin.com/in/nhung-nguyen-407081196',
            'headshot': 'about/officers/nh.png'
        },
        'swe_outreach_coordinator': {
            'first_name': 'Gracie',
            'last_name': 'Courville',
            'title': 'Outreach Coordinator',
            'major': 'Chemical Engineering',
            'email': 'gracie.courville1@louisiana.edu',
            'headshot': 'about/officers/gracie.png'
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
            'first_name': 'Al',
            'last_name': 'Sharairi',
            'title': 'Technical Director',
            'major': 'Computer Science',
            'email': 'asharairi@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/al-sharairi/',
            'headshot': 'about/officers/al.jpg'
        },
        'swe_adviser': {
            'first_name': 'Ling (Jessica)',
            'last_name': 'Fei, Ph.D.',
            'title': 'Adviser',
            'major': 'Ph.D. Chemical Engineering',
            'email': 'mikolajczyk@louisiana.edu',
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
