def fall_19(request):
    context = {
        'meeting_1': {
            'display_title': 'First General Meeting',
            'display_date': '9/11',
            'img_paths': [
                'events/img/carousel/fall19/meeting_1/meeting_1_1.png',
            ]
        },

        'les_bbq': {
            'display_title': 'Louisiana Engineering Society BBQ',
            'display_date': '9/6',
            'img_paths': [
                'events/img/carousel/fall19/les_bbq/les_bbq_1.JPG',
                'events/img/carousel/fall19/les_bbq/les_bbq_2.JPG',

            ]
        }

    }

    return context