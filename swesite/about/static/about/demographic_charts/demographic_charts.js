var majorData = {};


new Chartist.Pie('#gender-chart',
    {
        labels: ['Female', 'Male'],
        series: [97, 34]
    },
    {
        donut: true,
        donutWidth: 40
    }
);

new Chartist.Bar('#major-chart',
    {
        labels: [
            'Chemical Engineering',
            'Mechanical Engineering',
            'Electrical Engineering',
            'Other',
        ],
        series: [24, 4, 4, 2]
    },
    {
        distributeSeries: true
    }
);