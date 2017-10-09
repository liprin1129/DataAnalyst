getwd()
setwd("~/Private_Local_Data/Study/Udacity/DataAnalyst/Lessons/4.\ Exploratory\ Data\ Analysis/eda-course-materials/lesson2/")
getwd()
reddit <- read.csv('reddit.csv')

table(reddit$employment.status)

levels(reddit$age.range)
library(ggplot2)
qplot(data=reddit, x=age.range)
reddit$age.range <- ordered(reddit$age.range, levels = c('Under 18', '18-24',
                                                        '25-34', '35-44', '45-54',
                                                        '55-64', '65 or Above'))

reddit$age.range <- factor(reddit$age.range, levels = c('Under 18', '18-24', '25-34', '35-44', '45-54',
                                                        '55-64', '65 or Above'), ordered = T)
