from insights.boolean_fun.tut_code_01 import bool_fun


def test_bool_fun():
    expected_string = "notice how the mast of a large ship shows up on the horizon!"
    my_test_result = bool_fun()
    print(my_test_result, expected_string)
    assert my_test_result == expected_string
