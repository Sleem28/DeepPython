from Student import Student

if __name__ == '__main__':
    student = Student('Ali', 'Baba', 'matters.csv')
    # bad_student = Student('R2', 'D2', 'matters.csv')  # caught the exception

    # student.set_grade('phisics', 8) # caught the exception
    student.set_grade('phisics', 3)
    student.set_grade('phisics', 2)
    student.set_grade('biology', 2)
    student.set_grade('chemistry', 2)
    student.set_grade('geography', 2)
    student.set_test_grade('phisics', 10)
    # student.set_test_grade('phisics', 1023) # caught the exception
    student.set_test_grade('phisics', 63)
    student.set_test_grade('phisics', 16)
    student.get_average_grade_by_tests('phisics')
    student.get_average_grade_by_all_matters()

