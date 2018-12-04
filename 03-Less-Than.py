
# coding: utf-8

# In[ ]:


# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
# Instead of printing the elements one by one, make a new list that has all the elements in it and print out this new list. Write this in one line of code.

num = int(input('Enter a number: '))

print([i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i<num])

