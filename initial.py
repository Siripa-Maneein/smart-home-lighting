from config import database

collection = database.client["exceed06"]["smart_home"]

collection.delete_many({})

all_room = [
    {"id": 1, "room_name": "Kitchen", "brightness": 0, "status": False, "mode": "auto"},
    {
        "id": 2,
        "room_name": "Lounge",
        "brightness": 0,
        "status": False,
        "mode": "manual",
    },
    {
        "id": 3,
        "room_name": "Master_Bedroom",
        "brightness": 0,
        "status": False,
        "mode": "manual",
    },
]

collection.insert_many(all_room)
