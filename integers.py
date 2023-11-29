def find_smallest_index(nums):
    smallest = float('inf')
    smallest_index = 0
    
    for i in range(len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i
    
    return smallest_index

# Test program
num_list = input("Enter a list of numbers (separated by spaces): ")
num_list = list(map(int, num_list.split()))
index = find_smallest_index(num_list)
print("The index of the smallest element is:", index)
