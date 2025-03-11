from itertools import chain, combinations

def all_subsets(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))

# Ví dụ
lst = [1, 2, 3]
subsets = all_subsets(lst)

# Hiển thị tất cả các danh sách con
print("All subsets of the list:", subsets)
