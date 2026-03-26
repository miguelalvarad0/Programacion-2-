"""
Algoritmos clásicos de ordenamiento y búsqueda en Python.

Incluye:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Búsqueda Lineal (Linear Search)
- Búsqueda Binaria (Binary Search)

Cada función retorna la lista ordenada (para los sorts) o el índice (para búsquedas).
El bloque main al final muestra ejemplos de uso.
"""

from typing import List

# ---------------------------
# ORDENAMIENTOS
# ---------------------------

def bubble_sort(arr: List[int]) -> List[int]:
    """Ordenamiento Burbuja (in-place). O(n^2) tiempo, O(1) espacio."""
    n = len(arr)
    for i in range(n):
        hubo_cambio = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_cambio = True
        if not hubo_cambio:
            break  # Mejor caso: O(n) si ya estaba ordenado
    return arr


def selection_sort(arr: List[int]) -> List[int]:
    """Ordenamiento por Selección (in-place). O(n^2) tiempo, O(1) espacio."""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr: List[int]) -> List[int]:
    """Ordenamiento por Inserción (in-place). O(n^2) tiempo, O(1) espacio.
    Estable. Muy eficiente para listas casi ordenadas.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr: List[int]) -> List[int]:
    """Merge Sort (O(n log n) tiempo, O(n) espacio). Estable."""
    if len(arr) > 1:
        mid = len(arr) // 2
        izquierda = arr[:mid]
        derecha = arr[mid:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] <= derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]; i += 1; k += 1
        while j < len(derecha):
            arr[k] = derecha[j]; j += 1; k += 1
    return arr


def _partition(arr: List[int], low: int, high: int) -> int:
    """Partición de Lomuto para Quick Sort."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """Quick Sort (promedio O(n log n), peor O(n^2)). In-place."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = _partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


# ---------------------------
# BÚSQUEDAS
# ---------------------------

def linear_search(arr: List[int], target: int) -> int:
    """Búsqueda lineal. O(n) tiempo."""
    for i, v in enumerate(arr):
        if v == target:
            return i
    return -1


def binary_search(arr: List[int], target: int) -> int:
    """Búsqueda binaria (requiere arr ordenado ascendente). O(log n) tiempo."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------------------
# DEMOS
# ---------------------------

if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", datos)

    print("Bubble:", bubble_sort(datos.copy()))
    print("Selection:", selection_sort(datos.copy()))
    print("Insertion:", insertion_sort(datos.copy()))
    print("Merge:", merge_sort(datos.copy()))
    print("Quick:", quick_sort(datos.copy()))

    ordenado = merge_sort(datos.copy())
    print("\nBúsqueda lineal en ordenado:", linear_search(ordenado, 43))
    print("Búsqueda binaria en ordenado:", binary_search(ordenado, 43))
