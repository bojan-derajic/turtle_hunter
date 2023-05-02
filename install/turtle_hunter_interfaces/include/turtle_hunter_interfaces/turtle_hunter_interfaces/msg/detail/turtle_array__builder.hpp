// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtle_hunter_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
#define TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtle_hunter_interfaces/msg/detail/turtle_array__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtle_hunter_interfaces
{

namespace msg
{

namespace builder
{

class Init_TurtleArray_alive_turtles
{
public:
  Init_TurtleArray_alive_turtles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::turtle_hunter_interfaces::msg::TurtleArray alive_turtles(::turtle_hunter_interfaces::msg::TurtleArray::_alive_turtles_type arg)
  {
    msg_.alive_turtles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_hunter_interfaces::msg::TurtleArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_hunter_interfaces::msg::TurtleArray>()
{
  return turtle_hunter_interfaces::msg::builder::Init_TurtleArray_alive_turtles();
}

}  // namespace turtle_hunter_interfaces

#endif  // TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__BUILDER_HPP_
