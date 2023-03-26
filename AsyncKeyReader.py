#Appears that I will only need to use startReading and stopReading after importing

#Shamelessly stolen from Stack Overflow answer at https://stackoverflow.com/questions/13207678/whats-the-simplest-way-of-detecting-keyboard-input-in-a-script-from-the-termina
#Importing necessary modules to capture keypress events
import threading
from win32api import STD_INPUT_HANDLE
from win32console import GetStdHandle, KEY_EVENT, ENABLE_ECHO_INPUT, ENABLE_LINE_INPUT, ENABLE_PROCESSED_INPUT

#Q: Not sure why this is wrapped in a class
class KeyAsyncReader():
    def __init__(self):
        #Calls the Lock factory method from threading module to assign most appropriate type of lock
        self.stopLock = threading.Lock()
        self.stopped = True
        #Q: Not sure what this is for, perhaps I'm supposed to set this
        self.capturedChars = ""

        #Interesting style, a blank line was placed between the attributes and the methods
        #This gets the STD_INPUT_HANDLE which defaults to CONIN$ meaning the Console Input Device (or keyboard and mouse)
        self.readHandle = GetStdHandle(STD_INPUT_HANDLE)
        #The pipe here is probably binary OR operator, not a SET UNION operator
        #This intercepts carriage returns, keyboard input, and (in addition to carriage returns) backspaces and new lines
        self.readHandle.SetConsoleMode(ENABLE_LINE_INPUT|ENABLE_ECHO_INPUT|ENABLE_PROCESSED_INPUT)



    def startReading(self, readCallback):
        self.stopLock.acquire()

        #Q: Why is this try-except block separated by a blank line? Is this the common formatting convention?
        try:
            #Q: What would cause self.stopped to be set to false? My only guess is so it isn't called twice, but why would that happen?
            if not self.stopped:
                raise Exception("Capture is already going")

            self.stopped = False
            #Q: Why is this defined for the first time here instead of being set to blank in the init function
            #Q: Not sure what readCallback here refers to, I think of callback as a function that calls a function, so which function is called here?
            self.readCallback = readCallback

            backgroundCaptureThread = threading.Thread(target=self.backgroundThreadReading)
            #Daemonic threads are stopped abruptly at shutdown
            backgroundCaptureThread.daemon = True
            backgroundCaptureThread.start()
        except:
            self.stopLock.release()
            raise

        self.stopLock.release()


    def backgroundThreadReading(self):
        curEventLength = 0
        while True:
            eventsPeek = self.readHandle.PeekConsoleInput(10000)

            self.stopLock.acquire()
            if self.stopped:
                self.stopLock.release()
                return
            self.stopLock.release()


            if len(eventsPeek) == 0:
                continue

            if not len(eventsPeek) == curEventLength:
                if self.getCharsFromEvents(eventsPeek[curEventLength:]):
                    self.stopLock.acquire()
                    self.stopped = True
                    self.stopLock.release()
                    break

                curEventLength = len(eventsPeek)



    def getCharsFromEvents(self, eventsPeek):
        callbackReturnedTrue = False
        for curEvent in eventsPeek:
            if curEvent.EventType == KEY_EVENT:
                    if ord(curEvent.Char) == 0 or not curEvent.KeyDown:
                        pass
                    else:
                        curChar = str(curEvent.Char)
                        if self.readCallback(curChar) == True:
                            callbackReturnedTrue = True
        return callbackReturnedTrue

    def stopReading(self):
        self.stopLock.acquire()
        self.stopped = True
        self.stopLock.release()