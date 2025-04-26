import calculationAndCreation
import matplotlib.pyplot as plt
from quickSort import qsort

DIR_NAME = "datasets"
FUNCTION_REPEATS = 1

if __name__ == "__main__":
    calculationAndCreation.generateDatasets(DIR_NAME)

    datasets = calculationAndCreation.loadDatasets(DIR_NAME)

    times = []
    iterations = []
    sizes = []

    for size, dataset in datasets:
        time = calculationAndCreation.measureTime(qsort, dataset, repeats=FUNCTION_REPEATS)
        iteration = qsort.iterationCount

        times.append(time)
        iterations.append(iteration)
        sizes.append(size)

    calculationAndCreation.removeDatasets(DIR_NAME)