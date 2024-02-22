# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
### Get Distance Working

We load `auto93.csv`, use the first row of `rows`, sort
the other rows by their distance to that first row, then print:

- every 30th row
- the distance from that 30th row back to that first row.

We obtain the following output:

``` 
Task 1: Get Distance Working:

1 ['8', '304', '193', '70', '1', '4732', '18.5', '10'] 0.0
31 ['8', '318', '150', '73', '1', '3777', '12.5', '20'] 0.13
61 ['8', '429', '198', '73', '1', '4952', '11.5', '10'] 0.2
91 ['6', '232', '100', '73', '1', '2789', '15', '20'] 0.25
121 ['6', '225', '95', '75', '1', '3264', '16', '20'] 0.31
151 ['8', '351', '138', '79', '1', '3955', '13.2', '20'] 0.38
181 ['4', '91', '70', '71', '1', '1955', '20.5', '30'] 0.49
211 ['4', '151', '90', '79', '1', '2556', '13.2', '30'] 0.58
241 ['4', '151', '90', '82', '1', '2950', '17.3', '30'] 0.67
271 ['4', '121', '110', '73', '2', '2660', '14', '20'] 0.69
301 ['4', '115', '95', '75', '2', '2694', '15', '20'] 0.72
331 ['4', '97', '67', '77', '3', '1985', '16.4', '30'] 0.75
361 ['4', '98', '76', '80', '2', '2144', '14.7', '40'] 0.81
391 ['4', '105', '74', '82', '2', '1980', '15.3', '40'] 0.85

```

### Get "Far" working

Using the fastmap heuristic, we find two points that are .95 far each other. We obtained the following Y evaluations:


```
Task 2: Get Far Working: 

far1:  ['3', '80', '110', '77', '3', '2720', '13.5', '20']
far2:  ['8', '400', '170', '71', '1', '4746', '12', '10']
distance:  0.8564052187549309
Attempts:  100
```

# Steps to run
* Navigate to the repository src/hw4/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w5/w5.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
