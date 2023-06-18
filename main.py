from twosum import twosum
import sys

def main():
    nums = [1,2,3,4,5,6,7,8,9]

    if len(sys.argv)==2:
        target = int(sys.argv[1])
    else:
        target = 5
    
    index = twosum(nums=nums, target=target)
    print(index)

if __name__ == "__main__":
    main()