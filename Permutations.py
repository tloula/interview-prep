import itertools

def permute(nums):
    return list(itertools.permutations(nums))

print(permute([1,2,3]))