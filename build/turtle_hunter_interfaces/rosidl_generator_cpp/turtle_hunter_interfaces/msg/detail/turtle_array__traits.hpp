// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from turtle_hunter_interfaces:msg/TurtleArray.idl
// generated code does not contain a copyright notice

#ifndef TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__TRAITS_HPP_
#define TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "turtle_hunter_interfaces/msg/detail/turtle_array__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'alive_turtles'
#include "turtle_hunter_interfaces/msg/detail/turtle__traits.hpp"

namespace turtle_hunter_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const TurtleArray & msg,
  std::ostream & out)
{
  out << "{";
  // member: alive_turtles
  {
    if (msg.alive_turtles.size() == 0) {
      out << "alive_turtles: []";
    } else {
      out << "alive_turtles: [";
      size_t pending_items = msg.alive_turtles.size();
      for (auto item : msg.alive_turtles) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TurtleArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: alive_turtles
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.alive_turtles.size() == 0) {
      out << "alive_turtles: []\n";
    } else {
      out << "alive_turtles:\n";
      for (auto item : msg.alive_turtles) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TurtleArray & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace turtle_hunter_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use turtle_hunter_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const turtle_hunter_interfaces::msg::TurtleArray & msg,
  std::ostream & out, size_t indentation = 0)
{
  turtle_hunter_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use turtle_hunter_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const turtle_hunter_interfaces::msg::TurtleArray & msg)
{
  return turtle_hunter_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<turtle_hunter_interfaces::msg::TurtleArray>()
{
  return "turtle_hunter_interfaces::msg::TurtleArray";
}

template<>
inline const char * name<turtle_hunter_interfaces::msg::TurtleArray>()
{
  return "turtle_hunter_interfaces/msg/TurtleArray";
}

template<>
struct has_fixed_size<turtle_hunter_interfaces::msg::TurtleArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<turtle_hunter_interfaces::msg::TurtleArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<turtle_hunter_interfaces::msg::TurtleArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TURTLE_HUNTER_INTERFACES__MSG__DETAIL__TURTLE_ARRAY__TRAITS_HPP_
