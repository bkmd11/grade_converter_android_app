""" A grade calculator that takes depth of knowledge grade and translates it into a percentage,
based on a lopsided scale, so that a more traditional grade can be entered into powerschool"""
import numpy

"""
PD = 3.5-4 = 92-100    
P = 2.5-3.4 = 76-91    
BP = 2-2.4 = 66-75     
I = 1.5-1.9 = 55-65    
N = 0-1.4 = 0-54        

"""

"""Setting my constant lists to reflect the score ranges referenced above"""
PD_TRADITIONAL_GRADE_RANGE_LIST = [i for i in numpy.arange(92, 100, .159).round(decimals=1)]
PD_GRADE_RANGE = [i for i in numpy.arange(3.5, 4.01, .01).round(decimals=2)]

P_TRADITIONAL_GRADE_RANGE_LIST = [i for i in numpy.arange(76, 91.3, .167).round(decimals=1)]
P_GRADE_RANGE = [i for i in numpy.arange(2.5, 3.41, .01).round(decimals=2)]

BP_TRADITIONAL_GRADE_RANGE_LIST = [i for i in numpy.arange(66, 75.3, .225).round(decimals=1)]
BP_GRADE_RANGE = [i for i in numpy.arange(2, 2.41, .01).round(decimals=2)]

I_TRADITIONAL_GRADE_RANGE_LIST = [i for i in numpy.arange(55, 65.2, .25).round(decimals=1)]
I_GRADE_RANGE = [i for i in numpy.arange(1.5, 1.91, .01).round(decimals=2)]

N_TRADITIONAL_GRADE_RANGE_LIST = [i for i in numpy.arange(0, 54.2, .386).round(decimals=1)]
N_GRADE_RANGE = [i for i in numpy.arange(0, 1.41, .01).round(decimals=2)]


def check_index(input_grade, depth_of_knowledge_grade_list):
    """Takes a depth of knowledge grade and compares its place in a list index to a corresponding list
    to convert into a traditional grade"""
    index_num = depth_of_knowledge_grade_list.index(input_grade)

    return index_num


def grade_converter(depth_of_knowledge_grade):
    """Takes the grade level descriptor and the DKG and finds the percentage range it will be in"""
    if 3.5 <= depth_of_knowledge_grade <= 4:
        grade_index = check_index(depth_of_knowledge_grade, PD_GRADE_RANGE)
        grade_percentage = PD_TRADITIONAL_GRADE_RANGE_LIST[grade_index]

    elif 2.5 <= depth_of_knowledge_grade <= 3.49:
        grade_index = check_index(depth_of_knowledge_grade, P_GRADE_RANGE)
        grade_percentage = P_TRADITIONAL_GRADE_RANGE_LIST[grade_index]

    elif 2 <= depth_of_knowledge_grade <= 2.49:
        grade_index = check_index(depth_of_knowledge_grade, BP_GRADE_RANGE)
        grade_percentage = BP_TRADITIONAL_GRADE_RANGE_LIST[grade_index]

    elif 1.5 <= depth_of_knowledge_grade <= 1.99:
        grade_index = check_index(depth_of_knowledge_grade, I_GRADE_RANGE)
        grade_percentage = I_TRADITIONAL_GRADE_RANGE_LIST[grade_index]

    elif 0 <= depth_of_knowledge_grade <= 1.49:
        grade_index = check_index(depth_of_knowledge_grade, N_GRADE_RANGE)
        grade_percentage = N_TRADITIONAL_GRADE_RANGE_LIST[grade_index]

    else:
        grade_percentage = 'Grade is out of range'

    return grade_percentage


def make_list(string_of_grades):
    """Converts the string of grades entered into a list and makes it a float"""
    grade_list = string_of_grades.split(', ')

    count = 0
    for i in grade_list:
        grade_list[count] = float(i)
        count += 1

    return grade_list


def find_average(list_of_grades):
    """ Calculates the average from a list"""
    avg = 0
    for i in list_of_grades:
        avg += i

    return round(avg / len(list_of_grades), 2)


def check_range(grade):
    """Assures the grade entered is within the expected range of 0 - 4"""
    if grade <= 4.0:
        return grade
    else:
        return f'{grade} is out of range'
