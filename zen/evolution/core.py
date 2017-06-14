from deap.base import Toolbox
from deap.tools import History, Statistics
from termcolor import colored

from .utils import log_stuff


def algorithm(toolbox, stats:Statistics, history:History, hof, popsize:int):
    # Create initial Population and evaluate it
    population = [toolbox.individual() for _ in range(popsize)]
    evaluate(population, toolbox)
    # Commence evolution
    for g in range(0, 1000 ):
        log_stuff(g, history, hof, population, stats, toolbox)
        offspring = toolbox.breed(population)
        mutants = toolbox.mutate(offspring + population)
        evaluate(offspring + mutants + population, toolbox)
        survivors = toolbox.select(offspring + mutants + population)
        population[:]=survivors

    return hof


def evaluate(population, toolbox):
    invalid_ind = [ind for ind in population if not ind.fitness.valid]
    print(colored(f"Summer is here, need to evaluate {len(invalid_ind)} individuals",'blue'))
    print(' '*len(invalid_ind)+'|')
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit