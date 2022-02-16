from genetic_algorithm import *

tsp_genetic = TSPGeneticAlgorithm(total_cities=30, 
                                  population_size=500, 
                                  mutation_rate=0.01, 
                                  stop_threshold=400)

def setup():
    size(800, 800)
    tsp_genetic.setup()

def draw():
    tsp_genetic.draw()
