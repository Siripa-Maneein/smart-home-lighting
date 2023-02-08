from fastapi import APIRouter, Body, HTTPException
from config import database

router = APIRouter(prefix="/room", tags=["room"])
collection = database.client["exceed06"]["smart_home"]


@router.post("/manual/turn_on/{id}")
def turn_on_manually(id: int):
    # Change manual in the database of that room to On.
    if not 1 <= id <= 3:
        raise HTTPException(status_code=406, detail="id is out of range")
    collection.update_one(
        {"id": id, "mode": "manual", "status": False},
        {"$set": {"status": True}},
        upsert=False,
    )
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/manual/turn_off/{id}")
def turn_off_manually(id: int):
    # Change manual in the database of that room to Off.
    if not 1 <= id <= 3:
        raise HTTPException(status_code=406, detail="id is out of range")
    collection.update_one(
        {"id": id, "mode": "manual", "status": True},
        {"$set": {"status": False}},
        upsert=False,
    )
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/change_mode/{id}/{mode}/")
def change_mode(id: int, mode: str):
    # disables Manual button and change Auto in the database of that room to On.
    if not 1 <= id <= 3:
        raise HTTPException(status_code=406, detail="id is out of range")
    elif mode not in ["auto", "manual"]:
        raise HTTPException(status_code=406, detail="Mode is not acceptable")
    collection.update_one({"id": id}, {"$set": {"mode": mode}}, upsert=False)
    return collection.find_one({"id": id}, {"_id": 0})


@router.post("/change_brightness/{id}/{brightness}/")
def change_brightness(id: int, brightness: int):
    if not 1 <= id <= 3:
        raise HTTPException(status_code=406, detail="id is out of range")
    elif not 0 <= brightness <= 255:
        raise HTTPException(status_code=406, detail="Brightness is out of range")
    collection.update_one({"id": id}, {"$set": {"brightness": brightness}})
    return collection.find_one({"id": id}, {"_id": 0})


@router.get("/get_all_bulbs_info/")
def get_all_bulbs_info():
    # get all bulbs info
    result = {}
    for i in collection.find({}, {"_id": False}):
        result["room_" + str(i["id"])] = i
    return result


@router.get("/bulb_info/{id}")
def bulb_info(id: int):
    if not 1 <= id <= 3:
        raise HTTPException(status_code=406, detail="id is out of range")
    return collection.find_one({"id": id}, {"_id": 0})
