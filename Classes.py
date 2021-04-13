# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 22:13:16 2021

@author: pc
"""

class studentClass():
    def admission(self):
        print("studentClass admission")

    def exam(self, subject):
        print("studentClass exam" + subject)


class teacherClass(studentClass):
    def exam(self):
        print("teacherClass exam")

    def admission(self):
        studentClass.admission(self)
        print("teacherClass admission")


def main():
    c = studentClass()
    c.admission()
    c.exam("Maths")
    
    c2 = teacherClass()
    c2.admission()
    c2.exam()
    

if __name__ == "__main__":
    main()
