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

- does SMO do better than the random baselines  (see prints 1,2,4)?
- how many y row evaluations are required for print 3?
- how does SMO do compared to absolute best (print 3)<br/>

# Steps to run
* Navigate to the repository src/hw4/ <br/>


* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
