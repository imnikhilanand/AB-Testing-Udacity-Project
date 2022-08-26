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

*Fig 1. Flow of users on Udacity Course Description Page*


### Metric Choice

**Choosing Invariant Metrics**

**Choosing Evaluation Metrics**


### Measuring Standard deviation



## Sizing

### Number of Samples vs. Power


### Duration vs. Exposure

## Experimental Analysis


### Sanity Checks

### Result Analysis

**Effective Test Size**

**Sign Test**

**Summary**


### Recommendation




