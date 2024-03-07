# Automated Software Engineering - Spring 24 (Group1)
Codebase for CSC-591-(021) Automated Software Engineering course @ NCSU, group 1.

# About
## Finding interesting ranges

For auto93, our RRP finds 24 _best_ so I picked  3\*24=72_rest_. 

Next, for all the numeric columns, divide them into bins of size _(hi - lo)/16_ and count how often
attribute values fall into each of those bins.

Now sort the bins and look for adjacent bins that can be merged

## Merge Rules

We got the following ranges:

```

PART - 1

{'at': 1, 'scored': 0, 'txt': 'Clndrs', 'x': {'hi': '4', 'lo': -inf}, 'y': {'HATE': 35, 'LIKE': 24}}
{'at': 1, 'scored': 0, 'txt': 'Clndrs', 'x': {'hi': inf, 'lo': '4'}, 'y': {'HATE': 37}}

{'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': '98', 'lo': -inf}, 'y': {'HATE': 13, 'LIKE': 15}}
{'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': '200', 'lo': '98'}, 'y': {'HATE': 21, 'LIKE': 1}}
{'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': '360', 'lo': '200'}, 'y': {'HATE': 25}}
{'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': inf, 'lo': '360'}, 'y': {'HATE': 13, 'LIKE': 8}}

{'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': '79', 'lo': -inf}, 'y': {'HATE': 56}}
{'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': '80', 'lo': '79'}, 'y': {'HATE': 4, 'LIKE': 8}}
{'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': '81', 'lo': '80'}, 'y': {'HATE': 4, 'LIKE': 9}}
{'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': inf, 'lo': '81'}, 'y': {'HATE': 8, 'LIKE': 7}}

{'at': 5, 'scored': 0, 'txt': 'origin', 'x': {'hi': '1', 'lo': '1'}, 'y': {'HATE': 45}}
{'at': 5, 'scored': 0, 'txt': 'origin', 'x': {'hi': '2', 'lo': '2'}, 'y': {'HATE': 15}}
{'at': 5, 'scored': 0, 'txt': 'origin', 'x': {'hi': '3', 'lo': '3'}, 'y': {'HATE': 12, 'LIKE': 24}}
```

That is, we have $2+4+5+3=13$ ranges, so we $2^{13}-1=8191$ possible rules-- each of which
we have to test on $24+72=96$ rows.  So lets reduce that search space.

## Pruning Ranges

Those ranges can score and sort and pruned as follows. If a range is found in LIKE of the _best_ rows
and _HATE_ or the _rest_ rows, then score is _LIKE\*LIKE/(LIKE+HATE)_.

Here are the ranges, sorted (ignoring anything with less than 10% of max score). 

```
PART - 2

#scores:

0.86 {'at': 5, 'scored': 0, 'txt': 'origin', 'x': {'hi': '3', 'lo': '3'}, 'y': {'HATE': 12, 'LIKE': 24}}
0.67 {'at': 1, 'scored': 0, 'txt': 'Clndrs', 'x': {'hi': '4', 'lo': -inf}, 'y': {'HATE': 35, 'LIKE': 24}}
0.48 {'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': '98', 'lo': -inf}, 'y': {'HATE': 13, 'LIKE': 15}}
0.33 {'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': '81', 'lo': '80'}, 'y': {'HATE': 4, 'LIKE': 9}}
0.29 {'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': '80', 'lo': '79'}, 'y': {'HATE': 4, 'LIKE': 8}}
0.22 {'at': 2, 'scored': 0, 'txt': 'Volume', 'x': {'hi': inf, 'lo': '360'}, 'y': {'HATE': 13, 'LIKE': 8}}
0.21 {'at': 4, 'scored': 0, 'txt': 'Model', 'x': {'hi': inf, 'lo': '81'}, 'y': {'HATE': 8, 'LIKE': 7}}
{'HATE': 72, 'LIKE': 24}
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
