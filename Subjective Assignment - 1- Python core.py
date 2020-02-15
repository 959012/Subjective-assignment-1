#!/usr/bin/env python
# coding: utf-8

# Q1. Write a Python program to get the string from the given string where
# all the occurrence of its first char has been changed to '$,' except first
# char itself?
# 
#     Sample String: 'prospect'
#     Expected Result : 'pros$ect'
# 

# In[62]:


word = 'prospect'
a = word.index('p', word.index('p')+1)
Result = word[:a] + '$'+ word[a+1:]
Result


# Q2. Write a Python program to get the single string from the two given
# strings, and separated by the space and swap the first two characters of
# each string?
# 
#     Sample String : 'abc', 'xyz'.
#     Expected Result: 'xyc abz'

# In[2]:


a = 'abc'
b = 'xyz'
c = list(b + " " + a)
c[2], c[6] = c[6], c[2]
"".join(c)


# Q3. Write the Python program to add 'ing' at the end of the given string
# (length of the string should be at least 3). If given string already ends
# with 'ing,' then add 'ly' instead. If string length of the given string is less
# than 3, leave it unchanged?
# 
# 
#     Sample string: ' abc '
#     Expected result: ' abcing '
#     Sample string: ' string '
#     Expected result: ' stringly '
# 

# In[3]:


x = 'ing'
z= 'ly'
a = 'acbing'
if len(a) == 3:
    print(a+x)
elif len(a) > 3 and a[-3:] == 'ing':
    print(a+z)
else:
    print(a)


# Q4. Write the Python program to find the first appearance of the
# substring 'not' and 'poor' from the given string, if 'not' follows the 'poor',
# replace the whole 'not'...' poor' substring with 'good'.Return the resulting
# string.
# 
#     Sample string: 'The lyrics are not that poor!'
#     'The lyrics are poor!'
#     Expected Result: 'The lyrics are good!'
#     'The lyrics are poor!'

# Q5. Write the Python program to remove the characters which have odd
# index values of a given string.

# In[4]:


def oddnumber(str):
    result = ""
    for i in range(len(str)):
        if i % 2== 0:
            result = result + str[i]
    return result
print(oddnumber('abcderfg'))


# Q6. Write the python program to print the following floating numbers up
# to 2 decimal places?

# In[18]:


a = 5.15256
print(""+"{:.2f}".format(a));


# Q7. Write the Python program to format a number with a percentage?

# In[5]:


a = 0.44
print("{:.2%}".format(a))


# Q8. Write the Python program to count occurrences of a substring in a
# String?

# In[6]:


a = 'Now I am studing Deep Learning aslo studing Machine learning'
print(a.count('studing'))


# Q9. Write the Python program to count repeated characters in a string.
# 
#     Sample string: ' thequickbrownjumpsoverthelazydog '
#     
#     Expected output:
#     o 3
#     e 3
#     u 2
#     h 2
#     r 2
#     t 2

# In[7]:


a = 'thequickbrownjumpsoverthelazydog'
for i in a:
    count= a.count(i)
    if count>0:
        print (i, count)


# Q10. Write the Python program to print the square and cube symbol in
# the area of a rectangle and volume of a cylinder?
# 
#     Sample outputThe area of the rectangle is 1256.66cm2
#     The volume of the cylinder is 1254.725cm3
# 

# In[38]:


rectangle = 1256.66
cylinder = 1254.725
decimals = 2
decimals = 3
print("{0:.{1}f}cm\u00b2".format(rectangle, decimals))
print("{0:.{1}f}cm\u00b2".format(cylinder, decimals))
cylinder


# Q11. Write the Python program to check if a string contains all letters of
# the alphabet?

# In[8]:


import string
alphabet = set(string.ascii_lowercase)
input_string = 'A1CD'
set(input_string.lower()) >= alphabet
True
set(input_string.lower()) >= alphabet
False


# Q12. Write the Python program to find the second most repeated word
# in a given string?

# In[55]:


def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    return counts_x[-2]

print(word_count('Biswa Bhufff Biswa FFFF kkkkkk Biswa, FFFF, ram, sam, ram, ram'))


# Q13. Write the Python program to find the minimum window in the given
# string, which will contains all the characters of another given
# strings?
# 
#     Example 1
#     Input : string1 = " PRWSOERIUSFK "
#     string2 = " OSU "
#     Output: Minimum window is "OERIUS"

# In[ ]:





# Q14. Write the Python program to count number of substrings from a
# given string of lowercase alphabets with exactly k distinct (given)
# characters?
# 
#     Input a string (lowercase alphabets): wolf
#     Input k: 4
#     Number of substrings with exactly 4 distinct characters: 1

# In[ ]:





# Q15. Write the Python program to count number of substrings with same
# first and last characters of the given string?
# 
#     Input a string: abcd
#     4
# 

# In[56]:


def nsubstrings(str):
    result = 0
    n = len(str)
    for i in range(n):
        for j in range(i,n):
            if (str[i]==str[j]):
                result = result +1
    return(result)


# In[61]:


str = 'abcd'
print(nsubstrings(str))


# ## Great Job!
