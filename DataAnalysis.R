#Step 1: Reading the .csv data files and assigning it to a variable:
#Command for loading up tidyverse so we can use pipelines etc.
library(tidyverse)

#The commands to load up the data of all athletes in a sports teams (OG),
#all people in the wiki data file from 1800-2016 (wikipeople) and all americans (american).
OG <- read.csv('full.csv')
wikipeople <- read_csv("wikipeople.csv", 
                       col_types = cols(BirthYear = col_number(), 
                                        DeathYear = col_number()))
american <- read_csv("american.csv", col_types = cols(BirthYear = col_number(), 
                                                      DeathYear = col_number()))

#Three comands to copy the original variable to a new one, so we always have a reserve
data <- OG
all <- wikipeople
american. <- american

#Step 2: Age column:
#Three commands to create the age column by subtracting year of birth from year of death
data$age <- data$DeathYear - data$BirthYear
all$age <- all$DeathYear - all$BirthYear
american.$age <- american.$DeathYear - american.$BirthYear

#Step 3: Filtering:
#Three pipelines that filter out negative years of birth/death and filters out people that are
#not in the age range of 18-100. We chose 18 as this is the lowest age at which an athlete got a
#wikipedia page.
data <- data %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2018) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2018) %>%
  filter(age >= 18 ) %>%
  filter(age <= 100)
all <- all %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2018) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2018) %>%
  filter(age >= 18 ) %>%
  filter(age <= 100)
american. <- american. %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2018) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2018) %>%
  filter(age >= 18 ) %>%
  filter(age <= 100)

#Step 4: Calculating life expectancy:
#Three pipelines that first group our data by birth year (for life expectance per year), then
#creates a column with the life expectancy by calculating the mean age of that year.
data <- data %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE)))
all <- all %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE))) 
american. <- american. %>%
  group_by(BirthYear) %>%
  mutate(avg.exp = (mean(age, na.rm = TRUE)))

#Step 5: More filtering:
#The first 2 commands are used to filter for American baseball and football players.
#The 3rd and 4th command exclude any referees or coaches in our data
#The last command filters for american people.
#The commands creates 3 new data sets that we can use in our graph
data.baseball <- dplyr::filter(data, grepl('American baseball|American Baseball', Description))
data.football <- dplyr::filter(data, grepl('American Football|American football', Description))
data.baseball <- dplyr::filter(data.baseball, !grepl('coach|Coach|referee', Description))
data.football <- dplyr::filter(data.football, !grepl('coach|Coach|referee', Description))
data.american <- dplyr::filter(american., grepl('American|american', Description))

#Step 6: Plotting:
#This command plots 4 scatter plots in one graph, showing correlation between birth year and
#life expectancy for all people on wikipedia, Americans, American Baseball and Football players
#in our age range. 
ggplot() +
  geom_point(data = data.baseball, mapping = aes(x=BirthYear, y=avg.exp, colour='Baseball')) +
  geom_point(data = data.football, mapping = aes(x=BirthYear, y=avg.exp, colour='Football')) +
  geom_point(data = all, mapping = aes(x=BirthYear, y=avg.exp, colour='World')) +
  geom_point(data = data.american, mapping = aes(x=BirthYear, y=avg.exp, colour='American'))

#Steps we ended up not taking:
#These cammands creates variables for certain age groups that increase in increments of 10 years.
#So U30 = people under 30 years old, U40 = people of age between 30 and 40 and so on.
#We did this both for all people in a sports team and for American baseball and football players.
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

