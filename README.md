## streaming-05-smart-smoker

1.) Clickable link to your public GitHub repo with custom README and displayed screenshot: https://github.com/DrPuffs/streaming-05-smart-smoker <br>
2.) About how long did you spend this module: 2 days. A few hours each day. <br>
3.) Could you develop custom data pipelines for analytics using RabbitMQ and the resources available to you (y/n, why): Yes. It would take some work but I believe I could put the skills together to do so. <br>
4.) What streaming analytics topics / techniques / skills do you think will be most helpful for the work you want to do: Git and reading from CSV files. <br>
5.) Describe an idea for a (relatively simple) custom analytics pipeline you might want to implement in Module 7: I would like to do something game related. Perhaps Twich viewers over time. <br>
6.) What was most difficult about this module: Again, I kind of struggled with TypeErrors. Not nearly as bad as last time, but enough to be frustrating. <br>
7.) What was most interesting: The most interesting part was developing this project from "scratch". I borrowed a lot from previous modules but I enjoyed starting from the very beginning. <br>

![Screenshot 2023-02-12 130515](https://user-images.githubusercontent.com/69999115/218331940-2e365027-4478-4360-92a8-790b61f7e105.png)



## Assignment 6: Finishing the Smart Smoker


Clickable link to your public GitHub repo(s) with custom README and displayed screenshots: https://github.com/DrPuffs/streaming-05-smart-smoker <br>
About how long did you spend this module: 3 days. <br>
Did you use one consumer with 3 queues (or 3 consumers each with one queue): 3 consumers with 1 queue. <br>
Why: Less confusing for me. <br>
When did a Smoker Alert occur: When the temperature dropped by more than 15. It did this several times. My screenshot shows it dropping by 18.8 and 26.7. <br>
When did a Food A stall occur: The first time the temperature changed by 0.6 degrees. <br>
When did a Food B stall occur: The first time the temperature changed by 0.4 degrees. <br>
What was most difficult about this module: TYPEERRORS. I will never get these right the first try it seems. <br>
What was most interesting: Utilziing deque. <br>
In a real system, you'd want to get alerts from your smart smoker - maybe a text message. <br>
Did you experiment with adding alerts to the project and getting an email or text when the smoker alerted? No. Unfortunately, I did not have time. <br>
Would you be able to add this feature if implementing a similar system in real life? I believe that I could and I plan to do so for the project if time allows. <br>


Smart Smoker Producer:
![Smart Smoker Producer](https://github.com/DrPuffs/streaming-05-smart-smoker/blob/main/Smoker%Producer.png)
Smoker Consumer:
![Smoker Consumer](https://github.com/DrPuffs/streaming-05-smart-smoker/blob/main/Smoker%Consumer.png)
Food A Consumer:
![Food A Consumer](https://github.com/DrPuffs/streaming-05-smart-smoker/blob/main/Food%A%Consumer.png)
Food B Consumer:
![Food B Consumer](https://github.com/DrPuffs/streaming-05-smart-smoker/blob/main/Food%B%Consumer.png)
