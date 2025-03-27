import time
from typing import Generator
from threading import Thread


class GenStatus:
    def __init__(self, gen: Generator, lgen: int) -> None:
        self.gen = self._target(gen)
        self.lgen = lgen
        self.thread = None

    def is_running(self) -> bool:
        return self.gen.gi_running

    def is_suspended(self) -> bool:
        return self.gen.gi_suspended

    def is_closed(self) -> bool:
        return True if self.gen.gi_frame is None else False

    @staticmethod
    def _target(gen) -> Generator:
        for x in gen:
            time.sleep(1)
            yield x

    def _pnv(self) -> None:
        print(f"- Received value: '{next(self.gen)}'")

    def _get_status(self) -> None:
        if self.is_running():
            print("* Status: Running")
        elif self.is_suspended():
            print("* Status: Suspended")
        elif self.is_closed():
            print("* Status: Closed")

    def monitor(self) -> None:
        print("* Status: The Generator was created")

        for _ in range(self.lgen):
            thread = Thread(target=self._pnv)
            thread.start()
            print("- Request the next value")
            self._get_status()
            thread.join()
            self._get_status()
        else:
            try:
                print("- Request the next value")
                next(self.gen)
            except StopIteration:
                print("- StopIteration happened!")
                self._get_status()