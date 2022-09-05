# AB-Testing-Udacity-Project
This project is the Udacity's A/B Testing final course project where a hypothetical experiment was conducted to test few metrics in the hypothetical online platform.

## Experiment Design

During the experiment, the Udacity courses have two options:

1. Start Free Trail 
2. Access Course Materials

If the student clicks start free trail, the student will be asked to enter their credit card details and they will be enrolled in the free course. After 14 days, they will be automatically charged unless they cancel first.

If the student clicks access course materials, they will be able to view the videos and take the quizzes for free, but they won't be able to receive coaching support and verified certificate, and they won't be able to upload their project to get the feedback.

For the experiment, udacity wants to test a change where if the student clicks - "Start free trail", they will be asked how much time they are willing to dedicate for the course. If the student selects 5 or more hours per week, a message would appear indicating that Udacity usually requires a greater time commitment. At this point the student would have the option to either join the free trail or access the course materials for free instead.

The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time—without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

<br>

<p align="center">
	<img src="img/flow.png" alt="User Flow" width="70%">
</p>


### Metric Choice

<table>
	<tr><th>Metric</th><th>Description</th></tr>
	<tr><td>Number of Cookies</td><td>That is, number of unique cookies to view course overview page</td></tr>
	<tr><td>Number of User-Ids</td><td>That is, number of users who enroll in the free trail</td></tr>
	<tr><td>Number of Clicks</td><td>That is, number of unique cookies to click the "Start free trail" button (which happens before the free trail screener is trigger)</td></tr>
	<tr><td>Click-through-Probability</td><td>That is, number of unique cookies to click the "Start free trail" button divided by the number of cookies to view the course overview page</td></tr>
	<tr><td>Gross Conversion</td><td>That is, number of user-ids to complete checkout and enroll in the free trail divided by number of cookies to click the "Start free trail" button.</td></tr>
	<tr><td>Retention</td><td>That is, number of user-ids to remain enrolled past the 14 day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout</td></tr>
	<tr><td>Net Conversion</td><td>That is, number of user-ids to remain enrolled past the 14 day boundary (and thus make atleast 1 payment) divided by the nuber of unique cookies to click the "Start free trail" button</td></tr>
</table>

**Choosing Invariant Metrics**

1. Number of Cookies: Since the unit of diversion is Cookies, the number of cookies in both control and treatment groups will remain same.
2. Number of Clicks: Since the number of cookies that clicks the start free trail is before the "Free trail screener", the number of clicks in the two groups will remain approximately same. 
3. Click through Probability: This metric is the combination of the above two metric. So it will also remain the same.

**Choosing Evaluation Metrics**

