from app import app
from plugins.scheduled.iris_virus import infect
from schedule import jobs, scheduler
from server import start_server
import asyncio



def main ():
    jobs()
    scheduler.start()
    start_server()
    app.run()

if __name__ == "__main__":
    main ()
