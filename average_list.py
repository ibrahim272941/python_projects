nums1 = [1, 1, 3, 4, 4, 5, 6, 7] 
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
average_nums1 = sum(nums1) / len(nums1)
average_nums2 = sum(nums2) / len(nums2)
total_average = (sum(nums1) + sum(nums2)) / (len(nums1) + len(nums2))
print(average_nums1)
print(average_nums2)
print(total_average)
print(len(nums1) + len(nums2))
print(sum(nums1) + sum(nums2))
