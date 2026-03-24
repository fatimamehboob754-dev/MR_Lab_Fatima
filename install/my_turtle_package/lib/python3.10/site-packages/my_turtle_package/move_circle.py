import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import time

class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        
        # Set a constant forward speed (m/s)
        msg.linear.x = 2.0  
        
        # Set a constant turning speed (rad/s)
        # Higher value = smaller circle; Lower value = larger circle
        msg.angular.z = 1.0 
        
        # Publish the command
        self.publisher_.publish(msg)
        
        # We don't need time.sleep() for a basic circle because 
        # the timer keeps sending these same values every 0.5s.
        self.get_logger().info('Publishing: Linear=%f, Angular=%f' % (msg.linear.x, msg.angular.z))
        
def main(args=None):
    rclpy.init(args=args)
    velocity_publisher = VelocityPublisher()
    rclpy.spin(velocity_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically 
    # when the garbage collector destroys the node object)
    velocity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()