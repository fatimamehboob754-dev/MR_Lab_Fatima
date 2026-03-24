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
        
        # Move in a triangle (3 sides)
        for i in range(3):
            self.get_logger().info('Moving Side %d' % (i + 1))
            
            # 1. Move Forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(2.0) # Adjust this for longer/shorter sides

            # 2. Stop briefly
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.5)

            # 3. Turn 120 degrees (Equilateral Triangle)
            # Formula: 2 * pi / 3 = 2.094 radians
            msg.angular.z = 2.094 
            self.publisher_.publish(msg)
            time.sleep(1.0) # Adjust this to ensure the turn completes

            # 4. Stop rotation before next side
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.5)
            
        self.get_logger().info('Triangle Complete!')
        
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