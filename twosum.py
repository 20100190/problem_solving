def twosum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

def main():
    nums = [1,2,3,4,5,6,7,8,9]
    target = 5
    index = twosum(nums=nums, target=target)
    print(index)

if __name__ == "__main__":
    main()