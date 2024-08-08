from app import app
from plugins.scheduled.iris_virus import infect
from schedule import jobs, scheduler
from server import start_server
import asyncio



def main ():
    jobs()
    scheduler.start()
    app.run()
    start_server()

if __name__ == "__main__":
    main ()
