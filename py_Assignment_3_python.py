#!/usr/bin/env python
# coding: utf-8

# ### This notebook shows a linear regression using python modeling salary based on years of experience - this one is edited for assignment 3

# ---
# ---

# In[7]:


#loading the dataset and import pandas from the environment (already installed to bash_setup.env)
import pandas as pd
import numpy as np
dataset = pd.read_csv("regression_data.csv")


# In[8]:


#seeing the format of my dataset (just to help me visualize what is happening)
print(dataset)


# In[9]:


#importing and prepping tools for use in linear regression
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


# In[10]:


#use pandas to read the csv file in a way that numpy can understand
df = pd.read_csv('regression_data.csv')
data = df.to_numpy()


# In[11]:


#confirming my column names are the same after pandas so I can use that for numpy
print(df.columns)


# In[12]:


#making my data in numpy
x = np.array(df['YearsExperience'])
y = np.array(df['Salary'])


# In[13]:


# I am checking to make sure my x and y values are correct (earlier in my troubleshooting 
# I had a lot of problems with this)
print("x (YearsExperience):", x)
print("y (Salary):", y)


# In[14]:


# they look good so I am continuing


# In[15]:


# Linear regression additions for my third plot for assignment 3
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)


# In[16]:


#This was leftover from assignment 2 and need it to run my script 
x_col = "YearsExperience"
y_col = "Salary"


# In[17]:


# the old plot for assignment 2 (I didn't want to delete this)
plt.scatter(dataset[x_col], dataset[y_col], color="purple") #change dot color to purple


# In[19]:


# still from assignment 2
#fit a linear model and also import LinearRegression (already installed to bash_setup.env)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[20]:


# overlaying a regression line to the scatterplot (for the old assignment 2)
#change linear regression line to green
plt.plot(dataset[x_col], model.predict(dataset[[x_col]]), color="green")
plt.scatter(dataset[x_col], dataset[y_col], color="purple")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[21]:


# this is where we get back to the new plot for assignment 3
#I changed where the text is so that it looks better on the graph
#I also made the scatterplot in purple
plt.scatter(dataset[x_col], dataset[y_col], color="purple")
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(2.7, max(y) - 25000,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()


# In[22]:


# evaluation of the model
model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared

