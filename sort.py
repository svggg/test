def integer_list(txt):
    lst = []

    for char in txt:
        lst.append(int(char))
    return lst

def quick_merge(list1, list2):
    result = []

    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


n = int(input())

lst1 = integer_list(input().split())

final_list = quick_merge(lst1, integer_list(input().split()))

for _ in range(n - 2):
    final_list = quick_merge(final_list, integer_list(input().split()))

print(*final_list)