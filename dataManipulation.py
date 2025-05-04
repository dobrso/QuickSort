import random
import os
import shutil
import json
from pathlib import Path
from typing import List, Tuple


def generateDatasets(dirName: str, numberOfDatasets: int = 50, minSize: int = 100, maxSize: int = 10000) -> None:
    if not os.path.exists(dirName):
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


def loadDatasets(dirName: str) -> List[Tuple[int, List[int]]]:
    datasets = []
    dataDir = Path(dirName)

    for file in dataDir.glob("dataset_*.json"):
        with open(file, "r") as f:
            dataset = json.load(f)
            datasets.append((dataset["size"], dataset["dataset"]))

    return sorted(datasets, key=lambda x: x[0])
