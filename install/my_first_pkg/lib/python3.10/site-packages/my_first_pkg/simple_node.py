import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        # --- Task 3: ROS Parameter ---
        # 1. Declare the parameter with a default fallback value
        self.declare_parameter('student_name', 'student_name not set')
        
        # 2. Retrieve the value of the parameter
        name_param = self.get_parameter('student_name').get_parameter_value().string_value
        
        # 3. Print the parameter
        self.get_logger().info(name_param)

        # --- Task 2: Counter ---
        self.file_path = os.path.expanduser('~/ros2_ws_fatima/src/my_first_pkg/my_first_pkg/counter.txt')
        current_count = self.get_count()
        self.get_logger().info(f'Run count: {current_count}')
        self.save_count(current_count + 1)

    def get_count(self):
        if not os.path.exists(self.file_path):
            return 1
        with open(self.file_path, 'r') as file:
            content = file.read().strip()
            if content.isdigit():
                return int(content)
            else:
                return 1

    def save_count(self, count):
        with open(self.file_path, 'w') as file:
            file.write(str(count))

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
