import math

n = int(input().strip())

def nextPermutation(nums):
        i = 0
        flag = False
        iVal = 0
        while (i < len(nums) - 1):
            if nums[i] < nums[i + 1]:
                flag = True
                iVal = max(iVal, i)
            i += 1
        
        if flag:
            j = iVal + 1
            jVal = j
            while (j < len(nums)):
                if nums[j] > nums[iVal]:
                    jVal = max(jVal, j)
                j += 1
            
            t = nums[iVal]
            nums[iVal] = nums[jVal]
            nums[jVal] = t
            
            nums[iVal + 1:] = nums[iVal + 1:][::-1]
        
        else:
            nums[:] = nums[:][::-1]
            
        return nums
    
def convert(a):
    s = ""
    for x in a:
        s = s + str(x)
    return int(s)
    
a = [x + 1 for x in range(n)]
productSet = set()
for _ in range(0, math.factorial(n)):
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            x = convert(a[:i + 1])
            y = convert(a[i + 1: j + 1])
            z = convert(a[j + 1:])
            if x * y == z:
                productSet.add(z)
    a = nextPermutation(a)
    
print(sum(productSet))

