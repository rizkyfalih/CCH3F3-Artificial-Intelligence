from random import uniform
import math
import random

#cost = fungsi
def cost(x1,x2):
    fungsiK = (4-(2.1*(x1**2))+((x1**4)/3))*(x1**2) + x1*x2 + (-4+(4*(x2**2)))*(x2**2)
    return fungsiK 

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def akurasi(solution):
    akurasis = (1-((solution-(-1.03163))/(-1.03163)))*100
    return akurasis

def SA(x1,x2):
    alpha = 0.9
    temperature = 1.0
    min_temperature = 0.00001
    cost1 = cost(x1,x2)
    while temperature > min_temperature:
        i = 1

        while i<=100: # <=3000 for -1.031
            #solution2 =  random.random()
            x1_new = uniform(-10,10)
            x2_new = uniform(-10,10)            
            cost2 = cost(x1_new,x2_new)
            ap = acceptance_probability(cost1,cost2,temperature)
            if ap > random.random():
                x1 = x1_new
                x2 = x2_new
                cost1 = cost2
            i +=1

        temperature = temperature * alpha
    return x1, x2, cost1 , akurasi(cost1)

x1 = uniform(-10,10)
x2 = uniform(-10,10)
print("x1 solusi, x2 solusi, cost, akurasi: ", SA(x1,x2))
print("Reference: http://katrinaeg.com/simulated-annealing.html")