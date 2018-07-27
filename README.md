# Simulating Planetary Orbits
This repository contains an example of a work experience project: Simulating Planetary Orbits in Python. This small Object-Oriented program will introduce you to the basic principles of Python programming. 

This exercise uses a computational method called NUMERIC INTEGRATION.

A.	BASIC PRINCIPLES OF THE PROGRAM 


The program uses a “brute force approach” as the basis for our simulation. 
1.	We map the Object Positions and Velocities at time, t using a coordinate system 
2.	Calculate the forces the bodies exert on each other in both the x and y components. 
3.	The Velocities and the Position of the Body is updated using a while loop, as the object “steps forward throughout time” in an incremental step of one day. 
4.	The results are outputted into a table 
5.	Using the turtle module in Python, the movement of the object can be mapped graphically. 

B.	UNDERSTANDING THE PROGRAM 

Let a class of solar objects be created, with definitions of velocity, mass and position of the object. 
Using Newton’s Law of Gravitation, we can calculate the force of the object. This is expressed in our Attraction method, where the force will be calculated in the x and y components.
Update Info Message is a table that will return the values of the Attraction Method in a table that is printed 

The loop function models the movement of the bodies using a while loop.

We take the “other body”, and use the same Attraction Method Fg to update fx and fy. We update the position of the body using Newton’s Second Law of Motion. 

We create a main function which contains the name, mass, vx and py of each object in the solar system. 

The bodies are run in the loop (bodies) and the program is run because of the main sentinel statement at the end of the program. 
Graphics
We use the Turtle Module as the parent class to bodies, so bodies inherits the attributes and methods of the module. 

We then use the dot size and pen color (note the American spelling) functions in our main function. 
