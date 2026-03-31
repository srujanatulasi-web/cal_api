# Room Booking Application
 This is a full-stack Room Booking Application built using **FastAPI**(backend)and **streamlit**(frontend).it allows users to create,view,update,and manage room bookings
 ## Features
 -View all rooms
 -Create new room
 -Update room details
 -Book/unbook rooms
 -simple UI using Stremlit

 ---
 ## Tech Stack
 -Python
 -FastAPI
 -Streamlit
 -Supabase

 ---
 ## Project Structure
 room_booking_app/
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── main.py
│
└── README.md

---
## How to Run
### 1.Run Backend
```bash
cd backend
uvicorn main:app --reload
```
👉Backend runs at:
http://127.0.0.1:8000

---
### 2.Run Frontend
```bash
cd frontend
streamlit run main.py
```
---
## API Testing (Swagger UI)
You can test all API endpoints using FastAPI's built-in interactive docs.

👉open in browser:
http://127.0.0.1:8000/docs
 ## API Endpoints
 -GET/rooms → Get all rooms
 -POST/rooms/add → Add new room
 -PUT/rooms/update → Update room
 -DELETE/rooms/delete → Delete room

 ## Project Description
 This project demonstrates how to build a full-stack application using FastAPI and stramlit with a realtime database(supabase)

 ---
 ## Author
 Srujana Tulasi
