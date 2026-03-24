import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class MoveToGoal(Node):
    def __init__(self):
        super().__init__('move_to_goal')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        # We must subscribe to the Pose to know where we are!
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.update_pose, 10)
        self.pose = Pose()
        self.timer = self.create_timer(0.1, self.move_turtle)
        
        # Define your target location here
        self.target_x = 2.0
        self.target_y = 2.0

    def update_pose(self, data):
        self.pose = data

    def move_turtle(self):
        msg = Twist()
        
        # 1. Calculate distance to goal
        distance = math.sqrt((self.target_x - self.pose.x)**2 + (self.target_y - self.pose.y)**2)
        
        # 2. Calculate angle to goal (using atan2)
        angle_to_goal = math.atan2(self.target_y - self.pose.y, self.target_x - self.pose.x)
        angle_error = angle_to_goal - self.pose.theta

        # 3. Simple Control Logic
        if distance > 0.1:
            # If the angle is wrong, turn first
            if abs(angle_error) > 0.1:
                msg.angular.z = 1.0 * angle_error
                msg.linear.x = 0.0
            else:
                # If facing the right way, move forward
                msg.linear.x = 1.5
                msg.angular.z = 0.0
        else:
            # Stop when reached
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info("Goal Reached!")

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MoveToGoal()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()