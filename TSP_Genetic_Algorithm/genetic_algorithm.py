class TSPGeneticAlgorithm:
    def __init__(self, total_cities, population_size, mutation_rate, stop_threshold):
        self.total_cities = total_cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.current_generation = 0
        self.stop_threshold = stop_threshold
        self.count = 0
    
    def setup(self):
        self.cities = []
        order = []
        self.population = [[]] * self.population_size
        self.fitness = [0.0] * self.population_size
        
        for i in range(self.total_cities):
            v = PVector(random(width), random(120, height / 2))
            self.cities.append(v)
            order.append(i)

        for i in range(self.population_size):
            shuffled_order = self.shuffle(order, i + 1)
            self.population[i] = shuffled_order
            
        self.record_distance = float('inf')
        self.best_ever = []
        self.current_best = []
            
    def draw(self):
        background(20)
        
       
        # Genetic Algorithm
        prev_record_distance = self.record_distance
        self.calculate_fitness()
        self.normalize_fitness()
        self.next_generation()
        if self.record_distance < prev_record_distance:
            self.count = 0
        else:
            self.count += 1
            
        textSize(26)
        noStroke()
        fill(255)
        text("Generation: " + str(self.current_generation) + ", Stop Threshold: " + str(self.stop_threshold), 20, 40)
        text("Record Distance: " + str(nf(self.record_distance, 0, 2)), 20, 80)
        
        
        if self.count == self.stop_threshold:
            noLoop()
    
        stroke('#4caf50')
        strokeWeight(4)
        noFill()
        beginShape()
        for i in range(len(self.best_ever)):
            n = self.best_ever[i]
            vertex(self.cities[n].x, self.cities[n].y)
            circle(self.cities[n].x, self.cities[n].y, 12)
        endShape()
    
        translate(0, height / 2 - 40)
        stroke('#3cabff')
        strokeWeight(4)
        noFill()
        beginShape()
        for i in range(len(self.current_best)):
            n = self.current_best[i]
            vertex(self.cities[n].x, self.cities[n].y)
            circle(self.cities[n].x, self.cities[n].y, 12)
        endShape()

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def shuffle(self, a, num):
        shuffled = list(a)
        for i in range(num):
            index_a = floor(random(len(shuffled)))
            index_b = floor(random(len(shuffled)))
            self.swap(shuffled, index_a, index_b)
            
        return shuffled
    
    def calculate_distance(self, points, order):
        sum = 0
        for i in range(len(points) - 1):
            city_a = points[order[i]]
            city_b = points[order[i + 1]]
            d = dist(city_a.x, city_a.y, city_b.x, city_b.y)
            sum += d
    
        return sum
    
    def calculate_fitness(self):
        current_record = float('inf')
        for i in range(len(self.population)):
            d = self.calculate_distance(self.cities, self.population[i])
            if d < self.record_distance:
                self.record_distance = d
                self.best_ever = self.population[i]
                
            if d < current_record:
                current_record = d
                self.current_best = self.population[i]
            
            self.fitness[i] = 1 / (pow(d, 8) + 1)
            
    def normalize_fitness(self):
        sum = 0.0
        for i in range(len(self.fitness)):
            sum = sum + self.fitness[i]
            
        for i in range(len(self.fitness)):
            self.fitness[i] = self.fitness[i] / sum
            
    def next_generation(self):
        new_population = [[]] * self.population_size
        for i in range(len(self.population)):
            order_a = self.pick_one(self.population, self.fitness)
            order_b = self.pick_one(self.population, self.fitness)
            order = self.cross_over(order_a, order_b)
            self.mutate(order, 0.01)
            new_population[i] = order
            
        self.population = new_population
        self.current_generation += 1 
        
    def pick_one(self, arr_list, prob):
        index = 0
        r = random(1)
        
        while r > 0:
            r = r - prob[index]
            index = index + 1
            
        index = index - 1
        return list(arr_list[index])
    
    def cross_over(self, order_a, order_b):
        start = floor(random(len(order_a)))
        _end = floor(random(start + 1, len(order_a)))
        new_order = []
        for i in range(start, _end):
            new_order.append(order_a[i])
            
        for i in range(len(order_b)):
            city = order_b[i]
            if not city in new_order:
                new_order.append(city)
        
        return new_order
    
    def mutate(self, order, mutation_rate):
        for i in range(self.total_cities):
            if random(1) < self.mutation_rate:
                index_a = floor(random(len(order)))
                index_b = (index_a + 1) % self.total_cities
                self.swap(order, index_a, index_b)        
    
    
    
    
    
        
        
        
