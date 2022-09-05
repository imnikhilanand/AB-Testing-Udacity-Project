# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 17:23:19 2022

@author: Nikhil
"""

""" Importing the libraries
"""
import pandas as pd
import numpy as np
import scipy.stats as stats

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
def is_binomial_normal(n, p):
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

# function to calualte standard deviation
def standard_error(n, p):
    return (p*(1-p)/n)**0.5

# gross conversion standard error
standard_error(400, 0.2062)

# retention standard error
standard_error(82, 0.53)

# net conversion standard error
standard_error(400, 0.1093)




""" Sanity Check """

#set alpha and p_hat
p = 0.5
alpha = 0.05

# function to calculate the standard error
def standardError (n, p):
    return (p*(1-p)/n)**0.5

# Pageviews 
n = control['Pageviews'].sum() + experiment['Pageviews'].sum()
n_control = control['Pageviews'].sum()

# uppper and lower limit of the control (or treatment) gorup proportion for Pageviews
p-(stats.norm.ppf(1-alpha/2)*standardError(n,p))
p+(stats.norm.ppf(1-alpha/2)*standardError(n,p))

# actual 
p_actual = control['Pageviews'].sum()/n

# Clicks
n = control['Clicks'].sum() + experiment['Clicks'].sum()
n_control = control['Clicks'].sum()

# uppper and lower limit of the control (or treatment) gorup proportion for Pageviews
p-(stats.norm.ppf(1-alpha/2)*standardError(n,p))
p+(stats.norm.ppf(1-alpha/2)*standardError(n,p))

# actual 
p_actual = control['Clicks'].sum()/n

# lets calculate CTP for thw two groups
CTP_control = control['Clicks'].sum()/control['Pageviews'].sum()
CTP_experiment = experiment['Clicks'].sum()/experiment['Pageviews'].sum()

# standard deviation of control group
S_control = (CTP_control*(1-CTP_control))**0.5
# standard deviation of treatment group
S_experiment = (CTP_experiment*(1-CTP_experiment))**0.5

# pooled standard deviation
SE_pooled = ((S_control)**2/control['Pageviews'].sum() + (S_experiment)**2/experiment['Pageviews'].sum())**0.5

# confidence interval
0 - (stats.norm.ppf(1-alpha/2)*SE_pooled)
0 + (stats.norm.ppf(1-alpha/2)*SE_pooled)

# actial 
p_actual = CTP_experiment - CTP_control


""" Effective test size """

# total size of the Pageviews in both control and treatment groups
total_size = control.iloc[:23]['Pageviews'].sum() + experiment.iloc[:23]['Pageviews'].sum()

''' Gross Conversion '''

# conversion rate in control group for Gross Conversion
conv_control = control.iloc[:23]['Enrollments'].sum()/control.iloc[:23]['Clicks'].sum()
conv_treatment = experiment.iloc[:23]['Enrollments'].sum()/experiment.iloc[:23]['Clicks'].sum()

# evaluating the difference between the two rates
difference_gross_conv = conv_treatment - conv_control

# calculating the standard deviation of both control and treatment gorups
S_control = (conv_control*(1-conv_control))**0.5
S_treatment = (conv_treatment*(1-conv_treatment))**0.5

# evaluating the pooled standard deviation
SE_pooled = (S_control**2/control.iloc[:23]['Clicks'].sum()+S_treatment**2/experiment.iloc[:23]['Clicks'].sum())**0.5

# calculating the difference
difference_gross_conv - (stats.norm.ppf(1-alpha/2)*SE_pooled)
difference_gross_conv + (stats.norm.ppf(1-alpha/2)*SE_pooled)

''' Net Conversion '''

# conversion rate in control group for Gross Conversion
conv_control = control.iloc[:23]['Payments'].sum()/control.iloc[:23]['Clicks'].sum()
conv_treatment = experiment.iloc[:23]['Payments'].sum()/experiment.iloc[:23]['Clicks'].sum()

# evaluating the difference between the two rates
difference_net_conv = conv_treatment - conv_control

# calculating the standard deviation of both control and treatment gorups
S_control = (conv_control*(1-conv_control))**0.5
S_treatment = (conv_treatment*(1-conv_treatment))**0.5

# evaluating the pooled standard deviation
SE_pooled = (S_control**2/control.iloc[:23]['Clicks'].sum()+S_treatment**2/experiment.iloc[:23]['Clicks'].sum())**0.5

# calculating the difference
difference_gross_conv - (stats.norm.ppf(1-alpha/2)*SE_pooled)
difference_gross_conv + (stats.norm.ppf(1-alpha/2)*SE_pooled)













    