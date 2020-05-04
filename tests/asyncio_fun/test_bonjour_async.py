from insights.asyncio_fun.bonjour_aync import the_loop


def test_the_loop():
    test_result = the_loop()
    assert test_result == 'done'
