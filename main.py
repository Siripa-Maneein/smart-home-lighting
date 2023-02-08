from fastapi import FastAPI
from routing import routing_room
from config import database

collection = database.client["exceed06"]["smart_home"]

app = FastAPI()
app.include_router(routing_room.router)


@app.get("/")
def root():
    return {"smart_home": "welcome to smart home group 6"}


@app.get("/initial")
def reset():
    collection.delete_many({})
    room_name = ["Kitchen", "Lounge", "Master_Bedroom"]
    mode = ["manual", "manual", "auto"]
    all_room = []
    for i in range(3):
        dic = {}
        dic["id"] = i + 1
        dic["room_name"] = room_name[i]
        dic["brightness"] = 0
        dic["status"] = False
        dic["mode"] = mode[i]
        all_room.append(dic)
    collection.insert_many(all_room)
    return {"status": "initial complete"}
