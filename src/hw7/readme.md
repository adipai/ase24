# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
### Part 1 (no stats)

Reproduce the following output.

Before summarizing the results of many runs, first show details (very useful for debugging).

In the following we show baseline centroids (mid) and variability around that centroid (div). We then run SMO 20 times (smo9)with a budget of 9 (peek at 4 to find initial best and rest, then look at five more).

Then we compare to "just grab any 50 at random" (any50).

Finally, we abandoned all the principles of this subject and evaluated everything (100%).

```
date:26/02/2024 10:15:30
file:../../Data/auto93.csv
repeat:20
seed:31210.0
rows:398
cols:8
names			['Clndrs'  'Volume'   'HpX'    'Model'   'origin'   'Lbs-'    'Acc+'   'Mpg+']  	d2h-
Mid			[5.45      193.43     104.47   76.01     1          2970.42   15.57    23.84]   	0.56
Div			[1.7       104.27     38.49    3.7       1.33       846.84    2.76     8.34]    	0.16
#
smo9			[4         97         52       82        2          2130      24.6     40]      	0.17
smo9			[4         90         48       78        2          1985      21.5     40]      	0.19
smo9			[4         72         69       71        3          1613      18       40]      	0.27
smo9			[4         85         52       76        1          2035      22.2     30]      	0.31
smo9			[4         98         70       82        1          2125      17.3     40]      	0.31
smo9			[4         97         46       73        2          1950      21       30]      	0.32
smo9			[4         91         70       71        1          1955      20.5     30]      	0.33
smo9			[4         96         69       72        2          2189      18       30]      	0.38
smo9			[4         112        88       82        1          2395      18       30]      	0.39
smo9			[4         112        88       82        1          2395      18       30]      	0.39
smo9			[4         120        88       82        3          2160      14.5     40]      	0.39
smo9			[4         120        75       80        3          2542      17.5     30]      	0.41
smo9			[4         79         67       74        2          2000      16       30]      	0.42
smo9			[4         98         68       78        1          2155      16.5     30]      	0.42
smo9			[4         79         67       74        2          1963      15.5     30]      	0.43
smo9			[4         97         75       75        3          2171      16       30]      	0.43
smo9			[4         100        '?'      81        2          2320      15.8     30]      	0.44
smo9			[4         107        86       76        2          2464      15.5     30]      	0.45
smo9			[4         135        84       81        1          2385      12.9     30]      	0.52
smo9			[4         90         75       74        2          2108      15.5     20]      	0.54
#
any50			[4         79         67       74        3          1950      19       30]      	0.36
any50			[4         91         69       79        2          2130      14.7     40]      	0.39
any50			[4         120        74       81        3          2635      18.3     30]      	0.4
any50			[4         85         70       76        3          1990      17       30]      	0.4
any50			[4         104        95       70        2          2375      17.5     30]      	0.4
any50			[4         79         67       74        2          1963      15.5     30]      	0.43
any50			[4         122        96       77        1          2300      15.5     30]      	0.45
any50			[4         98         60       76        1          2164      22.1     20]      	0.45
any50			[4         97         78       74        2          2300      14.5     30]      	0.47
any50			[6         225        105      73        1          3121      16.5     20]      	0.57
any50			[4         119        97       78        3          2405      14.9     20]      	0.57
any50			[6         231        105      77        1          3425      16.9     20]      	0.59
any50			[4         121        98       75        2          2945      14.5     20]      	0.6
any50			[4         121        98       75        2          2945      14.5     20]      	0.6
any50			[6         258        120      78        1          3410      15.1     20]      	0.62
any50			[6         231        165      78        1          3445      13.4     20]      	0.66
any50			[8         304        150      70        1          3433      12       20]      	0.69
any50			[8         360        150      79        1          3940      13       20]      	0.71
any50			[8         302        137      73        1          4042      14.5     10]      	0.79
any50			[8         400        175      71        1          4464      11.5     10]      	0.87
#
100%			[4         97         52       82        2          2130      24.6     40]      	0.17
```
# Steps to run
* Navigate to the repository src/hw7/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w8/w8.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
