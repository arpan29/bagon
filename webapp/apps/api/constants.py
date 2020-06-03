# import enum


# class Constants(enum.Enum):

#     APPLICATION_NAME = "BAGON"


PRICING = {
    "BIKE": [
        {
            "start": 0,
            "end": 7200,
            "rate": 20
        },
        {
            "start": 7201,
            "end": 14400,
            "rate": 15
        },
        {
            "start": 14401,
            "end": 18000,
            "rate": 10
        },
    ],
    "SUV": [
        {
            "start": 0,
            "end": 7200,
            "rate": 40
        },
        {
            "start": 7201,
            "end": 14400,
            "rate": 60
        },
    ],
    "HATCHBACK": [
        {
            "start": 0,
            "end": 7200,
            "rate": 60
        },
        {
            "start": 7201,
            "end": 14400,
            "rate": 80
        },
    ],
}