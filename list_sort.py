def list_sort(nums):
    """
    :type nums: List[int]
    rtype: List[int]
    """
    # check if first element is smallest? 
        # if not replace it with next smallest number

    for _ in nums:
        for index, element in enumerate(nums):
            for j,i in enumerate(nums[index+1:]):
                if element > i:
                    nums[index] = i
                    nums[index+j+1] = element
                break
    return nums

    
def main():
    nums = [8,9,5,1,6,2,9,11]
    nums2 = [1,2,3,4]
    nums3 = [4,3,2,1]
    index = list_sort(nums=nums2)
    print(index)

if __name__ == "__main__":
    main()