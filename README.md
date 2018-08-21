# idne
A way to submit your solution file to Codeforces through terminal

![preview GIF](https://github.com/endiliey/idne/blob/master/preview.gif?raw=true)

## Installation

Clone the repositories
```
git clone https://github.com/endiliey/idne.git
```

Install all required dependencies in an isolated environment

```bash
cd idne
python3 -m venv env
source env/bin/activate
pip install --editable .
```

Go to `utils/config.py`, then insert your username and password
```python
username = "ababcba" # your codeforces username
password = "asdadas" # your password
```

Make sure to edit `template.cpp` as you wish
```
vim template.cpp
```


## Usage
----------



Example: Solving [Codeforces Round #259 (Div. 2)](http://codeforces.com/contest/454)

First, ensure that you have activated the virtualenv
Activate virtualenv
```
source env/bin/activate
```

Secondly, parse the problem

```
parse 454
```

And there will be a folder named 454-c++11, with a subfolder (e.g: A, B, C, D) inside. Assume you are solving problem A
```
cd 454-c++11/A
```

Use your favourite text editor and edit A.cpp. I use vim for this example
```
vim A.cpp
```

After confident with your solution, you can use ./test.sh to check if your solution passes the sample test
```
./test.sh
```

If it passes, you can submit with idne. The format is: idne [problem id] [filename]
```
idne 454A A.cpp
```

## Credits

- [Codeforces Parser](https://github.com/johnathan79717/codeforces-parser)
