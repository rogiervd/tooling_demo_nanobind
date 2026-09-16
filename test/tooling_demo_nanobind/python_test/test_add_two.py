from tooling_demo_nanobind import AddTwo


def test_add_two_adds_two():
    add_two = AddTwo()
    assert add_two(3) == 5


def test_add_two_handles_negative_numbers():
    add_two = AddTwo()
    assert add_two(-2) == 0


def test_add_two_docstring():
    assert "Add two to the given integer value." in AddTwo.__doc__

    assert "Add two to the given integer." in AddTwo.__call__.__doc__
    assert (
        ":param value: The integer value to which two will be added."
        in AddTwo.__call__.__doc__
    )
    assert (
        ":return: The result of adding two to the input value."
        in AddTwo.__call__.__doc__
    )
