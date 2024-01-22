# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
* HW3 - Create the like(), likes() functions for ROW, SYM, NUM classes. Complete Task1 for calculating class %ages of soybean and diabetes. Implemented learn() and bayes() functions for Task2 - compute accuracies for both datasets. As part of Task 3 varied k amd m to find optimal combination for soybean. Lastly, added new test cases for DATA class, like(), likes(), learn() and bayes().<br/>

# Task 1 Result -
We computed the class-wise %age for both diabetes and soybean dataset and stored them in an ascii table in task1.out [file](https://github.com/adipai/ase24/blob/main/hw/w3/task1.out)

# Task 2 Result - 
We implemented the like(), likes(), learn() and bayes() function to implement the Naive-Bayes classifier by modifying row.py, sym.py, num.py, main.py, config.py files.

# Task 3 Result -
We used the default k and m values for diabetes dataset as asked in the question and got 73.12% accuracy as seen in task3.out [file](https://github.com/adipai/ase24/blob/main/hw/w3/task3.out)

# Task 4 Result -
We varied k - [0,1,2,3] and m - [0,1,2,3] for soybean dataset and got the below accuracies. Also stored them as an ascii table in task4.out [file](https://github.com/adipai/ase24/blob/main/hw/w3/task4.out). We observed that best accuracy of 85.46% was achieved for k = 3 and m = 1 and the reason behind the same is (add reason on Monday)

# Steps to run
* Navigate to the repository src/hw3/ <br/>
* Here <filename.csv> can be "diabetes.csv" or "soybean.csv" - according to the user inputs <br/>
* For normal execution, run: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> > ../../hw/w3/w3.out`
* For normal execution and run all test cases: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> --run_tc all > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> -t all > ../../hw/w3/w3.out`
* For normal execution and run a particular test case: <br/>
  `$ python3 main.py --file ../../Data/<filename.csv> --run_tc <test_name> > ../../hw/w3/w3.out` OR `$ python3 main.py -f ../../Data/<filename.csv> -t <test_name> > ../../hw/w3/w3.out`
  * For calculating accuracy for diabetes: <br/>
    `$ python3 main.py --file ../../Data/diabetes.csv > ../../hw/w3/task3.out` OR `$ python3 main.py -f ../../Data/diabetes.csv > ../../hw/w3/task3.out`
* For varying k and m magic constants for soybean: <br/>
    `$ python3 main.py --file ../../Data/soybean.csv --k 1 --m 2 > ../../hw/w3/task4.out` OR `$ python3 main.py -f ../../Data/soybean.csv -k 1 -m 2 > ../../hw/w3/task4.out`
* For getting help: <br/>
  `$ python3 main.py --help > ../../hw/w3/w3.out` OR `$ python3 main.py -h > ../../hw/w3/w3.out`
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
