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
          'number of clicks': 3200,
         }

# evaluated metric based on the factor
for i in metric:
    metric[i] = metric[i]*factor
    
# printing metric
print(metric)

# checking if we can assume the binomial to be normally distributed
def is_binomial_normal(n,p):
    if n*p>=5 and n*(1-p)>=5:
        return 'Can be assumed normally distributed'
    else:
        return 'Cannot be assumed normal'

# Gross Conversion
is_binomial_normal(400, 0.2062)

# Retention
is_binomial_normal(82.5, 0.53)

# Net Conversion
is_binomial_normal(400, 0.1093)




































    