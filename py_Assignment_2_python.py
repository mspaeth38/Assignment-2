#!/usr/bin/env python
# coding: utf-8

# ### This notebook shows a linear regression using python modeling salary based on years of experience 

# ---
# ---


import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

#changed color of the dots and linear regression line to match what is in my Jupyter notebook
plt.scatter(data[[x_col]], data[[y_col]], color='purple')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='green')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()

# In[24]:


#loading the dataset and import pandas from the environment (already installed to bash_setup.env)
import pandas as pd
dataset = pd.read_csv("regression_data.csv")


# In[25]:


#I want to be able to type x_col and y_col instead of the actual names for later in my code
#I think this is how you define a variable but I'm not 100% sure
x_col = "YearsExperience"
y_col = "Salary"


# In[26]:


#make a scatterplot and import matplot from the environment (already installed to bash_setup.env)
import matplotlib.pyplot as plt
plt.scatter(dataset[x_col], dataset[y_col], color="purple") #change dot color to purple


# In[8]:


#the plot still appeared as it did before with my variable changes so I think it worked
#fit a linear model and also import LinearRegression (already installed to bash_setup.env)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])


# In[23]:


# overlaying a regression line to the scatterplot
#change linear regression line to green
plt.plot(dataset[x_col], model.predict(dataset[[x_col]]), color="green")
plt.scatter(dataset[x_col], dataset[y_col], color="purple")
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# In[10]:


# evaluation of the model
model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared

