#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if len(weights) < 2:
        print("Array is less than 2 indicies")
        return None

    elif len(weights) == 2:
        if weights[0] + weights[1] == limit:
            return [1, 0]

    else:
        for i in range(len(weights)):
            if ht.storage is not None:
                hash_table_insert(ht, weights[i], i)

def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
