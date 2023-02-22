"""
    This program listens for work messages contiously. 
    Start multiple versions to add more workers.  

    Author: Denise Case
    Date: January 15, 2023

"""

import pika
import sys
import time
from collections import deque

#Declares smoker deque
smoker_deque = deque(maxlen = 5)



# define a callback function to be called when a message is received
def smoker_callback(ch, method, properties, body):
    """ Define behavior on getting a message."""

    #The first 4 values is less than our 2.5 min check time. This if statement allows us to skip over the first 4 values without comparing them.
    if len(smoker_deque) < 5:

        smoker_deque.append(body.decode())

    #Once the deque reaches a length of 5, we want to start monitoring the temps.
    else:
        #Adds incoming message to deque after decoding it.
        smoker_deque.append(body.decode())

        #Assigns the first value in our deque to smoker_message variable.
        smoker_message = smoker_deque[0]
    
        #Assigns the virst 18 values or our smoker_message(which makes up the date/time) to a new variable.
        smoker_time_old = smoker_message[0:17]

        #Assigns the remaining values of our smoker_message(which is the smoker temperature) to a new variable.
        smoker_temp_old = smoker_message[19:]

        print(smoker_temp_old[18:])


        #Assigns the current message to a variable after decoding it.
        smoker_current = body.decode()

        #Assigns the virst 18 values or our smoker_message(which makes up the date/time) to a new variable.
        smoker_time_current = smoker_current[0:17]

        #Assigns the remaining values of our smoker_message(which is the smoker temperature) to a new variable.
        smoker_temp_current = smoker_current[19:]

        print(smoker_temp_current)

        #Calculates the difference between our current temperature and the temperature from 5 values(2.5 minutes) ago.
        temp_difference = smoker_temp_old = smoker_temp_current

        print(temp_difference)

        #Changes temp_difference to a float.
        temp_difference = float(temp_difference)

        #Alerts us if the temp_difference is more than 15.
        if temp_difference > 15:
            print('Alert! Your smoker temperature has dropped too much!')



 
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
        channel.basic_consume( queue=qn, on_message_callback=smoker_callback)

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
    main("localhost", "01-smoker")