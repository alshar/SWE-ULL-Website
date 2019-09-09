var genderData = {
  labels: ['Female', 'Male'],
  series: [97, 34]
};

var majorData = {
    labels: [
        'Chemical Engineering',
        'Electrical Engineering',
        'Computer Science',
        'Industrial Technology',
        'Civil Engineering',
        'Biology',
        'Mechanical Engineering',
        'Petroleum Engineering',
    ],
};

var options = {
  labelInterpolationFnc: function(value) {
    return value[0]
  }
};

var responsiveOptions = [
  ['screen and (min-width: 640px)', {
    chartPadding: 30,
    labelOffset: 100,
    labelDirection: 'explode',
    labelInterpolationFnc: function(value) {
      return value;
    }
  }],
  ['screen and (min-width: 1024px)', {
    labelOffset: 80,
    chartPadding: 20
  }]
];

new Chartist.Pie('#gender-chart', genderData, options, responsiveOptions);

new Chartist.Pie('#major-chart', data, options, responsiveOptions);