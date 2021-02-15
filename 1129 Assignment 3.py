#!/usr/bin/env python
# coding: utf-8

# In[2]:


marks = {'Andy': 88, 'Amy': 66, 'James': 90, 'Jules': 55, 'Arthur': 77}
print(type(marks))
print(marks)


# In[3]:


for l, n in marks.items():
    print(l,n)


# In[23]:


for n in marks:
    print (marks[n])


# In[21]:


maximum = max(marks.values())
print(maximum)


# In[20]:


minimum = min(marks.values())
print(minimum)


# In[22]:


average = sum (marks.values()) / len(marks.values())
print(average)


# In[32]:


for key in marks:
    if 'J' in key:
        break
    else:
        print(key)


# In[33]:


for key in marks:
    if 'J' in key:
        pass
    else:
        print(key)


# In[35]:


def studentname(Name):
    if Name in marks:
        print(Name, "obtained a grade of", marks[Name])
    else:
        print("I cannot find", Name, "in the list")
studentname("Arthur")
studentname("Jessica")
studentname("James")


# In[ ]:




