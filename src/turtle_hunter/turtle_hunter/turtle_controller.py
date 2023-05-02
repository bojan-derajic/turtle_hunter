#!/usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtle_hunter_interfaces.msg import Turtle, TurtleArray
from turtle_hunter_interfaces.srv import CatchTurtle


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.declare_parameter("catch_closest_turtle_first", True)
        self.declare_parameter("Kp_lin", 0.5)
        self.declare_parameter("Kp_ang", 4.0)
        self.declare_parameter("eps", 0.1)

        self._pose_subscriber = self.create_subscription(
            Pose, "turtle1/pose", self._pose_callabck, 10)
        self._alive_turtles_subscriber = self.create_subscription(
            TurtleArray, "alive_turtles", self._alive_turtles_callback, 10)
        self._cmd_vel_publisher = self.create_publisher(
            Twist, "turtle1/cmd_vel", 10)

        self.target_point = []
        self.target_name = ""
        self.current_point = []
        self.catch_closest_turtle_first = self.get_parameter(
            "catch_closest_turtle_first").value
        self.Kp_lin = self.get_parameter("Kp_lin").value
        self.Kp_ang = self.get_parameter("Kp_ang").value
        self.eps = self.get_parameter("eps").value

        self.get_logger().info("Turtle Hunter node successfully created")

    def _pose_callabck(self, pose_msg):
        self.current_point = np.array([pose_msg.x, pose_msg.y])
        if len(self.target_point) > 0:
            err_lin = np.linalg.norm(self.target_point - self.current_point)
            if err_lin >= self.eps:
                lin_vel = self.Kp_lin * err_lin

                current_angle = pose_msg.theta
                target_angle = np.arctan2(self.target_point[1] - self.current_point[1],
                                          self.target_point[0] - self.current_point[0])
                err_ang = target_angle - current_angle
                if err_ang > np.pi:
                    err_ang -= 2*np.pi
                elif err_ang < -np.pi:
                    err_ang += 2*np.pi
                ang_vel = self.Kp_ang * err_ang

                cmd_vel_msg = Twist()
                cmd_vel_msg.linear.x = lin_vel
                cmd_vel_msg.angular.z = ang_vel
                self._cmd_vel_publisher.publish(cmd_vel_msg)
            else:
                catch_turtle_client = self.create_client(CatchTurtle, "catch_turtle")
                while not catch_turtle_client.wait_for_service(1.0):
                    self.get_logger().warn("Waiting for the server...")
                catch_turtle_request = CatchTurtle.Request()
                catch_turtle_request.name = self.target_name
                catch_turtle_client.call_async(catch_turtle_request)

    def _alive_turtles_callback(self, alive_turtles_msg):
        if len(alive_turtles_msg.alive_turtles) > 0:
            if self.catch_closest_turtle_first and len(alive_turtles_msg.alive_turtles) > 1:
                next_target_turtle = self._find_closest_turtle(
                    alive_turtles_msg.alive_turtles)
            else:
                next_target_turtle = alive_turtles_msg.alive_turtles[0]

            self.target_point = np.array(
                [next_target_turtle.x, next_target_turtle.y])
            self.target_name = next_target_turtle.name
        else:
            self.target_point = []

    def _find_closest_turtle(self, alive_turtles_array):
        closest_turtle = alive_turtles_array[0]
        closest_turtle_point = np.array(
            [closest_turtle.x, closest_turtle.y])
        min_distance = np.linalg.norm(self.current_point - closest_turtle_point)
        for turtle in alive_turtles_array[1:]:
            turtle_point = np.array([turtle.x, turtle.y])
            distance = np.linalg.norm(self.current_point - turtle_point)
            if distance < min_distance:
                closest_turtle = turtle
                min_distance = distance
        return closest_turtle


def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
