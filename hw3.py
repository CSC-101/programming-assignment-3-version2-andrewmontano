# Task 1: Define CountyDemographics class
class CountyDemographics:
    def __init__(self, age: dict[str, float], county: str, education: dict[str, float],
                 ethnicities: dict[str, float], income: dict[str, float],
                 population: dict[str, float], state: str):
        self.age = age
        self.county = county
        self.education = education
        self.ethnicities = ethnicities
        self.income = income
        self.population = population
        self.state = state

    def __repr__(self):
        return f'CountyDemographics({self.age}, {self.county}, {self.education}, {self.ethnicities}, {self.income}, {self.population}, {self.state})'
# Task 2: Function to compute total population
def total_population(county: CountyDemographics) -> float:
    return sum(county.population.values())
# Task 3: Function to compute average income
def average_income(county: CountyDemographics) -> float:
    return sum(county.income.values()) / len(county.income) if county.income else 0


# Task 4: Function to find largest ethnic group
def largest_ethnic_group(county: CountyDemographics) -> str:
    return max(county.ethnicities, key=county.ethnicities.get)


# Task 5: Function to categorize education levels
def categorize_education(county: CountyDemographics) -> str:
    higher_education_rate = county.education.get("Bachelor's Degree", 0) + county.education.get("Graduate Degree", 0)
    if higher_education_rate > 50:
        return "Highly Educated"
    elif higher_education_rate > 25:
        return "Moderately Educated"
    else:
        return "Less Educated"





#Load data from a CSV file
def load_data(filename: str) -> list:
    counties = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming your CSV columns match the keys for CountyDemographics
            age = {"0-18": float(row["age_0_18"]), "19-64": float(row["age_19_64"]), "65+": float(row["age_65_plus"])}
            education = {"High School": float(row["education_highschool"]),
                         "Bachelor's": float(row["education_bachelors"]),
                         "Graduate": float(row["education_graduate"])}
            ethnicities = {"White": float(row["ethnicity_white"]), "Hispanic": float(row["ethnicity_hispanic"]),
                           "Black": float(row["ethnicity_black"]), "Other": float(row["ethnicity_other"])}
            income = {"Median": float(row["income_median"])}
            population = {"Total": float(row["population_total"])}
            state = row["state"]
            county = row["county"]

            county_demo = CountyDemographics(age, county, education, ethnicities, income, population, state)
            counties.append(county_demo)

    return counties


# Find the county with the maximum specified attribute
def find_max_county(counties: list, attribute: str) -> CountyDemographics:
    max_county = max(counties, key=lambda x: x.income[attribute] if attribute in x.income else 0)
    return max_county


# Filter counties based on a specified attribute and threshold
def filter_counties(counties: list, attribute: str, threshold: float) -> list:
    return [county for county in counties if county.income.get(attribute, 0) >= threshold]