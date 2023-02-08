from fastapi import APIRouter, Body, HTTPException
from config import database

router = APIRouter(prefix="/room", tags=["room"])
collection = database.client["exceed06"]["smart_home"]


@router.post("/manual/turn_on/{id}")
def turn_on_manually(id: int):
    # Change manual in the database of that room to On.
    collection.update({{"id": id, "mode": "manual"}, {"status": True}}, upsert=False)


@router.post("/manual/turn_off/{id}")
def turn_off_manually(id: int):
    # Change manual in the database of that room to Off.
    collection.update({"id": id, "mode": "manual"}, {"status": False}, upsert=False)


@router.post("/change_status/{id}/{mode}/")
def change_mode(id: int, mode: str):
    # disables Manual button and change Auto in the database of that room to On.
    collection.update({"id": id}, {"mode": mode}, upsert=False)


@router.post("/change_state/{id}/{brightness}/")
def change_brightness(id: int, brightness: int):
    collection.update({"id": id}, {"brightness": brightness})


@router.get("/get_all_bulb_info/")
def get_all_bulbs_info():
    result = []
    for i in collection.find({}, {"_id": False}):
        result.append(i)
    return {"result": result}
