# Remove messages from queues and copy to file
#!/usr/bin/python3
import os
import clr

clr.AddReference('System.Messaging')
from System.Messaging import MessageQueue
from System.Messaging import Message

clr.AddReference('System.IO')
from System.IO import StreamReader

clr.AddReference('System')
from System import TimeSpan

from datetime import datetime

# Variable to control script
path = "C:\\Users\\pf-psarmento\\Documents\\Visual Studio 2017\\Projects\\"
queueNameInSucess = ".\\private$\\baggagetty_ok"
queueNameEngineSucess = ".\\private$\\baggageengine_ok"
path = path + datetime.now().strftime('%Y-%m-%d')
if not os.path.isdir(path):
    os.mkdir(path)
path = path + "\\"
if not MessageQueue.Exists(queueNameInSucess):
    queue = MessageQueue.Create(queueNameInSucess)
else:
    queue = MessageQueue(queueNameInSucess)
try:
    msg = queue.Receive(TimeSpan.FromSeconds(2))
except:
    msg = None
print ("QueueIn cleanning will start")
while msg is not None:
    queueProcessedPath = path + "TTY " + msg.Label.replace(":", " ") + " "  + datetime.now().strftime('%Y-%m-%d %H.%M.%S.%f')  + ".rcv"
    print ("Path: ",queueProcessedPath)
    ttyFile = open(queueProcessedPath,'w')
    sr = StreamReader(msg.BodyStream)
    ttyFile.write(sr.ReadToEnd())
    ttyFile.close()
    try:
        msg = queue.Receive(TimeSpan.FromSeconds(2))
    except:
        msg = None
queue.Close()
print ("QueueIn cleanning finnish")
if not MessageQueue.Exists(queueNameEngineSucess):
    queue = MessageQueue.Create(queueNameEngineSucess)
else:
    queue = MessageQueue(queueNameEngineSucess)
print ("QueueEngine cleanning will start")
msg = queue.Purge()
print ("QueueEnine cleanning finnish")
