cmake_minimum_required(VERSION 3.0.2)
project(teleop_key)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  rospy
)

catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES teleop_key
  CATKIN_DEPENDS std_msgs rospy
  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#catkin_install_python(PROGRAMS
#  teleop_key.py
#  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
