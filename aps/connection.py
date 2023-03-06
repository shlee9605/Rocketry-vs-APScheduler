from aps.scheduleUtil import scheduler

async def on_app_start():
    scheduler.start()


async def on_app_shutdown():
    # scheduler.stop()
    print("close")
