# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# Week9: Rules

Using the code presented in class (ported to Python):

- build $N$ rules (for auto93) using just the labelled data 
- for each of the rules:
  - pretty print the rule, combining adjacent rangees
      - so NOT $1 \le x < 2$ or $2 \le x < 3$
      - but $1 \le x < 3$  
  - apply those rules to the as-yet-unlabelled data
    - for the rows selected by each rule
      - report the mid point of selected rows (see example below)
      - report rule score (see the function l.score in mylo.lua)

**Our Output (for auto93):**

```
score  mid selected                                              rule
----   ------------------------------------------------------    -----------------------------------------------------------------
1.0    {3.97, 91.19, 71.19, 77.71, 3, 2052.45, 16.94, 32.9}      Volume < 112.0 and origin == 3.0
0.89   {4.12, 100.54, 77.54, 77.27, 3, 2179.44, 16.51, 30.98}    origin == 3.0
0.89   {3.98, 93.74, 70.31, 76.78, 3, 2071.1, 17.07, 32.54}      Volume < 112.0
0.67   {3.88, 93.88, 75.13, 79.88, 3, 2187.38, 16.22, 35.0}      origin == 3.0 and 79.0 <= Model < 81.0
0.67   {4.0, 98.33, 70.56, 79.67, 2, 2113.0, 15.8, 35.56}        89.0 <= Volume < 112.0 and 79.0 <= Model < 81.0
0.67   {4.0, 98.42, 73.11, 78.05, 3, 2105.05, 16.18, 31.58}      89.0 <= Volume < 112.0 and origin == 3.0
0.67   {4.0, 102.0, 71.33, 80.0, 3, 2135.0, 15.33, 33.33}        89.0 <= Volume < 112.0 and origin == 3.0 and 79.0 <= Model < 81.0
0.67   {3.92, 93.15, 71.54, 79.69, 3, 2129.0, 16.23, 35.38}      Volume < 112.0 and 79.0 <= Model < 81.0
0.67   {3.86, 90.29, 72.71, 79.86, 3, 2152.14, 16.4, 34.29}      Volume < 112.0 and origin == 3.0 and 79.0 <= Model < 81.0
0.56   {4.82, 157.43, 90.93, 79.57, 1, 2679.04, 16.0, 30.0}      79.0 <= Model < 81.0
```

**Paragraph describing the observed _explanation tax_? i.e. explanations often mean simplifying complex ideas and some explanations do not capture all the details
of the data. Which means sometimes, the conclusions we make via explanations can be worse that if we reasoned from the instances.**

Explanations often aim to simplify complex ideas, but sometimes, they may oversimplify or omit crucial details of the data. This can lead to conclusions that are not as accurate or insightful as those derived from directly reasoning from the instances. The process of simplifying complex concepts for explanation purposes, while valuable for comprehension, can sometimes result in a loss of nuance or depth in the analysis. Therefore, it's important to carefully consider the limitations of explanations and to supplement them with thorough analysis and reasoning based on the complete dataset.

# Steps to run
* Navigate to the repository src/hw9/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w9/w9.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
