"""
    This program reads the smoker temperature, Food A temp and Food B temp
    from a CSV file and sends them to a queue.

    Author: Ryan Shaw
    Date: 2/12/2023

"""

import pika
import sys
import webbrowser
import csv
import time



def offer_rabbitmq_admin_site():
    
    ans = input("Would you like to monitor RabbitMQ queues? y or n ")
    print()
    if ans.lower() == "y":
        webbrowser.open_new("http://localhost:15672/#/queues")
        print()

def send_message(host: str, queue_name: str, message: str):
    
    

    
    

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters(host))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a durable queue
        # a durable queue will survive a RabbitMQ server restart
        # and help ensure messages are processed in order
        # messages will not be deleted until the consumer acknowledges
        ch.queue_declare(queue=queue_name, durable=True)
        # use the channel to publish a message to the queue
        # every message passes through an exchange
        ch.basic_publish(exchange="", routing_key=queue_name, body=message)
        # print a message to the console for the user
        print(f" [x] Sent {message}")
    except KeyboardInterrupt:
        print()
        print(" User interrupted process.")
        sys.exit(0)
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)

    finally:
        # close the connection to the server
        conn.close()

# Opens CSV file and cycles through it while skipping the header row
with open("C:\\Users\\User\\Desktop\\streaming-05-smart-smoker\\smoker-temps.csv", "r") as import_file:
    reader = csv.reader(import_file, delimiter=',')
    next(reader, None)
    offer_rabbitmq_admin_site()

    for row in reader:
    
    
        if __name__ == "__main__":  

            
            print("To exit press CTRL+C")
        
            Time, Smoker_Temp, FoodA_Temp, FoodB_Temp = row

            
        
         
            smoker_temp_message = (Time, Smoker_Temp)
            foodA_temp_message = (Time, FoodA_Temp)
            foodB_temp_message = (Time, FoodB_Temp)

            smoker_temp_message2 = ' '.join(smoker_temp_message)
            foodA_temp_message2 = ' '.join(foodA_temp_message)
            foodB_temp_message2 = ' '.join(foodB_temp_message)


            if Smoker_Temp != '':
                Smoker_Temp = float(Smoker_Temp)

            if FoodA_Temp != '':
                FoodA_Temp = float(FoodA_Temp)

            if FoodB_Temp != '':
                FoodB_Temp = float(FoodB_Temp)

    

        
        # send the messages to the queue
        # prints the messages to indicate success
            send_message("localhost","01-smoker",smoker_temp_message2.encode())
            print(f'Sent {smoker_temp_message2} to 01-smoker queue.')
            send_message("localhost", "02-food-A", foodA_temp_message2.encode())
            print(f'Sent {foodA_temp_message2} to 02-food-A queue.')
            send_message("localhost", "02-food-B", foodB_temp_message2.encode())
            print(f'Sent {foodB_temp_message2} to 02-food-B queue.')
            time.sleep(3)
        
