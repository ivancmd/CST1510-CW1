"""
RECORD CHECK  -  my version
===========================

Name  : Ivan Matara
Lane  : Cyber      (delete two)
Date  : 08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(value, limit=100):
    """Checks if the percentage is over the limit"""
    percent=((value/limit)*100)
    if percent>=limit:
        status=('OVER LIMIT')
        return(status)
    elif percent>=90:
        status=('WARNING')
        return(status)
    else:
        status=('OK')
        return(status)

def check(value, limit):
    """Returns the difference and percentage as 2 values"""
    difference=limit-value
    return(difference)
    percent=((value/limit)*100)
    return(percent)

def print_report(label, value, limit, difference, percent, status):
    """Outputs all of the values"""
    print(label)
    print(value)
    print(limit)
    print(difference)
    print(percent)
    print(status)


# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

label = input('Enter a Source IP: ')     # replace with an input() call
value = float(input('Enter a the number of failed logins: '))     # replace with an input() call, converted
limit = float(input('Enter the total number of attempts: '))     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference = limit-value   # replace with your code
percent = ((value/limit)*100)       # replace with your code
status = status_of(value, limit=100)          # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f'Failed Logins  :   {value:>10.2f}')
print(f'Total Attempts :   {limit:>10.2f}')
print(f'Difference     :   {difference:>10.2f}')
print(f'Percentage     :   {percent:>10.2f}%')
print(f'Status         :   {status:>10}')

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
# Test 1
#==================================
#  RECORD CHECK  -  10.0.0.5
#==================================
#Failed Logins  :        12.00
#Total Attempts :       400.00
#Difference     :       388.00
#Percentage     :         3.00%
#Status         :           OK
#==================================
#
# Test 2
#==================================
#  RECORD CHECK  -  10.23.54.67
#==================================
#Failed Logins  :        23.00
#Total Attempts :        54.00
#Difference     :        31.00
#Percentage     :        42.59%
#Status         :           OK
#==================================
#
# Test 3
#==================================
#  RECORD CHECK  -  4.32.4.67
#==================================
#Failed Logins  :       456.00
#Total Attempts :       457.00
#Difference     :         1.00
#Percentage     :        99.78%
#Status         :   OVER LIMIT
#==================================
#
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#ZeroDivisionError: division by zero
#
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
