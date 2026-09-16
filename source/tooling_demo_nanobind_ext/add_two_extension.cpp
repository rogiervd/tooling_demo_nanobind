#include <nanobind/nanobind.h>

#include "tooling_demo_cpp/add_two.hpp"

NB_MODULE(tooling_demo_nanobind_ext, m)
{
    nanobind::class_<tooling_demo_cpp::AddTwo>(
        m, "AddTwo", "Add two to the given integer value.")
        .def(nanobind::init<>())
        .def(
            "__call__", &tooling_demo_cpp::AddTwo::operator(),
            "Add two to the given integer.\n"
            ":param value: The integer value to which two will be added.\n"
            ":return: The result of adding two to the input value.");
}
