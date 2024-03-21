from .task import Task


class Printer:
    def __init__(self, ppm: int):
        self.ppm = ppm
        self.currentTask = None
        self.remainingTime = 0

    def tick(self):
        if self.currentTask != None:
            self.remainingTime -= 1  # each second has passed
            if self.remainingTime <= 0:
                self.currentTask = None

    def isBusy(self):
        return self.currentTask != None

    def next(self, newTask: Task):
        self.currentTask = newTask
        self.remainingTime = newTask.getPages() * 60 / self.ppm
