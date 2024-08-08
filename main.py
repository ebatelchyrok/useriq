from app import app
from schedule import jobs, scheduler
from server import start_server


def main ():
    jobs()
    scheduler.start()
    start_server()
    app.run()

if __name__ == "__main__":
    main ()
