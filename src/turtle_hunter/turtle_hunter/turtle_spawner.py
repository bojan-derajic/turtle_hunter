#!/usr/bin/env python3
import rclpy
import numpy as np
from rclpy.node import Node
from turtlesim.srv import Spawn, Kill
from turtle_hunter_interfaces.msg import Turtle, TurtleArray
from turtle_hunter_interfaces.srv import CatchTurtle
from functools import partial


class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.declare_parameter("spawn_frequency", 0.25)
        self.declare_parameter("turtle_name_prefix", "target")

        self._spawn_frequency = self.get_parameter("spawn_frequency").value
        self._turtle_name_prefix = self.get_parameter(
            "turtle_name_prefix").value
        self._alive_turtles = []
        self._alive_turtles_publisher = self.create_publisher(
            TurtleArray, "alive_turtles", 10)
        self._spawn_counter = 0
        self._spawn_timer = self.create_timer(
            1/self._spawn_frequency, self._call_spawn_service_callback)
        self._catch_turtle_service = self.create_service(CatchTurtle, "catch_turtle", self._catch_turtle_callback)

        self.x_lim = [0.0, 10.0]
        self.y_lim = [0.0, 10.0]
        self.get_logger().info("Turtle Spawner node successfully created")

    def _call_spawn_service_callback(self):
        turtle_x = self.x_lim[0] + \
            (self.x_lim[1] - self.x_lim[0])*np.random.rand()
        turtle_y = self.y_lim[0] + \
            (self.y_lim[1] - self.y_lim[0])*np.random.rand()
        turtle_theta = -np.pi + 2*np.pi*np.random.rand()
        turtle_name = self._turtle_name_prefix + "_" + str(self._spawn_counter)

        spawn_request = Spawn.Request()
        spawn_request.x = turtle_x
        spawn_request.y = turtle_y
        spawn_request.theta = turtle_theta
        spawn_request.name = turtle_name

        spawn_client = self.create_client(Spawn, "spawn")
        while not spawn_client.wait_for_service():
            self.get_logger().warn("Waiting for the server...")
        future = spawn_client.call_async(spawn_request)
        future.add_done_callback(
            partial(self._spawn_service_response_callback, spawn_request=spawn_request))

    def _spawn_service_response_callback(self, future, spawn_request):
        try:
            response = future.result()
            self.get_logger().info(
                "Target turtle with name {} successfully spawned.".format(response.name))

            spawned_turtle = Turtle()
            spawned_turtle.name = spawn_request.name
            spawned_turtle.x = spawn_request.x
            spawned_turtle.y = spawn_request.y

            self._alive_turtles.append(spawned_turtle)
            self._spawn_counter += 1

            alive_turtles_msg = TurtleArray()
            alive_turtles_msg.alive_turtles = self._alive_turtles
            self._alive_turtles_publisher.publish(alive_turtles_msg)

        except Exception as e:
            self.get_logger().error("Spawn service call failed %r" % (e,))

    def _catch_turtle_callback(self, request, response):
        for turtle in self._alive_turtles:
            if request.name == turtle.name:
                kill_client = self.create_client(Kill, "kill")
                while not kill_client.wait_for_service(1.0):
                    self.get_logger().warn("Waiting for the server...")
                kill_request = Kill.Request()
                kill_request.name = turtle.name
                kill_client.call_async(kill_request)

                self._alive_turtles.remove(turtle)
                alive_turtles_msg = TurtleArray()
                alive_turtles_msg.alive_turtles = self._alive_turtles
                self._alive_turtles_publisher.publish(alive_turtles_msg)
                response.success = True
        response.success = False
        return response

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()
