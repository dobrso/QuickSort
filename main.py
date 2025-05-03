import calculation
import dataManipulation
import visualization
from quickSort import qsort

DIR_NAME = "datasets"
FUNCTION_REPEATS = 1


def main() -> None:
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

    visualization.resultGraph(sizes, times, iterations)

    visualization.resultTable(sizes, times, iterations)


if __name__ == "__main__":
    main()
