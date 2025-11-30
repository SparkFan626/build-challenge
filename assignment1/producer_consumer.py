# assignment1/producer_consumer.py

import threading
import queue
import logging
from typing import Iterable, List, Any

# Special marker to signal the consumer that production is finished
SENTINEL = object()


class Producer(threading.Thread):
    """
    Producer Thread:
    - Reads items from a source iterable
    - Places each item into the shared blocking queue
    - Always sends a SENTINEL to signal completion
    """
    def __init__(self, source: Iterable[Any], shared_queue: "queue.Queue[Any]"):
        super().__init__()
        self.source = source
        self.shared_queue = shared_queue

    def run(self) -> None:
        try:
            for item in self.source:
                self.shared_queue.put(item)
                logging.info(f"Producing: {item}")
        finally:
            # Ensure consumer is notified even if producer fails
            self.shared_queue.put(SENTINEL)
            logging.info("Producer done, SENTINEL sent.")


class Consumer(threading.Thread):
    """
    Consumer Thread:
    - Continuously consumes items from the shared queue
    - Stops when it receives the SENTINEL
    """
    def __init__(self, shared_queue: "queue.Queue[Any]", dest_container: List[Any]):
        super().__init__()
        self.shared_queue = shared_queue
        self.dest_container = dest_container

    def run(self) -> None:
        while True:
            item = self.shared_queue.get()
            if item is SENTINEL:
                logging.info("Consumer received SENTINEL.")
                break

            self.dest_container.append(item)
            logging.info(f"Consumed: {item}")
            self.shared_queue.task_done()
