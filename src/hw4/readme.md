# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
HW4 - Sequential model optimization

from https://github.com/timm/lo/blob/6jan24/src/gate.lua#L194-L233

20 times, run gate() and catch the ouputs from `print("1...` to` `print("5...)`.
- note that each run needs to fully reset the DATA (so nothing carries over from one row to the next)
- ensure your random number seeds are different for each run

Sort that output so all the "1" rows are together, all the "2" rows are together, etc.

Answer this question, with justifications from this output:

**- Q1) Does SMO do better than the random baselines  (see prints 1,2,4)?** <br/> - Ans): Yes, SMO performs better than random baselines in most of the cases of 20 random seeds. For instance for random seed of 85, print 1 gave ['3520', '16.4', '20'], print 2 gave ['3520', '16.4', '20'] as the best output and print 4 gave [2929. , 15.48461538 , 25.38461538] which are far away from the SMO output of ['2130', '24.6', '40'] in the optimum case. This kind of behavior was observed for various random seeds as seen in the w4.out file. <br/>
**- Q2) How many y row evaluations are required for print 3?** <br/> - Ans): A total of 398 rows evaluations is needed for print 3 as we are sorting the whole 398 rows dataset to find the absolute best y-value with least d2h. <br/>

**- Q3) How does SMO do compared to absolute best (print 3)** <br/> - Ans): SMO's optimal(print 6) case performs fairly closeby to the absolute best(print 3). However, more realistically, the average case(print 5) ain't as good as the optimum case(print 6) but not bad after 14 evaluations. For instance, in the case of random seed of random seed as 82, print 3, i.e., absolute best was ['2130', '24.6', '40'], while print 5(avg best) and print 6(optimal best) came out to be [2339.387931034483, 16.528448275862075, 31.896551724137932] and ['2155', '16.5', '30'] respectively. Here print 6 is fairly close to print 3 and print 6 even though ain't as good but not bad after 14 evaluations! This pattern was seen for many random seed evaluations too. <br/>

# Steps to run
* Navigate to the repository src/hw4/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w4/w4.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
