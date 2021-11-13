#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import sys, select
import tty, termios

msg = """
Control Your TurtleBot3!
---------------------------
Moving around:
        w
   a    s    d

w : drive
a/d : turn left or right
space key, s : force stop
CTRL-C to quit
"""

e = """
Communications Failed
"""

def getKey():
  tty.setraw(sys.stdin.fileno())
  rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
  if rlist:
      key = sys.stdin.read(1)
  else:
      key = ''

  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
  return key

if __name__=="__main__":
  settings = termios.tcgetattr(sys.stdin)

  rospy.init_node('teleop_key')
  pub = rospy.Publisher('teleop_key', Int32, queue_size=1)

  status = 0

  try:
    print(msg)
    while(1):
      key = getKey()
      if key == 'w' :
        status = status + 1
        number = 1
        pub.publish(number)
        print("Drive!")
      elif key == 'a' :
        status = status + 1
        number = 2
        pub.publish(number)
        print("Turn Left!")
      elif key == 's' :
        status = status + 1
        number = 3
        pub.publish(number)
        print("Stop!")
      elif key == 'd' :
        status = status + 1
        number = 4
        pub.publish(number)
        print("Turn Right!")
      elif key == ' ' :
        status = status + 1
        number = 5
        pub.publish(number)
        print("Sit down!")
      elif key == 'r' :
        status = status + 1
        number = 6
        pub.publish(number)
        print("Motor Reboot!")
      else:
        if (key == '\x03'):
          break

        if status == 20 :
          print(msg)
          status = 0

  except:
    print(e)

  termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)