from insights.args_fun.my_script import do_something


def test_do_something_with_args():
    x = do_something(5, 30)
    assert(x == (5, 30))
