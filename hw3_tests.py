from multiprocessing.forkserver import read_signed

import data
import build_data
import unittest
import hw3
import math

# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total1(self):
        input = full_data
        result = hw3.population_total(input)
        expected = 318857056
        self.assertEqual(expected, result)

    def test_population_total2(self):
        input = reduced_data
        result = hw3.population_total(input)
        expected = 655813
        self.assertEqual(expected, result)

    # Part 2
    # test filter_by_state
    def test_filter_by_state1(self):
        input = reduced_data
        result = hw3.filter_by_state(input, 'CA')
        expected = [reduced_data[2], reduced_data[3]]
        self.assertEqual(expected, result)

    def test_filter_by_state2(self):
        input = full_data
        result = hw3.filter_by_state(input, 'CA')
        result2 = len(result)
        expected = 58
        self.assertEqual(expected, result2)

    # Part 3
    # test population_by_education
    def test_population_by_education1(self):
        input = [reduced_data[2]]
        result = hw3.population_by_education(input, "Bachelor's Degree or Higher")
        expected = 87911.145
        self.assertEqual(expected, result)

    def test_population_by_education2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_education(input, "Bachelor's Degree or Higher")
        expected = 20400.226
        end = math.isclose(result,expected)
        self.assertEqual(True,end)

    # test population_by_ethnicity
    def test_population_by_ethnicity1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_ethnicity(input, 'Two or More Races')
        expected = 2724.626
        end = math.isclose(result, expected)
        self.assertEqual(True, end)

    def test_population_by_ethnicity2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_by_ethnicity(input, 'Hispanic or Latino')
        expected = 5629.364
        end = math.isclose(result, expected)
        self.assertEqual(True, end)

    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.population_below_poverty_level(input)
        expected = 19165.589
        end = math.isclose(expected,result)
        self.assertEqual(True,end)

    def test_population_below_poverty_level2(self):
        input = []
        result = hw3.population_below_poverty_level(input)
        expected = 0
        end = math.isclose(expected,result)
        self.assertEqual(True,end)

    # Part 4
    # test percent_by_education
    def test_percent_by_education1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_education(input, "Bachelor's Degree or Higher")
        expected = 17.4224
        end = math.isclose(expected, result, abs_tol= 0.0001, rel_tol= 0.0001)
        self.assertEqual(end, True)

    def test_percent_by_education2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_education(input, 'High School or Higher')
        expected = 83.8085
        end = math.isclose(expected, result, abs_tol= 0.0001, rel_tol= 0.0001)
        self.assertEqual(end, True)

    # test percent_by_ethnicity
    def test_percent_by_ethnicity1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_ethnicity(input, 'Two or More Races')
        expected = 2.32691
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)
        self.assertEqual(end,True)

    def test_percent_by_ethnicity2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_by_ethnicity(input, 'Hispanic or Latino')
        expected = 4.80764
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)
        self.assertEqual(end,True)

    # test percent_below_poverty_level
    def test_percent_below_poverty_level1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.percent_below_poverty_level(input)
        expected = 16.368
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)

    def test_percent_below_poverty_level2(self):
        input = []
        result = hw3.percent_below_poverty_level(input)
        expected = 0
        end = math.isclose(expected, result, abs_tol= 0.00001, rel_tol= 0.00001)

    # Part 5
    # test education_greater_than
    def test_education_greater_than1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_greater_than(input, "Bachelor's Degree or Higher", 60.0)
        expected = []
        self.assertEqual(expected, result)

    def test_education_greater_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_greater_than(input, 'High School or Higher', 60.0)
        expected = [reduced_data[0], reduced_data[1]]
        self.assertEqual(expected, result)

    # test education_less_than
    def test_education_less_than1(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_less_than(input, "Bachelor's Degree or Higher", 60.0)
        expected = [reduced_data[0], reduced_data[1]]
        self.assertEqual(expected, result)

    def test_education_less_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.education_less_than(input, 'High School or Higher', 60.0)
        expected = []
        self.assertEqual(expected, result)

    # test ethnicity_greater_than
    def test_ethnicity_greater_than1(self):
        input = reduced_data
        result = hw3.ethnicities_greater_than(input, 'Hispanic or Latino', 10.0)
        expected = [reduced_data[2], reduced_data[3]]
        self.assertEqual(expected, result)

    def test_ethnicity_greater_than2(self):
        input = reduced_data
        result = hw3.ethnicities_greater_than(input, 'Two or More Races', 2.0)
        expected = [reduced_data[1], reduced_data[2], reduced_data[3], reduced_data[4], reduced_data[6]]
        self.assertEqual(expected, result)

    # test ethnicity_less_than
    def test_ethnicity_less_than1(self):
        input = reduced_data
        result = hw3.ethnicities_less_than(input, 'Hispanic or Latino', 10.0)
        expected = [reduced_data[0], reduced_data[1], reduced_data[4], reduced_data[5], reduced_data[6]]
        self.assertEqual(expected, result)

    def test_ethnicity_less_than2(self):
        input = reduced_data
        result = hw3.ethnicities_less_than(input, 'Two or More Races', 2.0)
        expected = [reduced_data[0], reduced_data[5]]
        self.assertEqual(expected, result)

    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than1(self):
        input = reduced_data
        result = hw3.below_poverty_level_greater_than(input, 15.0)
        expected = [reduced_data[1], reduced_data[3], reduced_data[4], reduced_data[5]]
        self.assertEqual(expected, result)

    def test_below_poverty_level_greater_than2(self):
        input = []
        result = hw3.below_poverty_level_greater_than(input, 15.0)
        expected = []
        self.assertEqual(expected, result)

    # test below_poverty_level_less_than
    def test_below_poverty_level_less_than1(self):
        input = reduced_data
        result = hw3.below_poverty_level_less_than(input, 15.0)
        expected = [reduced_data[0], reduced_data[2], reduced_data[6]]
        self.assertEqual(expected, result)

    def test_below_poverty_level_less_than2(self):
        input = [reduced_data[0], reduced_data[1]]
        result = hw3.below_poverty_level_less_than(input, 15.0)
        expected = [reduced_data[0]]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
