from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'health!'

def start_server():
    def run():
        app.run(debug=True, use_reloader=False, host='0.0.0.0')  # use_reloader=False чтобы избежать запуска приложения дважды в режиме отладки

    flask_thread = threading.Thread(target=run)
    flask_thread.start()
    return flask_thread
