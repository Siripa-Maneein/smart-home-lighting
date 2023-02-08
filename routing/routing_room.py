from fastapi import APIRouter, Body, HTTPException
from config import database

router = APIRouter(prefix="/room", tags=["room"])
collection = database.client["exceed06"]["smart_home"]


@router.post("/manual/turn_on/{id}")
def turn_on_manually(id: int):
    """Set status of bulb with given id to True."""
    collection.update_one(
        {"id": id, "mode": "manual", "status": False},
        {"$set": {"status": True}},
        upsert=False,
    )
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/manual/turn_off/{id}")
def turn_off_manually(id: int):
    """Set status of bulb with given id to False."""
    collection.update_one(
        {"id": id, "mode": "manual", "status": True},
        {"$set": {"status": False}},
        upsert=False,
    )
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/change_mode/{id}/{mode}/")
def change_mode(id: int, mode: str):
    """Set Mode of bulb with that id to the given mode ('auto'/ 'manual')."""
    collection.update_one({"id": id}, {"$set": {"mode": mode}}, upsert=False)
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/change_brightness/{id}/{brightness}/")
def change_brightness(id: int, brightness: int):
    """Set brightness of bulb with that id to the given brightness."""
    collection.update_one({"id": id}, {"$set": {"brightness": brightness}})
    return collection.find_one({"id": id}, {"_id": 0})


@router.get("/get_all_bulbs_info/")
def get_all_bulbs_info():
    """Return information about all light bulbs"""
    result = {}
    for i in collection.find({}, {"_id": False}):
        result["room_" + str(i["id"])] = i
    return result
