import random
from calculation import countIterations
from typing import List

@countIterations
def qsort(arr: List[int]) -> List[int]:
    if len(arr) <= 1 or arr == sorted(arr):
        return arr

    pivot = random.choice(arr)
    left = []
    middle = []
    right = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)

    return qsort(left) + middle + qsort(right)
