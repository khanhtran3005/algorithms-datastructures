from classes.printer import Printer
from classes.task import Task
from classes.queue import Queue
import random

def printerSimulation(numSeconds, ppm: int):
    printer = Printer(ppm)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not printer.isBusy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            printer.next(nextTask)

        printer.tick()

    averageWaitingTime = sum(waitingTimes) / len(waitingTimes)

    print("Average waiting time is {:.^14.2f} secs and {:.>5d} tasks remaining".format(averageWaitingTime, printQueue.size()))



def newPrintTask():
    num = random.randrange(1, 181)
    return num == 180

for i in range(10):
    printerSimulation(3600, "adsf")