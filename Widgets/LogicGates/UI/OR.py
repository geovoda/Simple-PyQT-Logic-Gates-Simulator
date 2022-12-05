GATE = {
    "title": "Poarta AND",
    "width": 250,
    "height": 200,

    "terminals": [
        {
            "type": "INPUT",
            "x": 2,
            "y": 40 - 5,
        },

        {
            "type": "INPUT",
            "x": 2,
            "y": 160 - 5,
        },

        {
            "type": "OUTPUT",
            "x": 230,
            "y": 100 - 5,
        },
    ],

    "elements": [
        {
            "type": "arc",
            "x": 0,
            "y": 2,
            "height": 196,
            "width": 196,
            "start": -90 * 16,
            "size": 180 * 16,
        },

        {
            "type": "line",
            "x1": 100,
            "y1": 2,
            "x2": 50,
            "y2": 2,
        },

        {
            "type": "line",
            "x1": 50,
            "y1": 0,
            "x2": 50,
            "y2": 200,
        },

        {
            "type": "line",
            "x1": 50,
            "y1": 198,
            "x2": 100,
            "y2": 198,
        },

        {
            "type": "line",
            "x1": 0,
            "y1": 40,
            "x2": 50,
            "y2": 40,
        },

        {
            "type": "line",
            "x1": 0,
            "y1": 160,
            "x2": 50,
            "y2": 160,
        },

        {
            "type": "line",
            "x1": 200,
            "y1": 100,
            "x2": 240,
            "y2": 100,
        },
    ]
}
