# UNIT TESTING ATTEMPT 1 (FAIL) : 

Report :

```bash
python .\unit_test.py -v
  test_12_format (__main__.TestClockInputs.test_12_format) ... FAIL
  test_24_format (__main__.TestClockInputs.test_24_format) ... FAIL
  test_minutes (__main__.TestClockInputs.test_minutes) ... FAIL
  test_seconds (__main__.TestClockInputs.test_seconds) ... FAIL

  ======================================================================
  FAIL: test_12_format (__main__.TestClockInputs.test_12_format)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 14, in test_12_format
      self.assertFalse(clock_testing(Clock(0,0,0,False,)))
      ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  AssertionError: True is not false

  ======================================================================
  FAIL: test_24_format (__main__.TestClockInputs.test_24_format)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 9, in test_24_format
      self.assertFalse(clock_testing(Clock(-1,0,0)))
      ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  AssertionError: True is not false

  ======================================================================
  FAIL: test_minutes (__main__.TestClockInputs.test_minutes)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 20, in test_minutes
      self.assertFalse(clock_testing(Clock(0,-10,0)))
      ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  AssertionError: True is not false

  ======================================================================
  FAIL: test_seconds (__main__.TestClockInputs.test_seconds)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 25, in test_seconds
      self.assertFalse(clock_testing(Clock(0,0,-15)))
      ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  AssertionError: True is not false

  ----------------------------------------------------------------------
  Ran 4 tests in 0.004s

  FAILED (failures=4)
```

This shows that i've forget to check for negative numbers in my checking functions, which is bad because a clock doesn't run with negative numbers.

# UNIT TESTING ATTEMPT 2 WITH FIXES

This time i've done negative number checking like this :
```python
if not 0 <= time.hours < 24:
    return False
```
If all the tests doesn't pass, then my syntax is wrong and i'll be safer in the next unit tests.

Report : 

```bash
    python .\unit_test.py -v
    test_12_format (__main__.TestClockInputs.test_12_format) ... FAIL
    test_24_format (__main__.TestClockInputs.test_24_format) ... FAIL
    test_minutes (__main__.TestClockInputs.test_minutes) ... ok
    test_seconds (__main__.TestClockInputs.test_seconds) ... FAIL

    ======================================================================
    FAIL: test_12_format (__main__.TestClockInputs.test_12_format)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 12, in test_12_format
        self.assertTrue(clock_testing(Clock(12,10,30,False)))
        ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: False is not true

    ======================================================================
    FAIL: test_24_format (__main__.TestClockInputs.test_24_format)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 8, in test_24_format
        self.assertFalse(clock_testing(Clock(55,0,0)))
        ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: True is not false

    ======================================================================
    FAIL: test_seconds (__main__.TestClockInputs.test_seconds)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 23, in test_seconds
        self.assertTrue(clock_testing(Clock(0,0,59)))
        ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: False is not true

    ----------------------------------------------------------------------
    Ran 4 tests in 0.003s

    FAILED (failures=3)
```

Yeah It doesn't look good. It means my syntax is wrong, i'll fix it for next attempt.

# UNIT TESTING ATTEMPT 3 WITH FIXES

Now, I take a more precautious approach by using or to check first if its below 0 or if its too much, like :
```python
  if 0 > time.hours or time.hours > 24:
      return False
```

I hope it'll work, if not then I either don't understand something about unit testing OR I've done something wrong and hasn't witnessed it still (which can be possible).

Report :

```bash
    python .\unit_test.py -v
    test_12_format (__main__.TestClockInputs.test_12_format) ... FAIL
    test_24_format (__main__.TestClockInputs.test_24_format) ... ok
    test_minutes (__main__.TestClockInputs.test_minutes) ... ok
    test_seconds (__main__.TestClockInputs.test_seconds) ... ok

    ======================================================================
    FAIL: test_12_format (__main__.TestClockInputs.test_12_format)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "C:\Users\belaz\Documents\development\software\PythClock\unit_test.py", line 14, in test_12_format
        self.assertFalse(clock_testing(Clock(0,0,0,False,)))
        ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError: True is not false

    ----------------------------------------------------------------------
    Ran 4 tests in 0.003s

    FAILED (failures=1)
```

Yeah now it's way better is it. There is still some failures which must be some inattention errors.

# UNIT TESTING ATTEMPT 4 WITH FIXES

After checking, I've missed the fact that there isn't 00h in 12h format.
In fact, it goes from 12 to 1 when getting to AM/PM, Where it goes from 23h59 to 00h00 in 24h format.
I've fixed that, now let's test it.

Report : 

```bash
    python .\unit_test.py -v
    test_12_format (__main__.TestClockInputs.test_12_format) ... ok
    test_24_format (__main__.TestClockInputs.test_24_format) ... ok
    test_minutes (__main__.TestClockInputs.test_minutes) ... ok
    test_seconds (__main__.TestClockInputs.test_seconds) ... ok

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
```

Now we're talking. The test are now all passed successfully, meaning my function clock_testing and so clock_validity do his job nicely.