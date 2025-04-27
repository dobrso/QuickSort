import numpy as np
import matplotlib.pyplot as plt
from typing import List


def resultGraph(sizes: List[int], times: List[np.ndarray], iterations: List[int]) -> None:
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Размер входных данных')
    ax1.set_ylabel('Время выполнения (в секундах)', color=color)
    ax1.plot(sizes, times, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:blue'
    ax2.set_ylabel('Количество итераций', color=color)
    ax2.plot(sizes, iterations, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title("Показатели алгоритма QuickSort")
    plt.show()
