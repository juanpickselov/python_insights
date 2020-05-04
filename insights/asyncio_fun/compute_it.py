import asyncio


async def compute(x, y):
    print("Compute %s + %s..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


def another_loop():
    a_loop = asyncio.get_event_loop()
    a_loop.run_until_complete(print_sum(15, 5))
    a_loop.close()


another_loop()
