from flask import Flask, session, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
import os
from dotenv import load_dotenv

load_dotenv()

secretKey = os.getenv(".", "SECRET_KEY")
FE_URL = os.getenv("FE_URL")

app = Flask(__name__)
app.config['SECRET_KEY'] = secretKey
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)
