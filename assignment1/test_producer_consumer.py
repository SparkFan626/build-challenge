# assignment1/test_producer_consumer.py

import unittest
import queue
import time
from producer_consumer import Producer, Consumer, SENTINEL


class TestProducerConsumer(unittest.TestCase):

    def test_all_items_transferred(self):
        """
        All produced items should appear in the destination container.
        """
        source = [10, 20, 30, 40]
        shared_queue = queue.Queue()
        dest = []

        producer = Producer(source, shared_queue)
        consumer = Consumer(shared_queue, dest)

        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

        self.assertEqual(dest, source)

    def test_empty_source(self):
        """
        Empty source should produce an empty destination.
        """
        source = []
        shared_queue = queue.Queue()
        dest = []

        producer = Producer(source, shared_queue)
        consumer = Consumer(shared_queue, dest)

        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

        self.assertEqual(dest, [])

    def test_blocking_behavior(self):
        """
        Queue should handle blocking properly under limited capacity.
        """
        source = list(range(20))
        shared_queue = queue.Queue(maxsize=1)
        dest = []

        producer = Producer(source, shared_queue)
        consumer = SlowConsumer(shared_queue, dest)

        producer.start()
        consumer.start()
        producer.join()
        consumer.join()

        self.assertEqual(dest, source)


class SlowConsumer(Consumer):
    """
    A slower consumer for testing queue blocking behavior.
    """
    def run(self):
        while True:
            item = self.shared_queue.get()
            if item is SENTINEL:
                break
            time.sleep(0.01)
            self.dest_container.append(item)
            self.shared_queue.task_done()


if __name__ == "__main__":
    unittest.main()
