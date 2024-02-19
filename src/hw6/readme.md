# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
### Cluster output
Recursive random projections, generating clusters at each leaf. Report centroid of each leaf.

```
﻿Task1 output:
|.. 
|.. |.. 
|.. |.. |.. 
|.. |.. |.. |.. 		{4.23, 110.5, 0, 81.15, 3, 2280.27, 15.82, 33.46}
|.. |.. |.. |.. 		{4.0, 97.12, 0, 78.4, 3, 2177.68, 16.5, 31.2}
|.. |.. |.. 
|.. |.. |.. |.. 		{4.08, 100.12, 0, 73.38, 3, 2201.77, 16.32, 26.15}
|.. |.. |.. |.. 		{4.0, 117.21, 0, 78.88, 1, 2356.13, 15.77, 29.58}
|.. |.. 
|.. |.. |.. 
|.. |.. |.. |.. 		{4.0, 102.0, 0, 72.12, 2, 2286.46, 16.77, 26.15}
|.. |.. |.. |.. 		{4.21, 112.08, 0, 76.25, 2, 2505.25, 15.7, 26.67}
|.. |.. |.. 
|.. |.. |.. |.. 		{4.48, 124.16, 0, 78.08, 2, 2512.56, 17.52, 31.6}
|.. |.. |.. |.. 		{4.0, 121.52, 0, 73.63, 1, 2348.25, 17.33, 25.42}
|.. 
|.. |.. 
|.. |.. |.. 
|.. |.. |.. |.. 		{4.15, 139.69, 0, 81.62, 1, 2628.88, 16.42, 29.62}
|.. |.. |.. |.. 		{6.08, 223.56, 0, 79.0, 1, 3248.64, 16.45, 22.0}
|.. |.. |.. 
|.. |.. |.. |.. 		{6.32, 241.04, 0, 76.08, 1, 3398.24, 17.31, 20.0}
|.. |.. |.. |.. 		{6.0, 231.67, 0, 72.58, 1, 3144.25, 15.96, 20.0}
|.. |.. 
|.. |.. |.. 
|.. |.. |.. |.. 		{8.0, 320.42, 0, 71.65, 1, 3936.08, 12.81, 14.23}
|.. |.. |.. |.. 		{8.0, 391.29, 0, 71.08, 1, 4290.0, 11.4, 11.67}
|.. |.. |.. 
|.. |.. |.. |.. 		{8.0, 317.72, 0, 77.44, 1, 3916.88, 13.96, 18.8}
|.. |.. |.. |.. 		{8.0, 366.61, 0, 74.39, 1, 4467.65, 12.77, 13.48}

                		{5.45, 193.43, 0, 76.01, 1, 2970.42, 15.57, 23.84}
                	{Clndrs, Volume, HpX, Model, origin, Lbs-, Acc+, Mpg+}
evals:  16
```

### Optimization Output
## Single Descent:
Just prune half as you go. And print the surviving examples:
```
Task2 output: 
centroid of output cluster: 
{3.96, 95.19, 0, 79.62, 3, 2113.38, 16.72, 33.85} {5.56, 200.29, 0, 75.76, 1, 3030.33, 15.49, 23.15}
evals:  5
```

## Double Tap:
Pass1: run single descent optimization down to

- Cluster down to select 32 items
- Take those survivors and then cluster down to four
- Print the median and best found in that four

```
Task3 output: 
median and best found in that four: 
{4.0, 92.33, 0, 76.33, 2, 1950.67, 15.37, 33.33} {5.54, 199.01, 0, 75.99, 1, 3002.0, 15.56, 23.66}
evals:  10
```

# Steps to run
* Navigate to the repository src/hw4/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w7/w7.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
