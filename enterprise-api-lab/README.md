# 🚀 Enterprise API Lab

This project demonstrates a simple **enterprise-style application architecture** with:

- Frontend (GUI)
- Backend API
- Dynamic Authentication (JWT)
- Request Tracking (UUID)

---

# 🏗️ Architecture Overview
User (Browser)
↓
Frontend (GUI) - 172.20.2.35
↓ HTTP Requests
Backend API - 172.20.2.18


---

# 🔐 Authentication Flow (JWT)

1. User clicks **Login** from GUI
2. GUI sends request to backend `/login`
3. Backend generates a **JWT token**
4. Token is returned and stored in GUI
5. GUI sends token in every request


POST /login → returns JWT
POST /process → requires JWT


---

# 🧾 Request Tracking (UUID)

Each API request generates a **unique UUID**:

- Helps track requests
- Useful for debugging and logging
- Simulates real enterprise tracing systems

Example response:

```json
{
  "message": "Hello Fares",
  "request_number": 3,
  "request_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

🔄 Application Flow
```json
1. Login → Get JWT token
2. Send request with token
3. Backend validates token
4. Backend processes request
5. Backend generates UUID
6. Response returned to GUI
```
🧠 Key Concepts
✅ JWT (Authentication)
Identifies the user
Signed and secure
Has expiration time
✅ UUID (Request ID)
Unique per request
Used for tracing and logging
Not used for authentication
📂 Project Structure
```json
enterprise-api-lab/
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── style.css
│
└── README.md
```
▶️ How to Run
🔵 Backend
```json
cd backend
pip install -r requirements.txt
python app.py
```
Backend will run on:
```json
http://172.20.2.18:5000
```
🟢 Frontend

Open in browser:
```json
frontend/index.html
```
🧪 Features
🔐 Login with JWT
🔒 Protected API endpoint
🔢 Request counter
🧾 UUID per request
🌐 CORS enabled for cross-server communication
🛡️ Security Notes
JWT is used for authentication
UUID is used for tracking (not security)
This is a lab environment, not production-ready
