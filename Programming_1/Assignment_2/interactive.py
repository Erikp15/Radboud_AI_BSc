#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:49:59 2024

@author: bryancsouza
"""

question1 = "Are you a first year student? [yes/no]"
question2 = "Do you sometimes wonder if you are on the right path? [yes/no]"
answer1 = "Entering the university often goes together with developping more autonomy in your life, and thus being the narrators of your own story. This is challenging at first, but very emancipating later on!"

answer2 = "Great! In this class, beyond learning programming, I hope you will be stimulated to constantly reflect on your views and actions on the world."

final_message = "If you wanna know more about that, check the Project Practice of this week."

answer = input(question1)
if answer == "yes":
    answer = input(question2)
    if answer == "yes":
         print(answer1)
    elif answer == "no":
        print(answer2)
else:
    print("All praise the error message! :)")
print(final_message)

error_message = "Invalid answer"