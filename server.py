from flask import Flask, render_template
from flask_socketio import SocketIO, send
from serial import Serial

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
    if msg == 'trigger':
        ser.write(("a").encode('raw_unicode_escape'))
        x = ser.readline()
        print(x)

if __name__ == '__main__':
    ser = Serial("COM4", 9600)
    x = ser.readline()
    print(x)
    socketio.run(app, host='0.0.0.0')
