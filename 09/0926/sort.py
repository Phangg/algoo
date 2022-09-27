
### merge sort

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    middle = len(lst)//2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):

    result = []

    while left or right:

        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif left:
            result.extend(left)
            break
        elif right:
            result.extend(right)
            break

    return result


# -----------------------------------------------------------------------------

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(l, r):
    res = []
    l = l[::-1]
    r = r[::-1]

    while l or r:
        if l and r:
            if l[-1] >= r[-1]:
                res.append(l.pop())
            else:
                res.append(r.pop())
        elif l:
            res.extend(l[::-1])
            break
        elif r:
            res.extend(r[::-1])
            break

    return res[::-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = merge_sort(lst)
    print(ans)

# -----------------------------------------------------------------------------

### quick sort


def quick_sort(lst, l, r):

    if l < r:
        pivot = partition(lst, l, r)
        quick_sort(lst, l, pivot-1)
        quick_sort(lst, pivot+1, r)



def hoare_partition(lst, l, r):
    pivot = lst[l]
    i = l
    j = r
    while i <= j:
        
        while i <= j and lst[i] <= pivot:
        # while not (lst[i] > pivot):
            i += 1
        while i <= j and lst[j] >= pivot:
            j -= 1
        if i < j :
            lst[i], lst[j] = lst[j], lst[i]

    lst[l], lst[j] = lst[j], lst[l]
    

    return j



def lomuto_partition(lst,l,r):
    pivot = lst[r]
    i = l-1
    for j in range(l, r):
        if lst[j] <= pivot:
            i += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[r], lst[i+1] = lst[i+1], lst[r]
    return i+1



# lst = [1,2,3,4,5,6,7,8,9,0]
# pivot = 6

# left = [x for x in lst if x < pivot]
# right = [x for x in lst if x > pivot]

# result = left + [pivot] + right


# -----------------------------------------------------------------------------
