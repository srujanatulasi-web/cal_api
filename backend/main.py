from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from supabase import create_client
from pydantic import BaseModel

app = FastAPI()
db = create_client("https://kajnhfsqosyosolonsur.supabase.co","sb_publishable__C7fO36RaHklFgPGdTYFqg_sOjKHPGz")
 
class Room(BaseModel):
    floor: int
    price: int
    is_booked: bool

class UpdateRoom(BaseModel):
    floor: int
    price: int
    is_booked: bool

@app.get("/")
def home(request: Request):
    return 'A Simple Booking API'
 
@app.get('/rooms')
def get_rooms(request: Request): 
    rooms = db.table('rooms').select('*').execute()
    rooms = rooms.data
    return JSONResponse(rooms)
 
@app.get('/rooms/{room_id}')
def get_room_by_id(request: Request, room_id):
    rooms = db.table('rooms').select('*').eq('id', room_id).execute()
    rooms = rooms.data 
    return JSONResponse(rooms) 

@app.post('/rooms/add')
async def create_room(room: Room):
    try:
        data = room.model_dump()
        res = db.table('rooms').insert(data).execute()
        print("RESULT:", res)
        return {"data": res.data}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    

@app.delete('/rooms/delete/{room_id}')
async def delete_room( room_id:int):
    db.table('rooms').delete().eq('id',room_id).execute()
    return "deleted successfully"

@app.put('/rooms/update/{room_id}') 
async def update_room(room_id: int,room: UpdateRoom):
    try:
        data = room.model_dump()
        res = db.table('rooms').update(data).eq('id', room_id).execute()
        print("UPDATE RESULT:", res)
        
        if res.data:
            return {"message": "Room updated successfully", "data": res.data}
        else:
            return {"message": "No row updated"}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}