def fall_19(request):
    context = {
        'upcoming_events': {
            'display_title': 'Upcoming Events',
            'display_date': 'See Flyer for Dates',
            'img_paths': [
                'events/img/carousel/fall19/bake_sale_1/flyer.png',
                'events/img/carousel/fall19/meeting_1/meeting_1_1.png'
            ]
        },
        # 'bake_sale_1': {
        #     'display_title': 'Bake Sale!',
        #     'display_date': '9/20',
        #     'img_paths': [
        #         'events/img/carousel/fall19/bake_sale_1/flyer.png'
        #     ]
        # },
        #
        # 'meeting_1': {
        #     'display_title': 'First General Meeting',
        #     'display_date': '9/11',
        #     'img_paths': [
        #         'events/img/carousel/fall19/meeting_1/meeting_1_1.png',
        #     ]
        # },

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
