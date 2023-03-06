from rocket.scheduleUtil import scheduler

async def on_app_start():
    await scheduler.start()

def on_app_shutdown():
    # scheduler.stop()
    print("finish")