#reading the class dataset 
df <- read.csv("regression_data.csv")
dataset <- read.csv("regression_data.csv")
x <- "YearsExperience"
y <- "Salary"

#check the format of the dataset (as df)
print(df)

#from assignment 3 need to get ggplot2 ready
library(ggplot2)

# Fit model
#edited so that I could theoretically use any csv file instead of only this specific file
#I would have to redefine by variables df, x, and y to do that
model <- lm(as.formula(paste(y, "~", x)), data = df)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(df[[x]], df[[y]])
pred <- predict(model)
mse <- mean((df[[y]] - pred)^2)

# Plot the data
ggplot(df, aes_string(x = x, y = y)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  annotate("text", x = 2, y = max(df[[y]]) - 5,
           label = paste("y =", round(slope, 2), "x +", round(intercept, 2),
                         "\nr =", round(r, 2), "\nMSE =", round(mse, 2)),
           size = 4) +
  labs(title = "Linear Fit",
       x = "x", y = "y") +
  theme_minimal()

#plotting the dataset (scatterplot) (assignment2)
#change the color (outline) of the dots to black (col="black")
#pch=21 makes the dots filled in and bg="green" makes the color of the fill
plot(dataset$YearsExperience, dataset$Salary, pch=21, bg="green", col="black")

#Saving
ggsave("regression_plot_r.png")

#Fitting the data to a linear model
model <- lm(Salary ~ YearsExperience, data=dataset)

#Overlaying a regression line
#change the colors of the dots and regression line
library(ggplot2)
ggplot() +
  geom_point(aes(x = df$YearsExperience, y = df$Salary), colour = 'green') +
  geom_line(aes(x = df$YearsExperience, y = predict(model, newdata = dataset)), colour = 'purple') +
  ggtitle('Salary vs Experience') +
  xlab('Years of experience') +
  ylab('Salary')

#evaluating the linear regression model
summary(model)
