args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

#changed color of the dots and linear regression line to match what is in my Jupyter notebook
library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "green") +
  geom_smooth(method = "lm", color = "purple") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot)
print(plot)

#reading the class dataset 
dataset <- read.csv("regression_data.csv")

#plotting the dataset (scatterplot)
#change the color (outline) of the dots to black (col="black")
#pch=21 makes the dots filled in and bg="green" makes the color of the fill
plot(dataset$YearsExperience, dataset$Salary, pch=21, bg="green", col="black")

#Fitting the data to a linear model
model <- lm(Salary ~ YearsExperience, data=dataset)

#Overlaying a regression line
#change the colors of the dots and regression line
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'green') +
  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'purple') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

#evaluating the linear regression model
summary(model)
