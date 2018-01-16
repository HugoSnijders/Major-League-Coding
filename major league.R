library(tidyverse)
OG <- read.csv('test.csv')
data <- OG
data$age <- data$DeathYear - data$BirthYear
data <- data %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2016) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2016) %>%
  filter(age >= 18 ) %>%
  filter(age <= 110) %>%

#explain this (why 18) 
data <- data %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE)))  
U30 <- data %>%
  filter(age < 30)
U40 <- data %>% 
  filter(age < 40) %>%
  filter(age >= 30)
  unique(data$BirthYear)
U50 <- data %>% 
  filter(age < 50) %>%
  filter(age >= 40)
U60 <- data %>% 
  filter(age < 60) %>%
  filter(age >= 50)
U70 <- data %>% 
  filter(age < 70) %>%
  filter(age >= 60)
up70 <- data%>%
  filter(age >= 70)


  
unique(data$BirthYear)
  filter
  
ggplot(data = data, mapping = aes(x = BirthYear, y = avg.exp)) + geom_point(mapping = aes(colour = 'black'))

  
  ggplot() +
    geom_point(data=U30, mapping =aes(x=BirthYear, y=avg.exp, colour='orange')) +
    geom_point(data= U40, mapping =aes(x=BirthYear, y=avg.exp, colour='lightblue')) +
    geom_point(data= U50, mapping =aes(x=BirthYear, y=avg.exp, colour='blue')) +
    geom_point(data= U60, mapping =aes(x=BirthYear, y=avg.exp, colour='green')) +
    geom_point(data= U70, mapping =aes(x=BirthYear, y=avg.exp, colour='purple')) +
    geom_point(data= up70, mapping =aes(x=BirthYear, y=avg.exp, colour='brown'))
  
  