#TAXI

steps to create a project :

1.created virtual environment by using the command i.e., python -m venv .venv

2.first craeted registration desk for driver by using  class of cabdriver
 2.1 using constructor method created an empty stack of driver and created a function for driver_info having all the rquired attributes
 2.2 In the function created dictionary of Driver for driver details and appending into the driver list

3.created registration desk for the rider to book a cab, created a class of cabrider in which we followed the same as of driver registration and also created a function to check the rider 

4. In the main file, a1 and a2 location of X- axis and Y- axis respectively and also b1 and b2 are location points of the rider along X- axis and Y- axis created
 4.1 created distance module to check the distance b/w cab and rider 
 4.2 importing math function to def the square root operation for find maximum distance
 4.3 finding max distance formula is sqrt((a2-a1)^2 + (b2-b1)^2)

5. Cab service provides a low, medium and, high quality services which varies in price and they need to give the co-ordinates of destination point

6. Found the max distance by using the reach point module distance required to travel and we found the price multipling the values of d,l and,amount

7. And rider can pay the amount and by taking entry == EXIT he can exit from the cab.