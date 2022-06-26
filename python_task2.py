def numbers(Students):
    subject=[]
    num={}
    for Student in Students:
        for course in Student:
            if course not in num:
                num[course]=0
            num[course]=num[course]+1
    return num
def popular(num):
    popular_course,enroll_max= None,-1
    for course ,enroll in num.items():
        if enroll > enroll_max:
            popular_course, enroll_max =course,enroll
    return popular_course

course_list=numbers([["math","phy","chem","cs"],["chem","phy","cs"],["math",'phy'],['history','phy']])
print(course_list )
print(popular(course_list))