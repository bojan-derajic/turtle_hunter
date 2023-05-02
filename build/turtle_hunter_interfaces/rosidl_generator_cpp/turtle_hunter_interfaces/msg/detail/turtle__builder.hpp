// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from turtle_hunter_interfaces:msg/Turtle.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
#define TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "turtle_hunter_interfaces/msg/detail/turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace turtle_hunter_interfaces
{

namespace msg
{

namespace builder
{

class Init_Turtle_y
{
public:
  explicit Init_Turtle_y(::turtle_hunter_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  ::turtle_hunter_interfaces::msg::Turtle y(::turtle_hunter_interfaces::msg::Turtle::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::turtle_hunter_interfaces::msg::Turtle msg_;
};

class Init_Turtle_x
{
public:
  explicit Init_Turtle_x(::turtle_hunter_interfaces::msg::Turtle & msg)
  : msg_(msg)
  {}
  Init_Turtle_y x(::turtle_hunter_interfaces::msg::Turtle::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Turtle_y(msg_);
  }

private:
  ::turtle_hunter_interfaces::msg::Turtle msg_;
};

class Init_Turtle_name
{
public:
  Init_Turtle_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Turtle_x name(::turtle_hunter_interfaces::msg::Turtle::_name_type arg)
  {
    msg_.name = std::move(arg);
    return Init_Turtle_x(msg_);
  }

private:
  ::turtle_hunter_interfaces::msg::Turtle msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::turtle_hunter_interfaces::msg::Turtle>()
{
  return turtle_hunter_interfaces::msg::builder::Init_Turtle_name();
}

}  // namespace turtle_hunter_interfaces

#endif  // TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE__BUILDER_HPP_
