require.config({
    baseUrl: '/assets/js',
    paths : {
        'jquery': 'lib/jquery-1.11.1.min',
        'retina': 'lib/retina.min'
    }
});

// uncomment for vertical type grid.
// require(['site', 'design']);
require(['site']);