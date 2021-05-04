#!/usr/bin/env python
# coding: utf-8

# In[62]:


from bs4 import BeautifulSoup
import requests

website=requests.get("https://www.movieinsider.com/movies/2020").text
soup=BeautifulSoup(website,'lxml')


# In[76]:


#testing only for 2020 year
ls=[]
for title in soup.find_all('div',class_='col-xs-7 col-md-5'):
    name=title.a.text
    ls.append(name)
dict={}


# In[97]:


# now getting movies from year 2010 to 2020
for i in range(2010,2021,1):
    website=requests.get("https://www.movieinsider.com/movies/%s" %i).text
    soup=BeautifulSoup(website,'lxml')
    for title in soup.find_all('div',class_='col-xs-7 col-md-5'):
        name=title.a.text
        dict[name]=i


# In[98]:


dict


# In[99]:


print("len() method :", len(dict))


# In[100]:


a_file = open("moviecompiledata.csv", "w")

writer = csv.writer(a_file)
for key, value in dict.items():
    writer.writerow([key, value])

a_file.close()


# In[ ]:




