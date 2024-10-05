#!/usr/bin/env python3
# -*- coding: utf-8 -*-

new_part1 = "We were good, we were gold \n"+\
  "Kinda dream that can't be sold \n" +\
  "We were right 'til we weren't \n"+\
  "Built a home and watched it burn\n"
new_part2 = "Paint my nails cherry red \n"+\
  "Match the roses that you left \n"+\
  "No remorse, no regret \n"+\
  "I forgive every word you said\n"
prechorus = "I didn't wanna leave you\n" +\
  "I didn't wanna lie/fight\n" +\
  "Started to cry, but then remembered I\n"
chorus1 = "I can buy myself flowers\n" +\
  "Write my name in the sand\n"+\
  "Talk to myself for hours\n"+\
  "Say things you don't understand\n"+\
  "I can take myself dancing\n"+\
  "And I can hold my own hand\n"+\
  "Yeah, I can love me better than you can\n"
chorus2 = "Can love me better\n"+\
  "I can love me better, baby"
chorus2_ending = "Can love me better\n"+\
  "I\n"
      
for iblock in range(3):
    if iblock==0:
        print(new_part1)
        print(prechorus)
        print(chorus1)
        print(chorus2)
        print(chorus2)
        print(chorus2_ending)
    if iblock==1:
        print(new_part2)
        print(prechorus)
        print(chorus1)
        print(chorus2)
        print(chorus2)
        print(chorus2)
        print(chorus2_ending)        
    if iblock==2:
        print(prechorus)
        print(chorus1)
        print(chorus2)
        print(chorus2)
        print(chorus2)
        print(chorus2_ending)        
        
