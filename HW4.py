from threading import Thread, Lock

mutex = Lock()

#The can message is variable based on the file used. In the case that it is drawn from an excel file, we would use the pandas library and the .ExcelFile() to read files.
CAN_message_1= [0x01, 0x40, 0x00, 0x00, 0x00]

#this is the first method which allows one the decoding of one can message
def CANDecode():

  #locks the method such that it can only be run during the threading
  mutex.acquire()

  #mask the first two bits
  CAN_message_1[0] = CAN_message_1[0] & 0x3f
  
  #bit shifts
  decoded = (CAN_message_1[0] << 3) + (CAN_message_1[1] >> 5)
  print(decoded)
  
  mutex.release()

#Second decode method to be threaded
def CANUpdate():
  
  #locks the method such that it can only be run during the threading
  mutex.acquire()

  CAN_message_1[1] = CAN_message_1[1] + 10
  mutex.release()


#thread the messages
th_CANDecode  = Thread(target=CANDecode)
th_CANUpdate  = Thread(target=CANUpdate)

#start the threads
th_CANDecode.start()
th_CANUpdate.start()


