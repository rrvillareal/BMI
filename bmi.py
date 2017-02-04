# -*- coding: utf-8 -*-

def main():
    print ("Find out your body mass index! ")
    metric = int(input("If used metric system press 1, if not press 2."))
    if metric == 1:
        height = float(input( "What is your height in METERS?: "))
        weight = float(input("What is your weight in KILOS?: "))
        answer = Metric(height, weight)
        print("your BMI is: ", round(answer, 1))
    else:
         print("Ex/ 1 Foot = 12 Inches!")
         height = float(input( "What is your height in INCHES?: "))
         weight = int(input("What is your weight in POUNDS?: ")) 
         answer = English(height, weight)
         print("Your BMI is: ", round(answer,1))
         print("Your dianoses is: ", Diagnoses(answer))
        
def Metric(height, weight):
    BMI = (weight/height/height)
    return BMI

def English(height, weight):
    BMIA = ((weight/height/height)*703) 
    return BMIA
    
def Diagnoses(answer):
    if answer <= 16:
        answer = "severly thin"
        return answer
    elif answer >= 16 and answer <=17:
        answer = "Moderate Thiness"
        return answer
    elif answer >= 17 and answer <= 18.5:
        answer = "Mile Thiness"
        return answer
    elif answer >= 18.5 and answer <= 24.5:
        answer = "Moderate Range"
        return answer
    elif answer >= 24.5 and answer <= 30:
        answer = "Over Weight"
        return answer 
    elif answer >= 30 and answer <= 35:
        answer = "Obese Class 1 (Moderate)"
        return answer
    else:
        answer = "Obese Class 2 (severe)"
        return answer
        