1. Gross Conversion: (# no of user ids enrolled/# of unique daily cookies to click "start free trial" button) Since the two different groups have same number of unique cookies, but the number of cookies checking out would be different as they will be shown Trigger.
2. Retention: (# no of user ids paid/# no of user ids that enrolled) Since the two different groups will have different behavior as the users in treatment groups would be more determined to complete the course and will remain enrolled. So the retention rate would be higher for the treatment group users.
3. Net Conversion: (# no of user ids paid/# of unique daily cookies to click "start free trial" button) Since the two groups have different behavior after joining the free training, the number of users who will remain enrolled past 14 days will be higher in the treatment group.


### Measuring Standard deviation

For each of the metric you selected as an evaluation metric, make an analytical estimate of its standard deviation, given a sample size of 5000 cookies visting the course overview page. Enter each estimate in the appropriate box to 4 decimal places.

The following metric values were provided by Udacity

<table>
	<tr><th>Metric</th><th>Values</th><th>Min Values</th></tr>
	<tr><td>Number of Cookies</td><td>40,000</td><td>3000</td></tr>
	<tr><td>Number of user-ids</td><td>660</td><td>50</td></tr>
	<tr><td>Number of clicks on 'Start Free Trial'</td><td>3200</td><td>240</td></tr>
	<tr><td>Click through Probability on 'Start Free Trial'</td><td>0.08</td><td>0.01</td></tr>
	<tr><td>Gross Conversion</td><td>0.2062</td><td>0.01</td></tr>
	<tr><td>Retention</td><td>0.53</td><td>0.01</td></tr>
	<tr><td>Net Conversion</td><td>0.1093</td><td>0.0075</td></tr>
</table>

Since, the given sample size of the experiment is 5000 cookies, we can calculate the standard deviation of the probabilites on the scaled data of 5000 cookies. We will be estimating how for the sample population likely to be from the mean proportion.

<table>
	<tr><th>Metric</th><th>Values</th><th>Scaled Estimates</th><th>Min Values</th></tr>
	<tr><td>Number of Cookies</td><td>40,000</td><td>5000</td><td>3000</td></tr>
	<tr><td>Number of user-ids</td><td>660</td><td>400</td><td>50</td></tr>
	<tr><td>Number of clicks on 'Start Free Trial'</td><td>82.5</td><td>3200</td><td>240</td></tr>
	<tr><td>Click through Probability on 'Start Free Trial'</td><td>0.08</td><td>NA</td><td>0.01</td></tr>
	<tr><td>Gross Conversion</td><td>0.2062</td><td>NA</td><td>0.01</td></tr>
	<tr><td>Retention</td><td>0.53</td><td>NA</td><td>0.01</td></tr>
	<tr><td>Net Conversion</td><td>0.1093</td><td>NA</td><td>0.0075</td></tr>
</table>

We can calculate standard deviation analytically by assuming binomial distribution for Gross Conversion, Net Conversion and Retension. Since n is very large, we can assume this binomial distribution to be close to normal distribution due to Central Limit Theorem. 

To approximate a binomial distribution as a normal distribution, n*p and n*(1-p) should be greater than 5.

1. Gross Conversion: 400 * 0.2062 > 5 and 400 * (1-0.2062) > 5
  
2. Retention: 82.5 * 0.53 > 5 and 82.5 * (1-0.53) > 5

3. Net Conversion: 400 * 0.109 > 5 and 400 * (1-0.1093) > 5

<table>
	<tr><th>Metric</th><th>Values</th><th>Standard Error</th></tr>
	<tr><td>Gross Conversion</td><td>0.2062</td><td>0.02022</td></tr>
	<tr><td>Retention</td><td>0.53</td><td>0.05511</td></tr>
	<tr><td>Net Conversion</td><td>0.1093</td><td>0.0156</td></tr>
</table>

## Sizing

### Number of Samples vs. Power

The alpha value for the experiment is 0.05 and power for the expriment is given as 0.80 (by setting beta to 0.2)

Using calculator we can estimate the total pageview to be:

Gross Conversion: 25830 * 2 * 40000 / 3200 = 645750 

Retention: 39115 * 2 * 40000 / 660 = 4741213

Net Conversion: 27411 * 2 * 40000 / 3200 = 685275

### Duration vs. Exposure

Since, the daily traffic on the website is 40,000, total number of Days for the following three metric will be:

<table>
	<tr><th>Metric</th><th>Days Required</th></tr>
	<tr><td>Gross Conversion</td><td>= 645750/40000 = ~17</td></tr>
	<tr><td>Retention</td><td>= 4741213/40000 = ~119 </td></tr>
	<tr><td>Net Conversion</td><td>= 685275/40000 = ~18</td></tr>
</table>


## Experimental Analysis

So, if we perform the entire experiment and try to measure all the three metric we will be rquiring ~119 days to get the results. This would be the case when we will divert the entire traffic i.e. 100%. If we track the metrics - Gross Conversion and Net Conversion, it will be feasible. 

There are two major problems with measuring Retention:

1. We cannot perform any other expriment during the same period.

2. There are business risks for performing expriment for that long.

Net Conversion is product of Gross Conversion and Retention, we can make inference about retention from these two metrics.

There are risks associated with running experiment for too long we can divert some proportion of traffic and increase the duration of the expriment.

### Sanity Checks


### Result Analysis


**Effective Test Size**

**Sign Test**

**Summary**


### Recommendation




