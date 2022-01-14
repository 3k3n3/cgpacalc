#this program calculates cgpa

"""
GET NAME >>>> 
GET NUMBER OF COURSES >>>
GET COURSE CODE AND UNIT FOR NUMBER OF COURSES >>>
GET COURSE GRADE>>>
SUM COURSE UNIT >>>
MULTIPLY GRADE BY 5, 4, 3, 2, 1>>>
SUM MULIPLIED GRADES>>>
DIVIDE MULTIPLIED GRADES BY SUM OF COURSE UNIT>>>
ACHIEVED SET BASICS 12/8/2021
ANYTHING FROM LINE IS ADDITIONAL IMPROVEMENT!!!
ADDED DATETIME
ADDED OPTION TO ADD AND AVERAGE PREVIOUS CGPA 12/14/2021
ADD PRINT COMMENTS BASED ON CGPA SCORE
ADD FUNCTIONS FOR EACH PART OF CODE attempted 24/12/2021, 08/01/2022
messed up code, need to write new code to accomodate functions
ADD OPTION TO CATCH ERROR FROM COURSE UNITS
ADD LIMIT ON NUM_COURSES, MAX IS 20, max is 12 08/01/2022
i think the code is complete. WOW!!
"""

def init():

    import datetime
    units = [ ] #list to store units of course input from user
    courses = [ ] #list to store courses entered
    grade = [ ] #list to store grades entered 
    value = [5, 4, 3, 2, 1, 0] #grades entered in alphabets assigned a numerical value


    def student():
        global name,mat_no
        name = str(input('Enter Your Name:\n'))
        mat_no = str(input('Enter Your Matric Number(optional):\n'))
        print ('Welcome %s %s' %(name, mat_no))

    student()

    def study():
        nc_list = ['1','2','3','4','5','6','7','8','9','10','11','12']
        global num_courses
        nc = input('Enter number of courses offered:\n')
        if nc in nc_list:
            num_courses = int(nc)
        else:
            print ('Enter correct number\nNumber of courses must be less than or equal to 12')
            study()
        #print ('number of courses offered is %d' %num_courses)

    study()

    def score():
        cu_list = ['2','3','4','6']
        global course_code, course_unit
        for i in range(num_courses): #this loops based on the number of courses
            course_code, course_unit, gp = input('Enter Course Code %d:\n'%(i+1)), input('Enter Course Unit %d:\n'%(i+1)), input('Enter your grade score %d:\n'%(i+1))
            if course_unit in cu_list:
                course_unit = int(course_unit)
                units.append(course_unit)
                courses.append(course_code)
            else:
                print('Incorrect!\nEnter correct Course Unit')
                score()
            grade_point = gp.lower() #converts imput to lower case alphabets as used in code
            if grade_point == 'a':
                grade.append(value[0] * course_unit)
            elif grade_point == 'b':
                grade.append(value[1] * course_unit)
            elif grade_point == 'c':
                grade.append(value[2] * course_unit)
            elif grade_point == 'd':
                grade.append(value[3] * course_unit)
            elif grade_point == 'e':
                grade.append(value[4] * course_unit)
            elif grade_point == 'f':
                grade.append(value[5] * course_unit)
            else: print ('Invalid option entered')
            #print(sum(grade))
            #print(sum(units))

    score()

    def semester():
        x = sum(grade) #total grades
        y = sum(units) #total units
        z = (x/y) #GPA AT LAST!!!
        print('Hello %s, your current GPA is %.2f!' %(name,z))
        prev_sem_cgpa = input('Previous Semester CGPA available?\nIf Yes, enter "Y" or "N" if No\n')
        prev_sem_cgpa = prev_sem_cgpa.upper()
        if prev_sem_cgpa == 'Y':
            last_sem = float(input('Enter previous CGPA\n'))

            if last_sem == False:
                semester()
            else:
                c = (z + last_sem)/2
                print('Congratulations %s %s, your CGPA is %.2f!' %(name,mat_no,c))
        elif prev_sem_cgpa == 'N':
            print('Hello %s %s, your CGPA is %.2f!' %(name,mat_no,z))
        else: print('Not quite sure...?')
        time = datetime.datetime.now()
        print(time.strftime('%c'))

    semester()
    
init()