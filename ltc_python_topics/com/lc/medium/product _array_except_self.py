# https://leetcode.com/problems/product-of-array-except-self/
def product_array_self(nums):

    arr_length = len(nums)
    # declare output array od same length with zero to retun the result
    output = [0]*arr_length
    """output[i] contains the product of all the elements to the left Note: for the element at index '0', there are no elements to the left,so the output[0] would be 1"""

    output[0] = 1

    for i in range(1, arr_length):
        """ answer[i - 1] already contains the product of elements to the left of 'i - 1' Simply multiplying it with nums[i - 1] would give the product of all elements to the left of index 'i'"""
        output[i] = output[i-1] * nums[i-1]
    """# R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1"""
    R = 1
    for i in reversed(range(arr_length)):
        # For the index 'i', R would contain the
        # product of all elements to the right. We update R accordingly
        output[i] = output[i] * R
        R *= nums[i]
    return output

our_num = [5, 8, 3, 4, 6]
print(product_array_self(our_num))


