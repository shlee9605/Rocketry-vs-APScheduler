import timeit
from rocket.connection import on_app_start as rocketry_start
from rocket.connection import on_app_shutdown as rocketry_stop
from aps.connection import on_app_start as apscheduler_start
from aps.connection import on_app_shutdown as apscheduler_stop

NUM_ITERATIONS = 1000

def test_rocketry():
    rocketry_start()
    for _ in range(NUM_ITERATIONS):
        pass  # do nothing, just run the scheduling code with Rocketry
    rocketry_stop()

def test_apscheduler():
    apscheduler_start()
    for _ in range(NUM_ITERATIONS):
        pass  # do nothing, just run the scheduling code with APScheduler
    apscheduler_stop()

rocketry_time = timeit.timeit(test_rocketry, number=1)
apscheduler_time = timeit.timeit(test_apscheduler, number=1)

print(f"Rocketry time: {rocketry_time}")
print(f"APScheduler time: {apscheduler_time}")
