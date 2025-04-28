import calculation
import dataManipulation
from visualization import resultGraph, resultTable
from quickSort import qsort

DIR_NAME = "datasets"
FUNCTION_REPEATS = 1

if __name__ == "__main__":
    dataManipulation.generateDatasets(DIR_NAME)

    datasets = dataManipulation.loadDatasets(DIR_NAME)

    dataManipulation.removeDatasets(DIR_NAME)

    times = []
    iterations = []
    sizes = []

    for size, dataset in datasets:
        time = calculation.measureTime(qsort, dataset, repeats=FUNCTION_REPEATS)
        iteration = qsort.iterationCount

        times.append(time)
        iterations.append(iteration)
        sizes.append(size)

    resultGraph(sizes, times, iterations)

    resultTable(sizes, times, iterations)


