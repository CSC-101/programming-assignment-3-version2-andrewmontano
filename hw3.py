from data import CountyDemographics
import build_data

#Part 1
#a function that returns the total population when given a list of county demographics objects
#input: list[CountyDemographics]
#output: int
def population_total(CD_lst:list[CountyDemographics]) -> int:
    sum_population = 0
    for county in CD_lst:
        pop_CD = county.population.get('2014 Population')
        sum_population += pop_CD
    return sum_population

#Part 2
#A function that takes in the data set with a state and returns a list of all counties in a specific state
# input: list of country demographics objects and a string that represents a state's initials.
# output: a list of county demographics objects
def filter_by_state(CD_lst:list[CountyDemographics], State:str) -> list[CountyDemographics]:
    filter_lst = []
    for County in CD_lst:
        if County.state == State:
            filter_lst.append(County)
    return filter_lst

#Part 3
#A function that takes in the data set and a string to find the population part of that category
# input:list of country demographics objects and a string that represents a category
# output: a float
def population_by_education(CD_lst:list[CountyDemographics], Ed:str) -> float:
    pop_total = 0
    for County in CD_lst:
        if County.education.get(Ed):
            ed_per = County.education.get(Ed)/100
            pop_total +=  County.population.get('2014 Population') * ed_per
    return pop_total

#A function that takes in the data set and a string to find the population part of the ethnicities category
# input: list of country demographics objects and a string that represents a category
# output: a float
def population_by_ethnicity(CD_lst:list[CountyDemographics], eth:str) -> float:
    pop_total = 0
    for County in CD_lst:
        if County.ethnicities.get(eth):
            eth_per = County.ethnicities.get(eth)/100
            pop_total += County.population.get('2014 Population') * eth_per
    return pop_total

#A function that takes in the data set and a string to find the population part of
# the below poverty level category in income
# input: list of country demographics objects and a string that represents a category
# output: a float
def population_below_poverty_level(CD_lst:list[CountyDemographics]) -> float:
    pop_total = 0
    for County in CD_lst:
        bpl_per = County.income.get('Persons Below Poverty Level')/100
        pop_total += County.population.get('2014 Population') * bpl_per
    return pop_total

#Part 4
#A function that takes in the data set and a string representing a
# category in education and returns the percentage of the population out of the total
# input: list of country demographics objects and a string that represents a category
# output: a float
def percent_by_education(CD_lst:list[CountyDemographics], ed:str)-> float:
    pop_total = population_total(CD_lst)
    ed_total = population_by_education(CD_lst, ed)
    try:
        ed_percent = ed_total/pop_total
    except ZeroDivisionError:
        ed_percent = 0.0
    return ed_percent*100

#A function that takes in the data set and a string representing a
# category in ethnicities and returns the percentage of the population out of the total
# input: list of country demographics objects and a string that represents a category
# output: a float
def percent_by_ethnicity(CD_lst:list[CountyDemographics], eth:str)-> float:
    pop_total = population_total(CD_lst)
    eth_total = population_by_ethnicity(CD_lst, eth)
    try:
        eth_percent = eth_total/pop_total
    except ZeroDivisionError:
        eth_percent = 0.0
    return eth_percent*100

#A function that takes in the data set and returns the
# percentage the population below poverty level out of the total population
# input: list of country demographics objects and a string that represents a category
# output: a float
def percent_below_poverty_level(CD_lst:list[CountyDemographics])-> float:
    pop_total = population_total(CD_lst)
    bpl_total = population_below_poverty_level(CD_lst)
    try:
        bpl_percent = bpl_total / pop_total
    except ZeroDivisionError:
        bpl_percent = 0.0
    return bpl_percent * 100

#Part 5
#A function that lists the counties with a specific education category percentage
# greater than the given percentage.
#input: a list of CountyDemographics objects, a string, and a float representing a percent
#output: a list of CountyDemographics objects
def education_greater_than(CD_lst:list[CountyDemographics], ed:str, percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.education.get(ed)
        if compare_percent > percent:
            filter_lst.append(county)
    return filter_lst

#A function that lists the counties with a specific education category percentage
# less than the given percentage.
#input: a list of CountyDemographics objects, a string, and a float representing a percent
#output: a list of CountyDemographics objects
def education_less_than(CD_lst:list[CountyDemographics], ed:str, percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.education.get(ed)
        if compare_percent < percent:
            filter_lst.append(county)
    return filter_lst

#A function that lists the counties with a specific ethnicities category percentage
# greater than the given percentage.
#input: a list of CountyDemographics objects, a string, and a float representing a percent
#output: a list of CountyDemographics objects
def ethnicities_greater_than(CD_lst:list[CountyDemographics], eth:str, percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.ethnicities.get(eth)
        if compare_percent > percent:
            filter_lst.append(county)
    return filter_lst

#A function that lists the counties with a specific ethnicities category percentage
# less than the given percentage.
#input: a list of CountyDemographics objects, a string, and a float representing a percent
#output: a list of CountyDemographics objects
def ethnicities_less_than(CD_lst:list[CountyDemographics], eth:str, percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.ethnicities.get(eth)
        if compare_percent < percent:
            filter_lst.append(county)
    return filter_lst

#A function that lists the counties where the percentage of people below poverty level is
# greater than the given percentage.
#input: a list of CountyDemographics objects and a float representing a percent
#output: a list of CountyDemographics objects
def below_poverty_level_greater_than(CD_lst:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.income.get('Persons Below Poverty Level')
        if compare_percent > percent:
            filter_lst.append(county)
    return filter_lst

#A function that lists the counties where the percentage of people below poverty level is
# less than the given percentage.
#input: a list of CountyDemographics objects and a float representing a percent
#output: a list of CountyDemographics objects
def below_poverty_level_less_than(CD_lst:list[CountyDemographics], percent:float) -> list[CountyDemographics]:
    filter_lst = []
    for county in CD_lst:
        compare_percent = county.income.get('Persons Below Poverty Level')
        if compare_percent < percent:
            filter_lst.append(county)
    return filter_lst
