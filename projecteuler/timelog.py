import sys, time 

global currentTime
global runtime
global isStarted


def start():
    currentTime = time.time()
    isStarted = True


def end():
    if isStarted:
        runtime = time.time() - currentTime()
        isStarted = False
    else: 
        runtime = 0 


def getRuntime():
    return runtime


def log():
    print("Total runtime %s" % runtime)


