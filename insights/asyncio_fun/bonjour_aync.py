import asyncio


async def hello_world():
    print("Bonjour tout le monde")


def the_loop():
    loop = asyncio.get_event_loop()
    # blocking call which returns when the hello_world coroutine is done
    loop.run_until_complete(hello_world())
    loop.close()
    return 'done'
