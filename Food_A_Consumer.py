"""
    This program listens for work messages contiously.
    Monitoring the temperature of Food A.  

    Author: Ryan Shaw
    Date: February 21, 2023

"""

import pika
import sys
import time
from collections import deque

foodA_deque = deque(maxlen = 20)

# define a callback function to be called when a message is received
def foodA_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""
    

    foodA_deque.append(body.decode())


    foodA_message = foodA_deque[0]
    
    
    

    foodA_time_old = foodA_message[0:17]

    foodA_temp_old = foodA_message[19:]

    print(foodA_temp_old[18:])


    
    foodA_current = body.decode()

    foodA_time_current = foodA_current[0:17]

    foodA_temp_current = foodA_current[19:]

    print(foodA_temp_current)


    temp_difference = foodA_temp_old = foodA_temp_current

    print(temp_difference)

    if temp_difference != '':

        temp_difference = float(temp_difference)

        if temp_difference < 1:
                print('Alert! Your Food A temperature has stalled!')



    # decode the binary message body to a string
    print(f" [x] Received {body.decode()}")
    # simulate work by sleeping for the number of dots in the message
    time.sleep(body.count(b"."))
    # when done with task, tell the user
    print(" [x] Done.")
    # acknowledge the message was received and processed 
    # (now it can be deleted from the queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# define a main function to run the program
def main(hn: str, qn: str):
    """ Continuously listen for task messages on a named queue."""

    # when a statement can go wrong, use a try-except block
    try:
        # try this code, if it works, keep going
        # create a blocking connection to the RabbitMQ server
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=hn))

    # except, if there's an error, do this
    except Exception as e:
        print()
        print("ERROR: connection to RabbitMQ server failed.")
        print(f"Verify the server is running on host={hn}.")
        print(f"The error says: {e}")
        print()
        sys.exit(1)

    try:
        # use the connection to create a communication channel
        channel = connection.channel()

        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        channel.queue_declare(queue=qn, durable=True)

        # The QoS level controls the # of messages
        # that can be in-flight (unacknowledged by the consumer)
        # at any given time.
        # Set the prefetch count to one to limit the number of messages
        # being consumed and processed concurrently.
        # This helps prevent a worker from becoming overwhelmed
        # and improve the overall system performance. 
        # prefetch_count = Per consumer limit of unaknowledged messages      
        channel.basic_qos(prefetch_count=1) 

        # configure the channel to listen on a specific queue,  
        # use the callback function named callback,
        # and do not auto-acknowledge the message (let the callback handle it)
        channel.basic_consume( queue=qn, on_message_callback=foodA_callback)

        # print a message to the console for the user
        print(" [*] Ready for work. To exit press CTRL+C")

        # start consuming messages via the communication channel
        channel.start_consuming()

    # except, in the event of an error OR user stops the process, do this
    except Exception as e:
        print()
        print("ERROR: something went wrong.")
        print(f"The error says: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print(" User interrupted continuous listening process.")
        sys.exit(0)
    finally:
        print("\nClosing connection. Goodbye.\n")
        connection.close()


# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    # call the main function with the information needed
    main("localhost", "02-food-A")
