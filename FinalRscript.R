#Step 1: Reading the .csv data files and assigning it to a variable:
#Command for loading up tidyverse so we can use pipelines etc.
library(tidyverse)

#The command to load up the data
new <- read_csv("Life_Expectancy.csv", col_types = cols(Athlete = col_character(), 
                                                 BirthYear = col_number(), DeathYear = col_number(), 
                                                 American = col_character()))
#Command to copy the original variable to a new one, so we always have one as backup.
new. <- new

#Step 2: Age column:
#Command to create the age column by subtracting year of birth from year of death.
new.$Age <- new.$DeathYear - new.$BirthYear

#Step 3: Filtering:
#A pipeline that filters out negative years of birth/death and filters out people that are
#not in the age range of 18-100. We chose 18 as this is the lowest age at which an athlete got a
#wikipedia page, and 100 as it is 2 standard deviations from the average life expectance of 73,
#which should include 95% of the population.
new. <- new. %>%
  filter(DeathYear >= 1800) %>%
  filter(DeathYear <= 2018) %>%
  filter(BirthYear >= 1800) %>%
  filter(BirthYear <= 2018) %>%
  filter(Age >= 18 ) %>%
  filter(Age <= 100)

#Step 4: More filtering:
#This step is where our original variable is split into the different subsets. First one filters
#for baseball players, second one for non-athletes, third for football players and the last one
#for Americans.
new.baseball <- new. %>%
  filter(Athlete == '1' | Athlete == '3')
new.world <- new. %>%
  filter(Athlete == '0')
new.football <- new. %>%
  filter(Athlete == '2' | Athlete == '3')
new.american <- new. %>%
  filter(American == '1')

#Step 5: Calculating life expectancy:
#Pipelines that first group our data by birth year (for life expectance per year), then
#creates a column with the life expectancy by calculating the mean age of that year.
new.baseball <- new.baseball %>%
  group_by(BirthYear) %>%
  mutate(Avg.exp = (mean(Age, na.rm = TRUE)))
new.football <- new.football %>%
  group_by(BirthYear) %>%
  mutate(Avg.exp = (mean(Age, na.rm = TRUE)))
new.world <- new.world %>%
  group_by(BirthYear) %>%
  mutate(Avg.exp = (mean(Age, na.rm = TRUE)))
new.american <- new.american %>%
  group_by(BirthYear) %>%
  mutate(Avg.exp = (mean(Age, na.rm = TRUE)))

#Step 6: Plotting:
#This command plots 4 scatter plots in one graph, showing correlation between birth year and
#life expectancy for baseball players, football players, non-athletes and Americans. 
r <- ggplot() + ggtitle("First trial of life expectancy for American Football and Baseball players \n compared to different populations") +
  geom_point(data = new.world, mapping = aes(x=BirthYear, y=Avg.exp, colour='World')) +
  geom_point(data = new.american, mapping = aes(x=BirthYear, y=Avg.exp, colour='American')) +
  geom_point(data = new.baseball, mapping = aes(x=BirthYear, y=Avg.exp, colour='Baseball')) +
  geom_point(data = new.football, mapping = aes(x=BirthYear, y=Avg.exp, colour='Football'))

r + labs(x = "Year of Birth", y = "Average Life Expectancy", colour = "Categories")
  






