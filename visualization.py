import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
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


def resultTable(sizes: List[int], times: List[np.ndarray], iterations: List[int]) -> None:
    root = tk.Tk()
    root.title("Результаты работы QSort")
    root.geometry("1280x720")

    dataQuadruplets = []
    for i in range(len(sizes)):
        number = i + 1
        quadruplet = (number, sizes[i], times[i], iterations[i])
        dataQuadruplets.append(quadruplet)

    columns = ("number", "size", "time", "iteration")

    tree = ttk.Treeview(columns=columns, show="headings")
    tree.pack(fill=tk.BOTH, expand=1)

    tree.heading("number", text="Номер")
    tree.heading("size", text="Размер входных данных")
    tree.heading("time", text="Время выполнения")
    tree.heading("iteration", text="Количество итераций")

    tree.column("#1", stretch=tk.NO, width=60)
    tree.column("#2", stretch=tk.NO, width=200)
    tree.column("#3", stretch=tk.NO, width=200)
    tree.column("#4", stretch=tk.NO, width=200)

    for quadruplet in dataQuadruplets:
        tree.insert("", tk.END, values=quadruplet)

    root.mainloop()
