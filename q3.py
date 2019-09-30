# ### Problem 3
# Given 2 lists of claim numbers, write the code to merge the 2 lists provided to produce a new list by alternating values between the 2 lists. Once the merge has been completed, print the new list of claim numbers (DO NOT just print the array variable!)
# ```
# # Start with these lists
# list_of_claim_nums_1 = [2, 4, 6, 8, 10]
# list_of_claim_nums_2 = [1, 3, 5, 7, 9]
# ```
# Example Output:
# ```
# The newly created list contains:     2  1  4  3  6  5  8  7  10  9
# `
# def new_list():
list_Array1 = [2, 4, 6, 8, 10]
list_Array2 = [1, 3, 5, 7, 9]
new_listArray=[]

list_Array1.append(list_Array2)
print(list_Array1)