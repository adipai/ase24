# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
* HW3 - Create the like(), likes() functions for ROW, SYM, NUM classes. Complete Task1 for calculating class %ages of soybean and diabetes. Implemented learn() and bayes() functions for Task2 - compute accuracies for both datasets. As part of Task 3 varied k amd m to find optimal combination for soybean. Lastly, added new test cases for DATA class, like(), likes(), learn() and bayes().<br/>

# Task 1 Result -

# Task 2 Result -

# Task 3 Result -

# Steps to run
* Navigate to the repository src/hw3/ <br/>
* Here <filename.csv> can be "diabetes.csv" or "soybean.csv" - according to the user inputs <br/>
* For normal execution, run: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> > ../../hw/w3/w3.out`
* For normal execution and run all test cases: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> --run_tc all > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> -t all > ../../hw/w3/w3.out`
* For normal execution and run a particular test case: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> --run_tc <test_name> > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> -t <test_name> > ../../hw/w3/w3.out`
* For varying k and m magic constants: <br/>
    `$ python3 main.py --file ../../Data/<filename.csv> --k 1 --m 2 > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> -k 1 -m 2 > ../../hw/w3/w3.out`
* For getting help: <br/>
  `$ python3 main.py --help > ../../hw/w3/w3.out` OR `$ python3 main.py -h > ../../hw/w3/w3.out`
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
