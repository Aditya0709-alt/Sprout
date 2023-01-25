import threading
import time

class Task(threading.Thread):
    def __init__(self, **kwargs):
        """
        Creates a repeating, periodic, background `Task` object. Accepts a "task" function and a sleep interval as keyword arguments.
        """
        super().__init__()

        self.running = True
        self.killed = False

        try:
            self.task = kwargs['task']
        except:
            raise RuntimeError('Task function not specified')

        try:
            self.sleep = kwargs['sleep']
        except:
            raise RuntimeError('Sleep period missing')

    def run(self):
        """
        Overriding the internal `run()` method of a threading.Thread() object.
        """
        while not self.killed:
            if self.running:
                self.task()
                time.sleep(self.sleep)

    def stop(self):
        """
        Pauses the `Task` loop.
        """
        self.running = False

    def restart(self):
        """
        Restarts a paused `Task`.
        """
        self.running = False
        self.running = True

    def kill(self):
        """
        Kills and finally ends the `Task` loop.
        """
        self.stop()
        self.killed = True
        self.join()