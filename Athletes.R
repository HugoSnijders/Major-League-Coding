library('tidyverse')
library(readr)
dataset <- read_csv("~/Group Assignment/.csv", 
                    col_types = cols(BirthYear = col_integer(), 
                                     DeathYear = col_integer(), Description = col_character()))
View(dataset)

athletes1 <- dataset
athletes1$age <- athletes1$DeathYear - athletes1$BirthYear 

View(athletes1)

athletes2 <- athletes1 %>%
  filter(BirthYear > 1899) %>%
  filter(age > 0)

athletes.af <- athletes2 %>%
  filter(Description == 'American football player')

athletes.AF <- athletes.af %>%
  filter(BirthYear > 1899) %>%
  filter(age > 0) %>%
  filter(age < 150)

athletes.AF2 <- subset(athletes.AF, select = -c(DeathYear, Description))

ggplot(data = athletes.AF) +
  geom_point(mapping = aes(x = BirthYear, y = age))

Athletes.AF3 <- aggregate(. ~BirthYear, athletes.AF2, mean)


ggplot(data = athletes2) +
  geom_point(mapping = aes(x = BirthYear, y = age))

new3 <- read_csv("~/Group Assignment/new3.csv", 
                 col_types = cols(BirthYear = col_integer(), 
                                  DeathYear = col_integer()))
View(new3)

new3$age <- new3$DeathYear - new3$BirthYear

new4 <- new3 %>%
  filter(BirthYear > 1899) %>%
  filter(age > 0) %>%
  filter(age < 150)

new5 <- subset(new4, select = -c(DeathYear))

new6 <- aggregate(. ~BirthYear, new5, mean)
  

ggplot() +
  geom_point(data = new6, mapping = aes(x = BirthYear, y = age, color = 'people')) +
  geom_point(data = Athletes.AF3, mapping = aes(x = BirthYear, y = age, color='football players'))




             