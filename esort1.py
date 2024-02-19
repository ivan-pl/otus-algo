from typing import Sequence, TextIO
import tempfile
import numpy as np

from utils import generate_file, timeit_sort_from_file
from msort import msort


def _find_min_ind(array: Sequence[int]) -> int:
    """Returns -1 if the array contains only zeros"""
    index = 0
    min_val = array[0]
    for i in range(1, len(array)):
        val = array[i]
        if val > 0 and val < min_val:
            index, min_val = i, val
    return index if min_val > 0 else -1


def _close_files(files: list[TextIO]) -> None:
    for file in files:
        file.close()


def esort1(path: str, t: int = 10) -> None:
    # split into t files
    tmp_files = [tempfile.NamedTemporaryFile(mode='w', delete=False) for i in range(t)]
    with open(path, 'r') as f:
        ind = 0
        line = f.readline()
        while line:
            tmp_files[ind].write(line)
            line = f.readline()
            ind = (ind + 1) % t
        _close_files(tmp_files)

    # sort every file
    for file in tmp_files:
        f = open(file.name, 'r')
        array = [int(s) for s in f.readlines()]
        msort(array)
        f.close()
        f = open(file.name, 'w')
        f.write('\n'.join(map(str, array)))
    _close_files(tmp_files)

    # merge files
    files = [open(f.name, 'r') for f in tmp_files]
    values = np.array([int(f.readline() or 0) for f in files])
    with open(path, 'w') as f:
        ind = _find_min_ind(values)
        while ind != -1:
            f.write(str(values[ind]) + '\n')
            values[ind] = int(files[ind].readline() or 0)
            ind = _find_min_ind(values)


if __name__ == '__main__':
    for N in [100, 1_000, 10_000, 100_000, 1_000_000]:
        for T in range(5, 20, 5):
            timeit_sort_from_file(N, T, esort1)
