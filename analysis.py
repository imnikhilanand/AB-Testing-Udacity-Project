# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:23:19 2022

@author: Nikhil
"""


"""
 estimating different metrics based on the sample size of 5000 cookies 
"""

# factor given in question
factor = 5000/40000

# metric given 
metric = {
          'number of_cookie': 40000,
          'number of user ids': 660,
          'number of clicks': 3200
         }

# evaluated metric based on the factor
for i in metric:
    metric[i] = metric[i]*factor
    
# printing metric
print(metric)


































    