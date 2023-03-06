import asyncio
from rocketry import Rocketry

class Scheduler:
    def __init__(self):
        self.app = Rocketry(execution="async")

        async def do_things():
            print("hello world")

        self.app.task('every 5 seconds')(do_things)

    async def loop(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.app.session.start)

    async def start(self):
        asyncio.create_task(self.loop())

    # def stop(self):
    #     self.app.session.stop()
    #     print("stop")

scheduler = Scheduler()