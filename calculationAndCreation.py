import time
import random
import os
import json
import shutil
import numpy as np
from pathlib import Path
from typing import Callable, Any, List

def measureTime(func: Callable[..., Any], *args: Any, repeats: int) -> np.ndarray:
    times = []

    for _ in range(repeats):
        timeStart = time.perf_counter_ns()
        func(*args)
        timeEnd = time.perf_counter_ns()

        timeDiff = timeEnd - timeStart
        times.append(timeDiff)

    meanTime = np.mean(times)
    return meanTime

def countIterations(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any) -> Any:
        wrapper.iterationCount += 1

        return func(*args)

    wrapper.iterationCount = 0

    return wrapper

def generateDatasets(dirName: str, numberOfDatasets: int = 50, minSize: int = 100, maxSize: int = 10000) -> None:
    os.mkdir(dirName)

    for i in range(numberOfDatasets):
        sizeOfDataset = random.randint(minSize, maxSize)
        dataset = [random.randint(-1000, 1000) for _ in range(sizeOfDataset)]

        with open(f"{dirName}/dataset_{i+1}.json", "w") as f:
            json.dump({
                "size": sizeOfDataset,
                "dataset": dataset
            }, f)

def removeDatasets(dirName: str) -> None:
    shutil.rmtree(dirName)

def loadDatasets(dirName: str) -> List[List[int]]:
    datasets = []
    dataDir = Path(dirName)

    for file in dataDir.glob("dataset_*.json"):
        with open(file, "r") as f:
            dataset = json.load(f)
            datasets.append((dataset["size"], dataset["dataset"]))

    return sorted(datasets, key=lambda x: x[0])