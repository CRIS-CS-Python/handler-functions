# Handler Functions Excercise

This program accepts commands and values, calls *handler functions* and prints returned results.

## Usage

This program is used by providing a valid command and one or more arguments.

Run the command `py convert.py` with no arguments to see the usage syntax and valid commands:

```
convert.py <command> <value1> [value2 ... valueN]

Where commands are:
    c_to_f        Convert Celsius number to Fahrenheit
    f_to_c        Convert Fahrenheit number to Celsius
    USD_to_THB    Convert US Dollar (USD) amount to Thai Baht (THB)
    THB_to_USD    Convert Thai Baht (THB) amount to US Dollar (USD)
```

## Test Handler Function

You will need to implement the above commands and their corresponding handler functions. A handler function is a function that processes the arguments for a particular command and returns the results.

The `convert.py` file contains starter code for a command called `test` and a handler function named `test_func`. This is an example to help you get started, but this example code should be removed and replaced with the actual handler functions for the valid commands.

## Completed Program Usage and Output

### Celcius to Fahrenheit

```
$ py convert.py c_to_f 37.3
99.14
```

### Fahrenheit to Celcius

```
$ py convert.py f_to_c 104.9
40.5
```

### USD to THB

Use a conversion rate of 1 USD to THB of `33.948286`. Otherwise these values will be different.

```
$ py convert.py USD_to_THB 75
2546.12145
```

### THB to USD

```
$ py convert.py THB_to_USD 7945
234.03243392022793
```

### [Unit Tests](https://en.wikipedia.org/wiki/Unit_testing)

Unit Tests are used to test each function our Python code, or at least
the functions that are meant to be called by users of our `convert` module.

The Unit Tests are already created for you if you define your handler functions
as `c_to_f(cmd, args)`, `f_to_c(cmd, args)`, `usd_to_thb(cmd, args)`, and
`thb_to_usd(cmd, args)`. You can inspect `test_convert.py` to see how they work.

Here is how to *run the Unit Tests*, showing success:

```
py test_convert.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
