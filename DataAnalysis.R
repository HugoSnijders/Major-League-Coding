library(tidyverse)
OG <- read.csv('full.csv')
data <- OG
data$age <- data$DeathYear - data$BirthYear
data <- data %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2016) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2016) %>%
  filter(age >= 18 ) %>%
  filter(age <= 120)

wikipeople <- read_csv("wikipeople.csv", 
                       col_types = cols(BirthYear = col_number(), 
                                        DeathYear = col_number()))
all <- wikipeople
all$age <- all$DeathYear - all$BirthYear
all <- all %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2016) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2016) %>%
  filter(age >= 18 ) %>%
  filter(age <= 120)
all <- all %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE))) 

data.baseball <- dplyr::filter(data, grepl('American baseball|American Baseball', Description))
data.football <- dplyr::filter(data, grepl('American Football|American football', Description))
data.baseball <- dplyr::filter(data.baseball, !grepl('coach|Coach|referee', Description))
data.football <- dplyr::filter(data.football, !grepl('coach|Coach|referee', Description))

unique(data$Description)

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
up70 <- data %>%
  filter(age >= 70)

#For baseball and Football
data.baseball <- data.baseball %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE)))
data.football <- data.football %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE)))

U30b <- data.baseball %>%
  filter(age < 30)
U40b <- data.baseball %>% 
  filter(age < 40) %>%
  filter(age >= 30)
U50b <- data.baseball %>% 
  filter(age < 50) %>%
  filter(age >= 40)
U60b <- data.baseball %>% 
  filter(age < 60) %>%
  filter(age >= 50)
U70b <- data.baseball %>% 
  filter(age < 70) %>%
  filter(age >= 60)
up70b <- data.baseball %>%
  filter(age >= 70)



U30f <- data.football %>%
  filter(age < 30)
U40f <- data.football %>% 
  filter(age < 40) %>%
  filter(age >= 30)
U50f <- data.football %>% 
  filter(age < 50) %>%
  filter(age >= 40)
U60f <- data.football %>% 
  filter(age < 60) %>%
  filter(age >= 50)
U70f <- data.football %>% 
  filter(age < 70) %>%
  filter(age >= 60)
up70f <- data.football %>%
  filter(age >= 70)

unique(data$BirthYear)
filter


ggplot() +
  geom_point(data = data.baseball, mapping = aes(x=BirthYear, y=avg.exp, colour='Baseball')) +
  geom_point(data = data.football, mapping = aes(x=BirthYear, y=avg.exp, colour='Football')) +
  geom_point(data = all, mapping = aes(x=BirthYear, y=avg.exp, colour='World'))
  #geom_point(data= U50b, mapping =aes(x=BirthYear, y=avg.exp, colour='orange')) +
  #geom_point(data= U60b, mapping =aes(x=BirthYear, y=avg.exp, colour='orange')) +
  #geom_point(data= U70b, mapping =aes(x=BirthYear, y=avg.exp, colour='orange')) +
  #geom_point(data= up70b, mapping =aes(x=BirthYear, y=avg.exp, colour='orange')) +
  #geom_point(data=U30f, mapping =aes(x=BirthYear, y=avg.exp, colour='red')) +
  #geom_point(data= U40f, mapping =aes(x=BirthYear, y=avg.exp, colour='red')) +
  #geom_point(data= U50f, mapping =aes(x=BirthYear, y=avg.exp, colour='red')) +
  #geom_point(data= U60f, mapping =aes(x=BirthYear, y=avg.exp, colour='red')) +
  #geom_point(data= U70f, mapping =aes(x=BirthYear, y=avg.exp, colour='red')) +
  #geom_point(data= up70f, mapping =aes(x=BirthYear, y=avg.exp, colour='red'))


