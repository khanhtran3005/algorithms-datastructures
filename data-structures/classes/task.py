import random


class Task:
    def __init__(self, timestamp: int):
        self.timestamp = timestamp
        self.pages = random.randrange(1, 21)

    def getTimestamp(self) -> int:
        return self.timestamp

    def getPages(self) -> int:
        return self.pages

    def waitTime(self, currentTime: int) -> int:
        return currentTime - self.timestamp
