cities = []
total_cities = 10
order = []
text_size = 52

def setup():
    size(800, 800)
    for i in range(total_cities):
        v = PVector(random(width), random(height - text_size * 2))
        cities.append(v)
        order.append(i)

    d = calc_distance(cities, order)
    global done
    done = False
    global total_permutations
    total_permutations = factorial(total_cities)
    global count
    count = 0.0
    global record_distance
    record_distance = d
    global best_ever
    best_ever = list(order)

def draw():
    global record_distance
    global best_ever
    global count
    global total_permutations
    
    background(10)
    stroke(255)
    strokeWeight(4)
    noFill()
    for i in range(len(cities)):
        circle(cities[i].x, cities[i].y, 12)
    
    stroke('#4caf50')
    strokeWeight(4)
    noFill()
    beginShape()
    for i in range(len(cities)):
        n = best_ever[i]
        vertex(cities[n].x, cities[n].y)
    endShape()
    
    if not done:
        stroke('#3bacff')
        strokeWeight(1)
        noFill()
        beginShape()
        for i in range(len(cities)):
            n = order[i]
            vertex(cities[n].x, cities[n].y)
        endShape()
    
    d = calc_distance(cities, order)
    if d < record_distance:
        record_distance = d
        best_ever = list(order)
        
    percentage = 100 * (count / total_permutations)
    s = str(nf(percentage, 0, 2)) + "% completed"
    text(s, 20, height - text_size)
    
    textSize(text_size)
        
    if not done:
        next_lexicographic_order()
    else:
        s = str(nf(percentage, 0, 2)) + "% completed"
        noLoop()
        
        
def next_lexicographic_order():
    global count
    global done
    count = count + 1
    largest_i = -1
    largest_j = -1
    
    for i in range(len(order) - 1):
        if order[i] < order[i + 1]:
            largest_i = i
            
    if largest_i == -1:
        count = total_permutations
        done = True
    
    for j in range(len(order)):
        if order[largest_i] < order[j]:
            largest_j = j
            
    swap(order, largest_i, largest_j)
    
    order[largest_i + 1: len(order)] = list(reversed(order[largest_i + 1: len(order)]))
        
        
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def calc_distance(points, order):
    sum = 0
    for i in range(len(points) - 1):
        city_a = points[order[i]]
        city_b = points[order[i + 1]]
        d = dist(city_a.x, city_a.y, city_b.x, city_b.y)
        sum += d

    return sum

def factorial(n):
    if n == 0 or n == 1:
        return 1.0
    else:
        return n * factorial(n - 1)
