l = [4,1,789,2314,4,7,5,23,79,123,56]

def mergeTwoList(l1, l2):
    l1_start = 0
    l2_start = 0
    new_list = []

    while l1_start < len(l1) and l2_start < len(l2):
        if l1[l1_start] < l2[l2_start]:
            new_list.append(l1[l1_start])
            l1_start += 1
        else:
            new_list.append(l2[l2_start])
            l2_start += 1
    
    if l1_start < len(l1):
        new_list.extend(l1[l1_start:])
    if l2_start < len(l2):
        new_list.extend(l2[l2_start:])
    return new_list

def mergeSort(ll):
    n = len(ll)
    if n <= 1:
        return ll
    
    mid = n // 2
    left_portion = ll[:mid]
    right_portion = ll[mid:]
    left = mergeSort(left_portion)
    right = mergeSort(right_portion)

    return mergeTwoList(left, right)


new_l = mergeSort(l)
print(new_l)