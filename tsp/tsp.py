import math

class Point:
    def __init__(self, index, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.index = index

    def col1 = []
    def col2 = []
    def col3 = []

    def distance(self, planet): # function that calculates distance
        return math.sqrt((self.x-planet.x)**2 + (self.y-planet.y)**2 + (self.z-planet.z)**2)

    def __repr__(self):
        return "(" + str(self.index) + ": " + ", ".join([str(self.x),str(self.y),str(self.z)]) + ")"

def getPlanets(filename='planets.txt'):#grabs data from given txt file
    with open(filename, 'r') as file:
        return [Point(*[int(k) for k in line.split(' ')]) for line in file]

def evaluateRoute(route):
    dist = sum(route[i].distance(route[i+1]) for i in range(len(route)-1))
    return dist + route[-1].distance(route[0])

def saveRoute(route):
    with open("route.txt", mode="w") as f:
        f.write(" ".join([str(planet.index) for planet in route]))

planets = getPlanets()

print(evaluateRoute(planets))

print(planets)


# Insert your code here!
while len(planets)>0:
    closest_planet =planets[0] # use hashtags for comments in python OK
    for planet in planets
        if route[1].distance(planet) < route [1].distance(closest_planet):
            closest_planet = planet
    planets.route(closest_planet)
    route.append
