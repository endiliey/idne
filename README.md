# idne
A way to submit your solution file to Codeforces through terminal

## Current Features:
* Submit solution to Codeforces through command-line (without going to www.codeforces.com/problem/submit/) and get result (OK/ Wrong Answer)

![Screenshot of Test Usage](img/demo1.jpg)

Proof of Working:
![Proof of Working](img/demo2.jpg)

## One time setup (pre-installation)

Go to utils/config.py, then insert your username and password
```python
username = "ababcba" # your codeforces username
password = "asdadas" # your password
```

Make sure to edit template.cpp as you wanted it to be.
```
vim template.cpp
```


## Installation (For Linux user only)

Prerequisites
-------------

I will assume that you have

* Git
* Python 2.7

Clone the repositories

```
git clone https://github.com/endiliey/idne.git
```

Set-up a Virtualenv
----------

```
pip install virtualenv
```

Create an isolated environments through virtualenv

```
cd idne
virtualenv venv
```

Activate virtualenv
```
. venv/bin/activate
```

Install all required dependencies by typing
```
pip install --editable .
```

Usage Scenario Example (+ Codeforces Parser)
----------



Example: Solving [Codeforces Round #259 (Div. 2)](http://codeforces.com/contest/454)

First, ensure that you activate the virtualenv
Activate virtualenv
```
. venv/bin/activate
```

Secondly, parse the problem using [Codeforces Parser](https://github.com/johnathan79717/codeforces-parser) (included in this repo) by

```
parse 454
```

And there will be a folder named 454-c++11, with a subfolder (e.g: A, B, C, D) inside. Assume you are solving problem A
```
cd 454-c++11/A
```

Use your favourite text editor and edit A.cpp. I use vim for this example
```
vim a.cpp
```

After confident with your solution, you can use ./test.sh to check if your solution passes the sample test
```
./test.sh
```

If it passes, you can submit with idne. The format is: idne [problem id] [filename]
```
idne 454A A.cpp
```

## ENJOY !
