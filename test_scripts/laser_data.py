import rospy
from sensor_msgs.msg import LaserScan

def ls_cb(msg):
    print(len(msg.ranges))

rospy.init_node("laser_scan_sub")
laser_sub = rospy.Subscriber("/vrep/scan", LaserScan, ls_cb)

rospy.spin()