def fall_19(request):
    context = {
        # 'bake_sale_1': {
        #     'display_title': 'Upcoming Events',
        #     'display_date': 'See Flyer for Dates',
        #     'img_paths': [
        #         'events/img/carousel/fall19/bake_sale_1/flyer.png',
        #     ]
        # },
        'bake_sale_1': {
            'display_title': 'Bake Sale',
            'display_date': '9/20/19',
            'img_paths': [
                'events/img/carousel/fall19/bake_sale_1/bs_1.JPG',
                'events/img/carousel/fall19/bake_sale_1/bs_2.JPG'
            ]
        },

        'meeting_1': {
            'display_title': 'First General Meeting',
            'display_date': '9/11/19',
            'display_description': '',
            'img_paths': [
                'events/img/carousel/fall19/meeting_1/m_5.jpg',
                'events/img/carousel/fall19/meeting_1/m_1.JPG',
                'events/img/carousel/fall19/meeting_1/m_2.JPG',
                'events/img/carousel/fall19/meeting_1/m_3.JPG',
                'events/img/carousel/fall19/meeting_1/m_4.JPG',


            ]
        },

        'les_bbq': {
            'display_title': 'Louisiana Engineering Society BBQ',
            'display_date': '9/6/19',
            'img_paths': [
                'events/img/carousel/fall19/les_bbq/les_bbq_1.JPG',
                'events/img/carousel/fall19/les_bbq/les_bbq_2.JPG',

            ]
        }

    }

    return context
