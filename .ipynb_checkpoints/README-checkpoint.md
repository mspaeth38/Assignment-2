## This is the readme file for assignment 2 (assignment 3 further down)

The purpose of this assignment is to make a linear regression plot for a dataset given to us in both python and R. I have made a Jupyter notebook for R and python as well as an html file for both.

---
---
### PART I
I added some features to my notebooks which are noted in the comments.

    1. In R: I changed the color of the dots in the scatterplot and the linear regression line using: 
    
    -col to change the outline color of the dots 
    -pch to make the dots filled in 
    -bg to change the color of the fill for the dots

    
     2. python: I changed the color of the dots in the scatterplot and the linear regression line using:
     
    - color to change the color of the dots and the linear regression


In python I also defined x_col and y_col as variables which is also noted in my comments

---

For the actual plotting of the linear regressions I needed to add these tools to my environment

    1. In R: 
            - ggplot
            
    2.  In python:
            - pandas
            - matplotlib
            - scikit-learn

The results of this were scatterplots with a linear regression line overlayed on top of my scatterplots as well as the R-squared value for my regression.


---
---
## PART II
The purpose of part II was to export the Jupyter lab notebooks as scripts that could be run from the command line. First, I exported the scripts, then I modified them to accept arguments. I then ran my scripts from the terminal and saved the plot output image files. To run the scripts input as follows in the command line:

    1. For R: Rscript R_Assignment_2_R.r regression_data.csv YearsExperience Salary
    
    2. For python: python py_Assignment_2_python.py regression_data.csv YearsExperience Salary
    
After these commands are run, a png with the plots will appear (as well as a pdf for R). R also has more information on the details of the plot (such as min, median, max, R-squared) in the terminal.


This assignment was informative, where we learned how to make a scatterplot and linear regression from an imported data set, how to export html files, how to edit scripts to be able to accecpt arguments, and how tp export and execute scripts in the terminal.


---
---
# This is the readme for assignment 3. 

### In this assignment, we are learning how to:

    1. clone a repository 
    
    2. make a new branch within a github repository
    
    3. edit our regression data from assignment_2
    
    4. create tags within github to track changes better
    
    5. create a pull request to re-combine a branch and the main branch
    