def tallest_tree(trees:list[int]) -> int:
    maximum = trees[0]
    for tree_height in trees:
        if tree_height > maximum:
            maximum = tree_height
    return maximum

def sorting(tree_heights:list[int]) -> list[int]:
    ##THIS IS AN INSERTION SORT (the nicest one)

    for i in range(1, len(tree_heights)):
        j = i - 1
        key = tree_heights[i]

        while key < tree_heights[j]  and j >= 0:
            tree_heights[j + 1] = tree_heights[j]
            j -= 1
        tree_heights[j + 1] = key

    return tree_heights



def remove_duplicates(tree_heights:list[int]) ->list[int]:
    return list(set(tree_heights))
            
# print(sorting([104, 67, 93, 82]))
print(remove_duplicates([67, 82, 82, 93, 104, 104, 104]))