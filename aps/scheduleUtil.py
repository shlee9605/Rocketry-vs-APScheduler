from apscheduler.schedulers.background import BackgroundScheduler

class Scheduler:
    def __init__(self):
        self.sched = BackgroundScheduler()

    def scheduled_job(self):
        # Code for the job you want to schedule
        print("Scheduled job is running")

    def start(self):
        self.scheduled_job()
        self.sched.add_job(self.scheduled_job, 'interval', seconds=5)
        self.sched.start()

    # def stop(self):
    #     self.sched.shutdown()

scheduler = Scheduler()