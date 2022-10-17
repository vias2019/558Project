import random 
import logging
import threading
import concurrent.futures

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    
    # __init__() initializes these three members and then calls .acquire() on the .consumer_lock. 
    # This is the state you want to start in. 
    # The producer is allowed to add a new message, 
    # but the consumer needs to wait until a message is present.
    def __init__(self):
        # .message stores the message to pass.
        self.message = 0
        # .producer_lock is a threading.Lock object that
        # restricts access to the message by the producer thread.
        self.producer_lock = threading.Lock()
        # .consumer_lock is also a threading.Lock that 
        # restricts access to the message by the consumer thread.
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    # .get_message() calls .acquire() on the consumer_lock. 
    # This is the call that will make the consumer wait until a message is ready.
    def get_message(self, name):
        logging.debug("%s:about to acquire getlock", name)
        self.consumer_lock.acquire()
        logging.debug("%s:have getlock", name)
        message = self.message
        logging.debug("%s:about to release setlock", name)
        self.producer_lock.release()
        logging.debug("%s:setlock released", name)
        return message

    # .set_message() will acquire the .producer_lock, set the .message, 
    # and the call .release() on then consumer_lock, 
    # which will allow the consumer to read that value.
    def set_message(self, message, name):
        logging.debug("%s:about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s:have setlock", name)
        self.message = message
        logging.debug("%s:about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s:getlock released", name)

SENTINEL = object()
# To generate a fake message, the producer gets a random number between one and one hundred. 
# It calls .set_message() on the pipeline to send it to the consumer.
# use a SENTINEL value to signal the consumer to stop after it has sent ten values. 
def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")

def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    # The consumer reads a message from the pipeline and writes it to a fake database, 
    # which in this case is just printing it to the display. 
    # If it gets the SENTINEL value, it returns from the function, 
    # which will terminate the thread.
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # logging.getLogger().setLevel(logging.DEBUG)  #turn on DEBUG logging to see all of the logging messages 

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)