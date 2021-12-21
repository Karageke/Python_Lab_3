import json
import pathlib
import pickle
from tqdm import tqdm


class ValidPeople:
    data: list

    def __init__(self, path: pathlib.Path) -> None:
        self.data = json.load(open(path, encoding='windows-1251'))


def quick_sort(alist ,flag:str):
    """alist список словарей
        flag поле по которому мы сортируем quick_sotr'ом
    """
    alist = alist[:100]
    if len(alist) < 2:
        return
    borders = [[0, len(alist) - 1]]
    while len(borders) > 0:
        left, right = borders.pop()
        p = alist[(left + right) // 2]
        i = left - 1
        j = right + 1
        while 1:
            while 1:
                i += 1
                if alist[i][flag] >= p[flag]:
                    break
            while 1:
                j -= 1
                if alist[j][flag] <= p[flag]:
                    break
            if i >= j:
                break
            alist[i], alist[j] = alist[j], alist[i]
        if j > left:
            borders.append([left, j])
        j += 1
        if right > j:
            borders.append([j, right])
    return alist

def write(path,array):
    """serealization write Pickle"""
    with open(path, 'wb') as write_file:
        pickle.dump(array, write_file)

def read(path):
    """serealization read Peckle"""
    with open(path, 'rb') as read_file:
        pickle.load(read_file)

valid_data = ValidPeople(pathlib.Path("correct_data.txt"))
sort_data = quick_sort(valid_data.data, "weight")
json.dump(sort_data,open("result_sort.txt", "w"),indent=4)

write("serial.pickle", sort_data)
readfile = read(pathlib.Path('serial.pickle'))