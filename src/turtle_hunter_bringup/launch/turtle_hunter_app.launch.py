from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="simulator"
    )
    turtle_controller_node = Node(
        package="turtle_hunter",
        executable="turtle_controller",
        name="master",
        parameters=[
            {"catch_clocest_first": True},
            {"Kp_lin": 2.0},
             {"Kp_ang": 6.0},
             {"eps": 0.1}
        ]
    )
    turtle_spawner_node = Node(
        package="turtle_hunter",
        executable="turtle_spawner",
        name="spawner",
        parameters=[
            {"spawn_frequency": 0.25},
            {"turtle_name_prefix": "target_turtle"}
        ]
    )

    ld = LaunchDescription()
    ld.add_action(turtlesim_node)
    ld.add_action(turtle_controller_node)
    ld.add_action(turtle_spawner_node)
    return ld