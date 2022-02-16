cities = []
total_cities = 7

def setup():
    size(800, 600)
    for i in range(total_cities):
        v = PVector(random(width), random(height))
        cities.append(v)

    d = calc_distance(cities)
    global record_distance
    record_distance = d
    global best_ever
    best_ever = list(cities)

def draw():
    global record_distance
    global best_ever
    
    background(10)
    fill(255)
    for i in range(len(cities)):
        circle(cities[i].x, cities[i].y, 12)

    # stroke(255)
    # strokeWeight(1)
    # noFill()
    # beginShape()
    # for i in range(len(cities)):
    #     vertex(cities[i].x, cities[i].y)
    # endShape()
    
    stroke(255, 0, 255)
    strokeWeight(3)
    noFill()
    beginShape()
    for i in range(len(cities)):
        vertex(best_ever[i].x, best_ever[i].y)
    endShape()
    
    i = floor(random(len(cities)))
    j = floor(random(len(cities)))
    swap(cities, i, j)
    d = calc_distance(cities)
    if d < record_distance:
        record_distance = d
        best_ever = list(cities)
        print "Record Distance:", record_distance

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def calc_distance(points):
    sum = 0
    for i in range(len(points) - 1):
        d = dist(points[i].x, points[i].y, points[i + 1].x, points[i + 1].y)
        sum += d

    return sum
