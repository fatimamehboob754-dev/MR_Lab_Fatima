import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class MultiTurtlePublisher(Node):
    def __init__(self):
        super().__init__('multi_turtle_publisher')
        
        # Publishers for each turtle
        self.pub1 = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        
        # High frequency timer (10Hz) for smooth control
        self.timer_period = 0.1 
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        self.elapsed_time = 0.0

    def timer_callback(self):
        self.elapsed_time += self.timer_period
        
        # --- TURTLE 1: PERFECT CIRCLE ---
        # Constant velocity creates a stable circle in one spot
        c_msg = Twist()
        c_msg.linear.x = 1.0
        c_msg.angular.z = 1.0
        self.pub1.publish(c_msg)

        # --- TURTLE 2: SQUARE (4-second cycle per side) ---
        s_msg = Twist()
        s_cycle = self.elapsed_time % 4.0 
        if s_cycle < 1.5:
            s_msg.linear.x = 1.0   # Move Forward for 1.5s
        elif s_cycle < 2.5:
            s_msg.angular.z = 1.5708 # Turn 90 deg (pi/2) for 1s
        else:
            s_msg.linear.x = 0.0   # Full Stop for 0.5s to stabilize
            s_msg.angular.z = 0.0
        self.pub2.publish(s_msg)

        # --- TURTLE 3: TRIANGLE (4-second cycle per side) ---
        t_msg = Twist()
        t_cycle = self.elapsed_time % 4.0
        if t_cycle < 1.5:
            t_msg.linear.x = 1.0   # Move Forward for 1.5s
        elif t_cycle < 2.5:
            t_msg.angular.z = 2.0944 # Turn 120 deg (2pi/3) for 1s
        else:
            t_msg.linear.x = 0.0   # Full Stop for 0.5s to stabilize
            t_msg.angular.z = 0.0
        self.pub3.publish(t_msg)

def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtlePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()