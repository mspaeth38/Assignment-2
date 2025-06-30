This is the readme file for assignment 2.

The purpose of this assignment is to make a linear regression plot for a dataset given to us in both python and R. I have made a Jupyter notebook for R and python as well as an html file for both.


PART I
I added some features to my notebooks which are noted in the comments.
    In R: I changed the color of the dots in the scatterplot and the linear regression line using:
            1) col to change the outline color of the dots
            2) pch to make the dots filled in
            3) bg to change the color of the fill for the dots
    In python: I changed the color of the dots in the scatterplot and the linear regression line using:
            1) color to change the color of the dots and the linear regression

In python I also defined x_col and y_col as variables which is also noted in my comments

For the actual plotting of the linear regressions I needed to add these tools to my environment
    In R: 
            1) ggplot
    In python:
            1) pandas
            2) matplotlib
            3) scikit-learn

The results of this were scatterplots with a linear regression line overlayed on top of my scatterplots as well as the R-squared value for my regression.

    # Assignment2_Linear_Regressions


PART II
The purpose of part II was to export the Jupyter lab notebooks as scripts that could be run from the command line. First, I exported the scripts, then I modified them to accept arguments. I then ran my scripts from the terminal and saved the plot output image files. To run the scripts input as follows in the command line:
    For R: Rscript R_Assignment_2_R.r regression_data.csv YearsExperience Salary
    For python: python py_Assignment_2_python.py regression_data.csv YearsExperience Salary
After these commands are run, a png with the plots will appear (as well as a pdf for R). R also has more information on the details of the plot (such as min, median, max, R-squared) in the terminal.


This assignment was informative, where we learned how to make a scatterplot and linear regression from an imported data set, how to export html files, how to edit scripts to be able to accecpt arguments, and how tp export and execute scripts in the terminal.