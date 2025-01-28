'''
<Name>, <Grade> <Course>

This program contains conversion algorithms in functions.
Subcommands determine which convertion function is called.
'''

### Imports ###
import sys

### Global Variables ###
USAGE = '''\
convert.py <command> <value1> [value2 ... valueN]

Where commands are:
    c_to_f        Convert Celsius number to Fahrenheit
    f_to_c        Convert Fahrenheit number to Celsius 
    USD_to_THB    Convert US Dollar (USD) amount to Thai Baht (THB)
    THB_to_USD    Convert Thai Baht (THB) amount to US Dollar (USD)
'''

### Functions ###
def warn(*args, **kwargs):
    '''print a string to stderr'''
    print(*args, file=sys.stderr, **kwargs)

def die(*args, **kwargs):
    '''print a string to stderr and exit 1'''
    warn(*args, **kwargs)
    sys.exit(1)

def test_func(cmd, args):
    '''Function to help get started - TODO replace or delete this.'''
    return f"command: {cmd}" + "\n" + f"values: {args}"

### Main ###

# a "dunder main" conditional statement is used such that its block of code
# is not executed if this module is initialized as a module
if __name__ == '__main__':
    # sys.argv at a minimum should contain: ['convert.py', 'command', 'arg1']
    # but can contain 1 or more arguments
    # print error and exit if not correct arguments
    if len(sys.argv) < 3:
        die(USAGE)

    # string containing command
    cmd = sys.argv[1]
    # list of string values (arguments)
    args = sys.argv[2:]

    # START TODO - replace code from here to "END TODO"
    # check for valid commands:
    # * if invalid command: print error message and usage to stderr and exit with error code
    # * if valid command: call handler function,
    #                     passing in cmd and args,
    #                     store returned results value

    # this is an example
    # replace `test` command and `test_func` with valid commands and handler functions
    if cmd == 'test':
        res = test_func(cmd, args)
    else:
        warn(f"no such command: {cmd}\n")
        die(USAGE)
    # END TODO

    # print results
    print(res)