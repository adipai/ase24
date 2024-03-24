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

output (for auto93):

```

```

Paragraph describing the observed _explanation tax_? i.e. explanations often mean simplifying complex ideas and some explanations do not capture all the details
of the data. Which means sometimes, the conclusions we make via explanations can be worse that if we reasoned from the instances.

```

```

# Steps to run
* Navigate to the repository src/hw9/ and run the below command <br/>
  `$ python3 main.py -f ../../Data/auto93.csv > ../../hw/w8/w9.out`
  
* For running test suite, run:<br/>
  `$ python3 -m coverage run test_suite.py`

# Team members
[Rishi Singhal](https://www.linkedin.com/in/rishi-singhal1101/)<br/>
[Deepak Rajendran](https://www.linkedin.com/in/deepr41)<br/>
[Aditya Pai Brahmavar](https://www.linkedin.com/in/adityapai16/)<br/>
