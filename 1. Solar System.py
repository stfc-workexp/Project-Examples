#!/usr/bin/env python3
from turtle import * # imports everything from the Turtle Module
import math

AU = 149.6e9
G= 6.67408e-11
Scale = 250/ AU  
class Body (Turtle): # The Class Body inherits attributes and methods from Turtle
    """
    The class bodies contains 'Solar Objects' which we need to define a given mass, velocity and position in order to calculate their movement
    according to Newton's Law of Gravitation
    """ # docstring (MUST INCLUDE FOR FUNCTIONS/ CLASSES...)
    name = "Body"
    mass = None
    vx = vy = 0.0
    px = py = 0.0
   
# Ex2: Using Pseudocode from Attraction Method. 
    def attractionMethod (self,other):
        """ (Body): (fx,fy)  # We using another body to produce output (fx,fy)
        This is a method that will calculate the force on the objects in two components (x,y) according to Newton's Law of Gravitation
        """
        if self is other:
            raise ValueError ("You cannot compare self to itself")
        sx = self.px
        sy = self.py
        ox = other.px 
        oy = other.py
        dx = ox - sx
        dy = oy - sy
        d = math.hypot (dx,dy)
        if d is 0:
            raise ValueError ("The Bodies have collided")
        f= (G*self.mass*other.mass)/d**2
        theta = math.atan2(dy,dx)
        fx = math.cos(theta)*f
        fy = math.sin(theta)*f
        return fx, fy   

# Ex3: Creating an Update Info Message 
def update_info (step,bodies):
    """(int, [Body])
This will create table which will return the values calculated using the Attraction method in a table
"""
    
    print ("Step Number{}".format(step)) # printing step number.
    for body in bodies:
        s = "{:^6} Position = {:^6.3f} {:^6.3f} Velocity = {:^10.3f} {:^10.3f}".format(body.name,body.px/AU,body.py/AU,body.vx,body.vy)
        #AU: Scales the numbers
        print(s)
        print()
            
            # For each bodies in bodies: Print out Variable s assigned to the calculated values using formatters. 

def loop (bodies):
    """
    The loop will update the step number, and the positions of all the bodies. This models the movement of the planet"
    """
    # Timestep: incremental change in time which governs the equation that we are solving. In this case we take the timestep as 1 day
    # NB: 1 day will be converted to seconds (SI units)
    timestep = 3600 * 24 
    step = 1
    for body in bodies:
        body.penup()
        body.ht() # Removes the turtle symbol
        
    while True: # This creates an infinite loop
        update_info (step,bodies)
        step += 1 # step = step + 1
        force = {} #empty dictionary
        for body in bodies:
            total_fx = total_fy = 0.0 #Setting the values of these variables. Set to zero so Earth results do not impact Other results.
            for other in bodies: # taking other body
                if body is other:
                    continue # preventing object being compared to itself
                fx,fy = body.attractionMethod(other)# taking other body, giving to attraction method --> calculate the Fg between the two objects. 
                total_fx += fx
                total_fy += fy
            #Newton's Second Law of Motion accounts for the TOTAL FORCE
            force[body] = (total_fx, total_fy)# NB: Dictionaries
        for body in bodies: # iterates over each body
            fx,fy = force[body] # loading the previous force values --> get the most recent step. 
            body.vx +=(fx/body.mass * timestep) # Updated Velocities and Positions using F = ma 
            body.vy += (fy/body.mass * timestep)# Associates F in y to velocity in y
            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px*Scale,body.py*Scale) # show movement graphically
            if body.name is "Sun":
                body.dot(175)
            elif body.name is "Mercury":
                body.dot(10)
            elif body.name is "Venus":
                body.dot (15)
            elif body.name is "Earth":
                body.dot (15)
            else:body.dot(14)
            
            
            # We must now calculate the new force exerted on the object: This will allow us to calculate the new velocities and position of the object(x,y)

# Allows to redefine variables in method
# Runs the main code first in execution
def main ():
    Sun = Body()
    Sun.name = "Sun"
    Sun.mass = 1.98892e30
    Sun.pencolor ("orange")
        

    Earth = Body()
    Earth.name = "Earth"
    Earth.mass = 5.9742e24
    Earth.vy = 29783
    Earth.px = -1*AU
    Earth.pencolor ("#000080")

    Mercury = Body()
    Mercury.name = "Mercury"
    Mercury.mass = 0.33e24
    Mercury.vy = -47400
    Mercury.px = 0.39*AU
    Mercury.pencolor ("#D2691E")


    Venus = Body()
    Venus.name = "Venus"
    Venus.mass = 4.87e24
    Venus.vy = 35000
    Venus.px = -0.723*AU
    Venus.pencolor ("#20B2AA")

    Mars = Body()
    Mars.name = "Mars"
    Mars.mass = 0.642e24
    Mars.vy = 24100
    Mars.px = -1.524*AU
    Mars.pencolor ("#FF0000")

    """
    Jupiter = Body()
    Jupiter.name = "Jupiter"
    Jupiter.mass = 1898e24
    Jupiter.vy = 13100
    Jupiter.px = -5.203*AU
    Jupiter.pencolor ("#FF1493")

    Saturn = Body()
    Saturn.name = "Saturn"
    Saturn.mass = 568e24
    Saturn.vy = 9700
    Saturn.px = -9.539*AU
    Saturn.pencolor ("#B8860B")

    Uranus = Body()
    Uranus.name = "Uranus"
    Uranus.mass = 86.8e24
    Uranus.vy = 6800
    Uranus.px = -19.18*AU
    Uranus.pencolor ("#191970")

    Neptune = Body()
    Neptune.name = "Neptune"
    Neptune.mass = 102e24
    Neptune.vy = 5400
    Neptune.px = -30.06*AU
    Neptune.pencolor ("#00FFFF")

    Pluto = Body()
    Pluto.name = "Pluto"
    Pluto.mass = 0.0146e24
    Pluto.vy = 4700
    Pluto.px = -39.53*AU
    Pluto.pencolor ("#696969")
    """
    screen = Screen()
    screen.screensize(1000, 800)
    screen.bgpic("star.gif")
    bodies = (Sun,Mercury,Venus,Earth,Mars)
    loop(bodies) # Starts the Loop
    


# Executes immediately during import; will not run
if __name__== '__main__':
    main()


    
    
        
        
