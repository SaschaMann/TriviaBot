# Based on Mikhail Gerasimov's [1] answer on StackOverflow [2]
# [1] https://stackoverflow.com/users/1113207/mikhail-gerasimov
# [2] https://stackoverflow.com/questions/45419723/python-timer-with-asyncio-coroutine/45430833#45430833
import asyncio


class AsyncTimer:
    def __init__(self, timeout, callback):
        self._timeout = timeout
        self._callback = callback
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()

    def cancel(self):
        self._task.cancel()
