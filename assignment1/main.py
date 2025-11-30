# assignment1/main.py

import queue
import logging
from producer_consumer import Producer, Consumer


def main():
    """
    Entry point demonstrating the producer–consumer pattern
    using a blocking queue and two worker threads.
    """
    # Enable simple logging to observe thread behavior
    logging.basicConfig(level=logging.INFO, format="%(threadName)s - %(message)s")

    # Sample source data for the producer
    source_data = [1, 2, 3, 4, 5]

    # Blocking queue with limited capacity to simulate backpressure
    shared_queue = queue.Queue(maxsize=3)

    # Destination container that the consumer will fill
    dest_data = []

    # Initialize worker threads
    producer = Producer(source_data, shared_queue)
    consumer = Consumer(shared_queue, dest_data)

    # Start both threads
    producer.start()
    consumer.start()

    # Wait for completion
    producer.join()
    consumer.join()

    print("\nFinal Results:")
    print("Source data:     ", source_data)
    print("Destination data:", dest_data)


if __name__ == "__main__":
    main()
