# -*- coding: utf-8 -*-
"""
===============================================================================
             PYTHON EXCEPTION HANDLING
===============================================================================


WHAT THIS FILE TEACHES 
-------------------------------------------------------
 01. What is an exception? What happens without handling?
 02. Understanding error messages and tracebacks
 03. try and except: correct syntax and execution flow
 04. ValueError and ZeroDivisionError with user input
 05. Multiple except blocks and common built-in exceptions
 06. Handling two or more error types in one except block
 07. Why bare except is dangerous
 08. Capturing exceptions using 'as e'
 09. Printing exception message and exception class name
 10. else: executes only when try succeeds
 11. finally: cleanup even when an exception happens
 12. raise: create an exception deliberately
 13. Exception propagation and re-raising using 'raise'
 14. Your own custom exception class
 15. Best practices for reliable programs

PRACTICAL EXTENSIONS
-----------------------------------------------------
 16. File operations and automatic resource cleanup
 17. Logging exceptions without exposing internal details
 18. SQLite database exception handling
 19. JSON/REST API input errors and FastAPI patterns
 20. Source-code analysis example relevant to code-checking projects
 21. Important subtleties: exception hierarchy, scope, finally + return
 22. Common developer mistakes and their corrected versions
 23. Interview questions, answers, and coding practice

HOW TO USE
----------
1. Read the triple-quoted notes BEFORE each program.
2. Predict the output of each function.
3. Run this entire file: python Python_Exception_Handling_Complete_Notes.py
4. To practice one example, call that demo function at the bottom.
5. Modify values: try 'abc', 0, missing dictionary keys, wrong indices, etc.
6. For programs that need manual input, read the OPTIONAL INTERACTIVE examples.
7. All demos run using Python's STANDARD LIBRARY; no pip installation needed.

IMPORTANT
---------
Exception handling is NOT a way to ignore bugs. It is a way to respond to
expected failures safely, preserve important resources, and give useful errors.

===============================================================================
"""

from __future__ import annotations

import ast
import json
import logging
import sqlite3
import tempfile
from pathlib import Path


def section(number: str, title: str) -> None:
    """Only prints attractive headings when example programs are run."""
    print("\n" + "=" * 76)
    print(f"SECTION {number}: {title}")
    print("=" * 76)


# ============================================================================
# 01. WHAT IS AN EXCEPTION? WHY HANDLE IT?
# ============================================================================
"""
DEFINITION (interview answer)
-----------------------------
An exception is an event/error raised during program execution that interrupts
the normal flow of statements. If it is not handled, Python typically stops
executing the current program and prints a traceback.

Simple example:
    Your code expects a number, but the user types 'hello'.
    int('hello') cannot convert that text -> ValueError is raised.

REAL-LIFE ANALOGY
-----------------
You are withdrawing cash from an ATM.
- Normal path: sufficient balance -> money is dispensed.
- Unexpected situation: requested amount exceeds balance.
- Handling: show 'Insufficient balance' instead of breaking the application.

WHY IT MATTERS
--------------
- Prevent one recoverable problem from unexpectedly ending a user workflow.
- Show useful and friendly error messages.
- Avoid partial operations and clean up files / database connections.
- Record useful diagnostics for developers.

IMPORTANT CORRECTION
--------------------
Not every error crashes an entire server. An unhandled exception stops the
current call/task; frameworks often catch it and return an HTTP 500 response.
Handling also does NOT mean the failed line magically starts working again.
Execution normally moves to the matching except block, then continues AFTER
the whole try/except statement.

ERROR vs EXCEPTION
------------------
'SyntaxError' can prevent a file from being parsed at all; a try block inside
that same invalid file cannot fix it. Many runtime problems, including
ValueError, TypeError and ZeroDivisionError, can be caught with try/except.
"""


def demo_01_why_exceptions_matter() -> None:
    # Without try/except, the next statement would not execute in this call.
    # We catch it so the study file can keep running.
    try:
        age = int("hello")
        print(age)             # Skipped due to ValueError
    except ValueError:
        print("Invalid age. Please type digits such as 18 or 25.")
    print("The application can continue with other work.")


# ============================================================================
# 02. HOW TO READ A TRACEBACK
# ============================================================================
"""
A traceback often looks like this:

    Traceback (most recent call last):
      File "example.py", line 3, in <module>
        age = int("abc")
    ValueError: invalid literal for int() with base 10: 'abc'

READ FROM THE BOTTOM FIRST:
1. ValueError -> exception class / name.
2. invalid literal ... -> explanation/message.
3. File + line number -> where the failure occurred.
4. The lines above it -> which functions were called to reach the error.

WHAT DOES 'base 10' MEAN?
-------------------------
It means decimal numbers (0-9). The word 'abc' is not a valid decimal integer.

HOW PYTHON KNOWS WHICH EXCEPTION OCCURRED
-----------------------------------------
Exceptions are objects of exception classes. Example:
    e              -> exception object
    str(e)         -> readable message
    type(e)        -> class object, e.g. <class 'ValueError'>
    type(e).__name__ -> class name, e.g. ValueError

You can inspect a caught error without allowing it to crash this lesson.
"""


def demo_02_traceback_details() -> None:
    try:
        number = int("abc")
        print(number)
    except ValueError as error:
        print("Exception name:", type(error).__name__)
        print("Exception message:", str(error))


# ============================================================================
# 03. try / except: BASIC SYNTAX AND EXECUTION FLOW
# ============================================================================
"""
BASIC SYNTAX:

    try:
        risky_statement()
    except ValueError:
        print("Please enter a valid number")

WHAT HAPPENS?
-------------
CASE A - NO EXCEPTION:
    try runs completely -> except is skipped -> next statement executes.

CASE B - A MATCHING EXCEPTION:
    try begins -> an exception happens -> remaining statements in try are
    SKIPPED -> matching except runs -> statement AFTER the structure runs.

CASE C - A DIFFERENT, UNHANDLED EXCEPTION:
    Exception keeps propagating to the caller. If nobody catches it, a
    traceback appears; code after that point may not execute.

ONE IMPORTANT DETAIL
--------------------
    try:
        print("A")
        int("wrong")
        print("B")        # This is SKIPPED
    except ValueError:
        print("C")
    print("D")

Output:
    A
    C
    D

Indentation (usually 4 spaces) decides which statements belong to each block.
"""


def demo_03_execution_flow() -> None:
    for raw in ("21", "abc"):
        print(f"\nInput: {raw!r}")
        try:
            print("1. Started conversion")
            age = int(raw)
            print("2. Converted age:", age)
        except ValueError:
            print("3. Invalid age: please enter a whole number.")
        print("4. This runs after try/except.")


# ============================================================================
# 04. HANDLING USER INPUT: ValueError
# ============================================================================
"""
VIDEO EXAMPLE: ADULT OR NOT ADULT
---------------------------------
    age = int(input("Enter age: "))
    if age >= 18:
        print("Adult")
    else:
        print("Not adult")

Problem: typing 'abc' raises ValueError. Put input conversion inside try.

PROPER PRACTICE
---------------
- Validate whether text can be converted into a number.
- Also validate business rules: age cannot be negative, for example.
- For demos below, we pass a string to a function, so you can run without
  typing into the terminal every time.
"""


def age_status(raw_age: str) -> str:
    """Return a friendly result for a user's age input."""
    try:
        age = int(raw_age)
    except ValueError:
        return "Please enter age as a whole number (e.g. 20)."

    if age < 0:
        return "Age cannot be negative."
    if age >= 18:
        return "Adult"
    return "Not adult"


def demo_04_age_input() -> None:
    for text in ("19", "17", "abc", "-10", "20.5"):
        print(f"Input {text!r} -> {age_status(text)}")


# ============================================================================
# 05. ZeroDivisionError AND MULTIPLE except BLOCKS
# ============================================================================
"""
ZERO DIVISION ERROR
-------------------
    10 / 2  -> 5.0
    10 / 0  -> ZeroDivisionError: division by zero

Another problem: int('abc') -> ValueError.

Instead of telling a user 'Some error occurred' for every problem,
catch different errors individually:

    try:
        num1 = int(input("First: "))
        num2 = int(input("Second: "))
        answer = num1 / num2
    except ValueError:
        print("Enter integer numbers only")
    except ZeroDivisionError:
        print("Second number cannot be zero")
    else:
        print(answer)

WHY SPECIFIC except BLOCKS?
---------------------------
- Different causes need different fixes and messages.
- Hidden bugs are less likely to be swallowed.
- More helpful for troubleshooting and interviews.

The FIRST matching except block handles the exception. Others are skipped.
Put more specific exception classes before broader ones such as Exception.
"""


def divide_user_numbers(first: str, second: str) -> str:
    try:
        num1 = int(first)
        num2 = int(second)
        result = num1 / num2
    except ValueError:
        return "Please enter valid integer numbers."
    except ZeroDivisionError:
        return "Cannot divide by zero. Use a nonzero second number."
    else:
        return f"Answer = {result}"


def demo_05_multiple_handlers() -> None:
    for first, second in (("10", "2"), ("10", "0"), ("abc", "2")):
        print(f"{first!r} / {second!r} -> {divide_user_numbers(first, second)}")


# ============================================================================
# 06. COMMON BUILT-IN EXCEPTION TYPES (FROM YOUR VIDEO)
# ============================================================================
"""
EXCEPTION           WHEN DOES IT HAPPEN?                  EXAMPLE
---------           --------------------                  -------
ValueError          Valid type, invalid value             int('hello')
ZeroDivisionError   Divide by zero                        10 / 0
TypeError           Operation incompatible with type     '5' + 2
IndexError          List index does not exist             [4, 8][9]
KeyError            Dictionary key does not exist        {'name':'A'}['age']
AttributeError      Object lacks attribute/method        'hello'.append('!')
NameError           Variable/function is undefined       print(unknown_var)
FileNotFoundError   File path cannot be found             open('missing.txt')
KeyboardInterrupt   User interrupts (often Ctrl+C)       Ctrl+C in terminal

ADDITIONAL USEFUL TYPES:
ImportError         Import cannot be completed            wrong import
ModuleNotFoundError A requested module is not found      import nonexistent
PermissionError     Operation is blocked by permissions   open protected file
OSError             Operating-system-related issue       some disk/I/O failures
TimeoutError        A timed operation failed             some network/file ops
json.JSONDecodeError Invalid JSON text                    json.loads('{')
sqlite3.IntegrityError Violated database constraint       duplicate UNIQUE key

REMEMBER:
- Indexes in [5, 7, 1] are 0, 1, and 2; index 9 does not exist.
- A dictionary missing key raises KeyError; dict.get() can be a better choice
  if a missing key is NORMAL and expected.
- A string has no .append() method; lists do.
- KeyboardInterrupt inherits BaseException, NOT Exception, so
  except Exception generally does not catch a normal Ctrl+C interruption.
- Never intentionally send Ctrl+C during these runnable demonstrations.
"""


def demo_06_common_exceptions() -> None:
    """Safely demonstrate common runtime errors without stopping execution."""
    examples = [
        ("ValueError", lambda: int("hello")),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("TypeError", lambda: "5" + 2),  # type: ignore[operator]
        ("IndexError", lambda: [5, 7, 1][9]),
        ("KeyError", lambda: {"name": "Asha"}["age"]),
        ("AttributeError", lambda: "hello".append("!")),  # type: ignore[attr-defined]
        ("NameError", lambda: eval("undefined_variable")),
    ]
    for title, action in examples:
        try:
            action()
        except (ValueError, ZeroDivisionError, TypeError, IndexError,
                KeyError, AttributeError, NameError) as error:
            print(f"{title:18} -> {type(error).__name__}: {error}")

    # Separate file example with a path that definitely does not exist.
    with tempfile.TemporaryDirectory() as temp_dir:
        missing_path = Path(temp_dir) / "never_created.txt"
        try:
            missing_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            print("FileNotFoundError  -> The requested file was not found.")


# ============================================================================
# 07. COMBINE MULTIPLE EXCEPTION TYPES IN ONE BLOCK
# ============================================================================
"""
If two different exception types need the SAME response:

    except (ValueError, ZeroDivisionError):
        print("Invalid input. Please try again.")

It is a TUPLE of exception classes.
A tuple is useful only if the same recovery action fits each case.
If the user needs different instructions, use separate except blocks instead.
"""


def demo_07_grouped_handlers() -> None:
    for value in ("abc", "0", "5"):
        try:
            result = 100 / int(value)
        except (ValueError, ZeroDivisionError):
            print(f"Input {value!r}: Invalid number for this calculation.")
        else:
            print(f"Input {value!r}: Result = {result}")


# ============================================================================
# 08. BARE except VS except Exception
# ============================================================================
"""
AVOID:
    try:
        important_work()
    except:
        pass

Problems:
- 'except:' catches even KeyboardInterrupt and SystemExit.
- 'pass' hides an important failure; now nobody knows what went wrong.
- A bug may appear as a successful operation when it is not.

ALSO AVOID as a default pattern:
    except Exception:
        print("Something went wrong")

It can be useful at a real application boundary (request handler, job worker),
but log the failure and return an appropriate error, or re-raise when needed.

PREFERRED:
    except ValueError as error:
        print("Invalid input:", error)

WHAT DOES Exception MEAN?
-------------------------
Most ordinary runtime exception classes inherit from built-in Exception.
Catching Exception is broader than catching ValueError alone, but narrower
than bare except (which also catches BaseException subclasses like Ctrl+C).

When handling a custom class inheriting from Exception, it works too.
"""


def demo_08_specific_vs_generic() -> None:
    try:
        int("not-a-number")
    except ValueError:
        print("Good: handled the exact input conversion failure.")


# ============================================================================
# 09. 'as e': CAPTURE THE EXCEPTION OBJECT
# ============================================================================
"""
SYNTAX:
    except ValueError as e:
        print(e)

'e' is just a variable name for the exception OBJECT. You may name it
'error', 'exc' or something else. A real exception object contains details.

WHAT CAN WE PRINT?
------------------
    print(e)                  -> error message
    print(str(e))             -> error message as string
    print(type(e))            -> class, e.g. <class 'ValueError'>
    print(type(e).__name__)   -> just ValueError

Important: type(e).__name__ uses DOUBLE underscores before and after 'name'.

WHEN USE THIS?
--------------
- Debugging failures.
- Structured logging.
- Tests checking the error category.
- Creating safe customer messages (but don't reveal internal/private details).
"""


def demo_09_exception_object() -> None:
    for value in ("abc", "0"):
        try:
            result = 20 / int(value)
            print("Result:", result)
        except (ValueError, ZeroDivisionError) as error:
            print("Error message:", error)
            print("Error name   :", type(error).__name__)
            print("Error class  :", type(error))


# ============================================================================
# 10. else: RUN ONLY IF try FINISHES WITHOUT AN EXCEPTION
# ============================================================================
"""
SYNTAX:
    try:
        number = int('25')
    except ValueError:
        print('Invalid number')
    else:
        print('Conversion succeeded')

Remember:
- else runs ONLY if the try block completed normally.
- It does not run if except handled an exception.
- Use else for the success-only part, not for risky conversion itself.
- Errors raised INSIDE else are not caught by the except clauses that
  belong to the same try statement; use another try if needed.

PROGRAM FLOW:
    success -> try -> else -> (finally if present) -> next statement
    error   -> try -> except -> (finally if present) -> next statement
"""


def demo_10_else() -> None:
    for raw in ("4", "abc"):
        try:
            number = int(raw)
        except ValueError:
            print(f"{raw!r}: conversion failed; else did NOT run.")
        else:
            print(f"{raw!r}: conversion succeeded; number squared = {number ** 2}.")


# ============================================================================
# 11. finally: CLEANUP CODE
# ============================================================================
"""
SYNTAX:
    try:
        risky_work()
    except ValueError:
        handle_error()
    else:
        handle_success()
    finally:
        clean_up()

WHY finally?
-------------
The finally block runs when control leaves the try statement, whether the
try block succeeds or fails, and even if a return is used.

Typical tasks:
- Close a file or resource.
- Release a lock.
- Disconnect from a database.
- Record final status.

IMPORTANT DETAIL:
finally executes even when an exception is going to propagate, but it cannot
be guaranteed after process termination, machine failure, os._exit(), etc.
An exception INSIDE finally can replace the original exception.

DO NOT RETURN FROM finally:
A return in finally can hide errors or override earlier return values.

BETTER MODERN PRACTICE:
Use 'with open(...) as file:' to close a file automatically. This is often
cleaner than manually calling file.close() inside finally.
"""


def demo_11_else_and_finally() -> None:
    for raw in ("10", "0", "wrong"):
        print(f"\nTrying input: {raw!r}")
        try:
            number = int(raw)
            answer = 100 / number
        except ValueError:
            print("except: Enter a valid integer.")
        except ZeroDivisionError:
            print("except: Cannot divide 100 by zero.")
        else:
            print("else: Result =", answer)
        finally:
            print("finally: Calculation attempt finished.")


# ============================================================================
# 12. raise: CREATE AN EXCEPTION YOURSELF
# ============================================================================
"""
WHY raise?
----------
Sometimes Python considers a value valid, but YOUR application does not.
For example: int('-5') works, but an age of -5 is not valid.

SYNTAX:
    raise ValueError('Age cannot be negative')

Difference:
    print('Invalid age') -> displays text, but callers may think success.
    raise ValueError(...) -> stops normal execution and signals failure.

WHEN TO RAISE?
--------------
- Validation: quantity must be positive.
- Business logic: requested amount exceeds account balance.
- Precondition: required config/API key is missing.
- Data integrity: input does not satisfy system rules.

A function that raises may be caught by its CALLER. This separation lets
low-level code report a problem while higher-level code decides how to show it.
"""


def validate_age(age: int) -> str:
    """Validate age with clear error messages rather than print-and-continue."""
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >= 150:
        raise ValueError("Age is outside the supported range")
    return f"Age {age} is valid."


def demo_12_raise() -> None:
    for age in (20, -5, 1000):
        try:
            print(validate_age(age))
        except ValueError as error:
            print(f"Validation failed for {age}: {error}")


# ============================================================================
# 13. ERROR PROPAGATION AND RE-RAISING USING 'raise'
# ============================================================================
"""
VERY IMPORTANT FROM THE VIDEO
-----------------------------
Imagine two functions:
    main() -> check_age() -> int('abc') raises ValueError.

If check_age() catches it and DOES NOT re-raise, main() sees a normal return.
The outer try's else may even display 'Success!' although the operation
actually failed.

A BARE 'raise' INSIDE an except block re-raises the CURRENT exception.
That same failure then reaches the caller and can be caught there.

SYNTAX:
    def inner():
        try:
            ...
        except ValueError:
            print('Inner: logging problem')
            raise           # Send the SAME exception to the caller.

    try:
        inner()
    except ValueError:
        print('Outer: now I know it failed')

KEY DIFFERENCE:
    raise ValueError('new')  -> create a new ValueError.
    raise                    -> re-raise the active exception in except.
    raise error              -> raises that object but may change traceback.

BEST PRACTICE: Prefer bare 'raise' when re-raising the current exception.

REAL EXAMPLE:
- Repository layer catches database error and logs context.
- It re-raises so service/API layer knows the operation failed.
"""


def inner_that_swallows_error() -> None:
    try:
        int("abc")
    except ValueError:
        print("Inside: problem was handled but not passed outside.")


def inner_that_reraises_error() -> None:
    try:
        int("abc")
    except ValueError as error:
        print("Inside: detected an error:", error)
        raise


def demo_13_reraise() -> None:
    print("\nA) WITHOUT re-raise:")
    try:
        inner_that_swallows_error()
    except ValueError:
        print("Outside: FAILED")
    else:
        print("Outside: thinks SUCCESS happened (misleading)!")

    print("\nB) WITH bare raise:")
    try:
        inner_that_reraises_error()
    except ValueError as error:
        print("Outside: correctly received error:", error)
    else:
        print("Outside: success")


# ============================================================================
# 14. CUSTOM EXCEPTIONS - YOUR OWN ERROR TYPE
# ============================================================================
"""
VIDEO'S BANKING EXAMPLE
-----------------------
Account balance = Rs. 1000
Withdraw request = Rs. 5000

Instead of generic ValueError, create a meaningful business exception:

    class InsufficientFundsError(Exception):
        pass

Why '(Exception)'?
------------------
This is INHERITANCE. It makes InsufficientFundsError a normal exception class
that Python can raise/catch with try/except.

Why 'pass'?
-----------
The new class does not need extra methods yet; it inherits useful behavior
from the Exception superclass.

Custom exceptions help:
- Describe domain-specific problems clearly.
- Let the caller catch one specific business case.
- Avoid writing confusing special cases around generic error strings.

Real applications may use more detailed subclasses, e.g.
    class AttendanceAlreadyMarkedError(Exception): pass
    class InvalidSourceCodeError(Exception): pass
"""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""


class InvalidWithdrawalError(Exception):
    """Raised when the withdrawal amount is zero or negative."""


def withdraw_money(balance: float, amount: float) -> float:
    if amount <= 0:
        raise InvalidWithdrawalError("Withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientFundsError("Not enough balance")
    return balance - amount


def demo_14_custom_exceptions() -> None:
    for amount in (500, 5000, -20):
        try:
            remaining = withdraw_money(1000, amount)
        except InsufficientFundsError as error:
            print(f"Withdraw {amount}: {type(error).__name__}: {error}")
        except InvalidWithdrawalError as error:
            print(f"Withdraw {amount}: {type(error).__name__}: {error}")
        else:
            print(f"Withdraw {amount}: remaining balance = Rs. {remaining}")


# ============================================================================
# 15. PRACTICAL FILE HANDLING (ADDITIONAL PROJECT KNOWLEDGE)
# ============================================================================
"""
FILES CAN FAIL IN MANY WAYS:
- FileNotFoundError -> specified file doesn't exist.
- PermissionError -> user/process may not have permission.
- OSError -> general filesystem/I/O problem.
- UnicodeDecodeError -> bytes aren't valid in requested encoding.

COMMON WRONG IDEA:
    file = open('myfile.txt')
    data = file.read()
    file.close()

If file.read() fails, close() might never execute.

PREFERRED:
    with open('myfile.txt', encoding='utf-8') as file:
        data = file.read()

'with' automatically closes the file when the block ends, even after a
read error. Catch exceptions around the with block when recovery is needed.

IN WEB DEVELOPMENT:
- Read server configuration or a user's uploaded text.
- Show a safe error if the expected file does not exist.
- Never expose internal folder structure to the end user.
"""


def read_report_file(path: Path) -> str:
    try:
        with path.open("r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as error:
        raise ValueError("Requested report was not found") from error
    except PermissionError as error:
        raise ValueError("Requested report cannot be opened") from error


def demo_15_file_handling() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        location = Path(temp_dir) / "report.txt"
        location.write_text("Code quality report: 0 critical issues", encoding="utf-8")
        print("Existing file:", read_report_file(location))
        try:
            read_report_file(Path(temp_dir) / "missing.txt")
        except ValueError as error:
            print("Friendly file error:", error)


# ============================================================================
# 16. logging: RECORD EXCEPTIONS FOR DEVELOPERS (ADDITIONAL)
# ============================================================================
"""
WHY LOG INSTEAD OF ONLY print()?
--------------------------------
print() is fine while learning; real apps often use logging for severity,
context, timestamps, and central log collection.

    import logging
    logger = logging.getLogger(__name__)

    try:
        something_risky()
    except SomeExpectedError:
        logger.exception('Operation failed')
        raise

logger.exception() automatically includes exception traceback when called
INSIDE an exception handler. It is useful for investigating failures.

SECURITY:
- Logs may contain sensitive information. Do not log passwords, tokens,
  uploaded secrets, raw biometric data, or other private user content.
- Show users generic safe messages; keep technical details in restricted logs.
- Avoid duplicate logs for one failure across many application layers.

NOTE: Our simple demo uses no actual log calls to avoid noisy console output.
"""


def parse_positive_integer(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as error:
        raise ValueError("A whole number is required") from error
    if value <= 0:
        raise ValueError("Number must be greater than zero")
    return value


def demo_16_error_context() -> None:
    for value in ("8", "abc", "-2"):
        try:
            print("Parsed:", parse_positive_integer(value))
        except ValueError as error:
            print("Safe message:", error)
            if error.__cause__ is not None:
                print("Original cause type:", type(error.__cause__).__name__)


# ============================================================================
# 17. EXCEPTION CHAINING: raise ... from error (ADDITIONAL)
# ============================================================================
"""
Sometimes a low-level error should be converted into a clearer application
error, while preserving the original cause for diagnostics.

    try:
        int('abc')
    except ValueError as error:
        raise RuntimeError('Could not process age field') from error

Why this is useful:
- Original exception: ValueError converting text.
- New exception: a more meaningful high-level failure.
- __cause__ points to the original exception.

'raise NewError(...) from None' suppresses cause display in the traceback.
Use it intentionally; do not conceal useful diagnostics by accident.

COMPARE:
- 'raise'                  re-raise SAME active exception.
- 'raise NewError()'        create new exception, possibly implicit context.
- 'raise NewError() from e' create new exception WITH explicit cause.
"""


# ============================================================================
# 18. SQLite DATABASE ERRORS (ADDITIONAL - BACKEND PROJECTS)
# ============================================================================
"""
WHY THIS MATTERS:
In FastAPI/Flask projects, the API often reads/writes a database.
Examples of DB failures:
- Duplicate value in a UNIQUE column -> sqlite3.IntegrityError.
- Invalid SQL statement -> sqlite3.OperationalError.
- Other DB-specific issues -> sqlite3.DatabaseError subclasses.

PRODUCTION RULES:
- Do not claim that a database write succeeded when it failed.
- Use transactions so multi-step writes are committed together or rolled back.
- Return a meaningful response, often HTTP 409 for a genuine conflict.
- Close database connections using proper resource management.

Below is a standalone demo using an in-memory database. It creates no
permanent data on your computer.
"""


def demo_18_sqlite_errors() -> None:
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute(
            "CREATE TABLE students (id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL)"
        )
        with connection:  # Commit on success; roll back the transaction on error.
            connection.execute(
                "INSERT INTO students (id, email) VALUES (?, ?)",
                (1, "student@example.com"),
            )

        try:
            with connection:
                # Triggers a UNIQUE constraint failure.
                connection.execute(
                    "INSERT INTO students (id, email) VALUES (?, ?)",
                    (2, "student@example.com"),
                )
        except sqlite3.IntegrityError:
            print("Database conflict: this email is already registered.")

        count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print("Rows after attempted duplicate insert:", count)
    finally:
        connection.close()  # 'with connection:' alone does NOT close connection.


# ============================================================================
# 19. JSON / REST API INPUT: SAFE ERROR HANDLING (ADDITIONAL)
# ============================================================================
"""
REAL WEB-API SITUATION:
A frontend sends a JSON body to a Python backend.
Example valid text:
    {"student_id": 45, "attendance": true}

Possible problems:
1. Text is not valid JSON -> json.JSONDecodeError.
2. JSON isn't an object -> wrong type -> ValueError (our validation).
3. Required field missing -> KeyError (or explicitly validate key).
4. A field has the wrong data type -> TypeError / custom validation error.

In FastAPI with Pydantic request models, much of request validation is already
handled for you, typically returning HTTP 422 for invalid input.
You should STILL handle domain-specific errors and database errors.

FRAMEWORK SKETCH (REFERENCE ONLY; FastAPI isn't required to run these notes):

    from fastapi import FastAPI, HTTPException
    app = FastAPI()

    @app.get('/withdraw')
    def withdraw(balance: float, amount: float):
        try:
            new_balance = withdraw_money(balance, amount)
        except InsufficientFundsError:
            raise HTTPException(status_code=400, detail='Insufficient balance')
        except InvalidWithdrawalError:
            raise HTTPException(status_code=422, detail='Amount must be positive')
        return {'remaining_balance': new_balance}

Security: real financial operations must NOT trust a balance sent from the
client. They must use an authenticated account, validated permissions, an
atomic database transaction, and server-side balance checks. The above is
only an exception-handling illustration, NOT an actual banking API.
"""


def read_attendance_payload(raw_json: str) -> str:
    """Validate a simple JSON object, with safe messages for client code."""
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError as error:
        raise ValueError("The request body is not valid JSON") from error

    if not isinstance(payload, dict):
        raise ValueError("JSON body must be an object")
    if "student_id" not in payload:
        raise ValueError("student_id is required")
    if not isinstance(payload["student_id"], int) or isinstance(payload["student_id"], bool):
        raise ValueError("student_id must be an integer")
    return f"Attendance request accepted for student {payload['student_id']}"


def demo_19_json_api() -> None:
    examples = (
        '{"student_id": 45, "attendance": true}',
        '{"student_id": "wrong"}',
        '{"attendance": true}',
        '{broken json}',
        '[1, 2, 3]',
    )
    for raw in examples:
        try:
            print(read_attendance_payload(raw))
        except ValueError as error:
            print("HTTP-style validation error:", error)


# ============================================================================
# 20. CODE ANALYSIS / SECURITY CHECKER USE CASE (ADDITIONAL)
# ============================================================================
"""
A Python code-analysis platform may parse user-provided Python text with AST.

If the user uploads invalid Python syntax:
    ast.parse('def broken(:')

Python raises SyntaxError. Here it happens while PARSING A STRING during
program execution, so a surrounding try/except SyntaxError CAN catch it.
This differs from a syntax error in the application's own .py source code,
which could prevent the application module from loading at all.

PROJECT-SAFE PATTERN:
- Catch SyntaxError from source parsing.
- Return a clear validation failure to the user.
- Do not run untrusted user-submitted code with exec/eval.
- AST parsing alone does NOT guarantee code safety or security.
"""


class InvalidSourceCodeError(Exception):
    """Raised when supplied source text cannot be parsed as Python."""


def count_python_functions(source_code: str) -> int:
    try:
        tree = ast.parse(source_code)
    except SyntaxError as error:
        line = error.lineno if error.lineno is not None else "unknown"
        raise InvalidSourceCodeError(f"Invalid Python syntax near line {line}") from error
    return sum(isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
               for node in ast.walk(tree))


def demo_20_code_analysis() -> None:
    for code in ("def hello():\n    return 42\n", "def broken(:\n    pass\n"):
        try:
            print("Number of functions:", count_python_functions(code))
        except InvalidSourceCodeError as error:
            print("Code analysis could not begin:", error)


# ============================================================================
# 21. COMMON MISTAKES AND PRODUCTION BEST PRACTICES
# ============================================================================
"""
MISTAKE 1: Catch everything, then ignore the problem
    try: save_to_db()
    except: pass
FIX: Catch a specific exception and take useful action. Re-raise if needed.

MISTAKE 2: Enclose too much code in one try
    try: read_input(); update_db(); send_email(); generate_report()
    except Exception: print('Failed')
FIX: Separate operations; catch failures where you can handle them.

MISTAKE 3: Show raw exception messages to public users
    except Exception as e: return {'error': str(e)}
FIX: Log safely on server; give user a suitable generic response.

MISTAKE 4: Assume code continues at the failed line
    try:
        value = int('abc')
        print('never executed')
    except ValueError:
        print('handled')
FIX: The failed try path is abandoned; use retry logic if appropriate.

MISTAKE 5: Use exception handling instead of simple checks when checks fit
    try: user['middle_name']
    except KeyError: middle_name = None
ALTERNATIVE: user.get('middle_name') if missing is a normal case.

MISTAKE 6: Catch the wrong class
    except ZeroDivisionError: ...   # cannot catch int('abc') ValueError
FIX: Identify realistic failure types; add relevant except blocks.

MISTAKE 7: Wrong order
    except Exception: ...
    except ValueError: ...         # Unreachable for ValueError
FIX: Put ValueError first and the broader Exception later.

MISTAKE 8: Return a value from finally
FIX: Keep finally for cleanup, NOT for return. A finally return can replace
     a value or hide a raised exception.

MISTAKE 9: Assume 'with sqlite3.connect(...)' closes DB connection
FIX: sqlite3 connection context manager manages a transaction; explicit
     connection.close() or another closing strategy is still required.

MISTAKE 10: Assume exception handling makes unreliable code correct
FIX: Improve validation, tests, idempotency, database transactions,
     observability, and recovery behavior too.

10 RULES TO REMEMBER:
1. Catch the smallest set of errors you can realistically handle.
2. Prefer specific error types over broad catch-all handlers.
3. Put the risky operation inside try.
4. Put success-only code in else when it improves clarity.
5. Put cleanup in finally (or prefer 'with' for supported resources).
6. Raise exceptions when a function cannot fulfill its contract.
7. Re-raise if the caller still needs to know an operation failed.
8. Use custom exceptions for important domain errors.
9. Log enough context for debugging, but protect sensitive data.
10. Test both success cases and failure cases.
"""


# ============================================================================
# 22. SUBTLE BUT COMMON INTERVIEW QUESTIONS
# ============================================================================
"""
Q: Does finally run if there is a return inside try?
A: Yes, normally finally executes before the function returns. But it is not
   guaranteed after immediate process termination or certain fatal failures.

Q: Does a catch for Exception catch KeyboardInterrupt?
A: Generally no. KeyboardInterrupt inherits directly from BaseException.

Q: What happens if there is an error inside finally?
A: It may replace an exception that was already being propagated.

Q: Does try need an except?
A: Not always. A try statement must have at least an except or a finally.
   Example: try: do_work() finally: cleanup()

Q: Does else run if except catches a problem?
A: No. else runs only when the try block exits normally.

Q: Can an except block catch an exception raised in its OWN else block?
A: No, not by the same try statement's except handlers.

Q: Is ValueError always a user-input error?
A: No. Any code can raise it for a value that is inappropriate.

Q: Can we use multiple exception classes in the same handler?
A: Yes: except (ValueError, TypeError) as e:

Q: What happens when no exception occurs?
A: All statements in try run, except is skipped, else runs if present, and
   finally runs if present.

Q: Why not use exceptions for every 'if' decision?
A: Exceptions indicate operations that cannot proceed normally. Routine
   control flow often reads better with regular if statements.
"""


def demo_22_finally_and_return() -> None:
    def example() -> str:
        try:
            return "Returned from try"
        finally:
            print("finally runs before the return is completed")

    print(example())


# ============================================================================
# 23. INTERVIEW QUESTIONS + SHORT, SIMPLE ANSWERS
# ============================================================================
"""
01. What is exception handling in Python?
    It is a way to respond to runtime failures using try/except and optionally
    else/finally, instead of letting every failure remain unhandled.

02. Why do we need exception handling?
    For safe recovery, useful error messages, cleanup, and reliable software.

03. Explain try and except.
    try holds code that may fail; except handles matching exceptions.

04. What is an exception?
    An object signaling an abnormal condition during execution.

05. What is the difference between SyntaxError and ValueError?
    SyntaxError concerns invalid Python syntax. ValueError means a value is
    unsuitable for an operation, such as int('abc').

06. How do you handle multiple exceptions?
    Write several except blocks or use a tuple of exception types.

07. What is the difference between except ValueError and except Exception?
    ValueError handles just that category (and subclasses); Exception handles
    most usual runtime exceptions and their subclasses.

08. Why avoid bare except?
    It catches too much, including Ctrl+C and process-exit exceptions.

09. What does 'except ValueError as e' mean?
    Catch a ValueError and give its exception object the variable name e.

10. How can you print the error message?
    str(e) or print(e).

11. How can you print the error name?
    type(e).__name__.

12. What is ZeroDivisionError?
    It is raised when an invalid division by zero is attempted.

13. What is TypeError?
    An operation or function received an inappropriate type, e.g. '3' + 2.

14. What is IndexError?
    You tried to access a sequence index that does not exist.

15. What is KeyError?
    You requested a missing dictionary key with dictionary[key].

16. What is AttributeError?
    An object does not have the requested attribute/method.

17. What is FileNotFoundError?
    A requested file/directory path cannot be found for an operation.

18. What is the purpose of else in try/except?
    It runs only after a successful try block.

19. What is the purpose of finally?
    To run cleanup even when an exception occurs or a return is made.

20. Does finally always run?
    Under normal Python control flow, yes; not after forced process termination.

21. What does raise do?
    It deliberately raises an exception object or class.

22. Why raise ValueError('Age cannot be negative')?
    Because the age violates a business rule, even though -5 is an integer.

23. What is re-raising an exception?
    Raising the currently handled exception again so callers can handle it.

24. How do you re-raise the same error?
    Use bare raise inside an except block.

25. Why might a caller need a re-raised exception?
    The caller must know a lower-level operation failed so it can abort or
    select an appropriate response.

26. What is a custom exception?
    A user-defined class derived from Exception for a specific application error.

27. Why inherit custom errors from Exception?
    To make them compatible with the normal Python exception machinery.

28. What does 'pass' mean inside a custom exception class?
    It leaves the class body empty; inherited behavior is still available.

29. How can exception handling help in backend web development?
    It converts input, database, file and business failures into appropriate
    API responses while allowing server-side logging and cleanup.

30. How should errors be returned from an API?
    Use the correct HTTP status and a safe message; do not expose stack traces.

31. What is exception chaining?
    Raising a new error 'from' an original one to preserve cause information.

32. What is the difference between exception and return?
    return provides the normal result. raise signals that normal work failed.

33. Can Python have try with only finally and no except?
    Yes, a try/finally is valid.

34. Can a generic except hide a bug?
    Yes; catching and ignoring an unexpected failure conceals the actual issue.

35. How would you handle duplicate attendance records?
    Add a database uniqueness rule, catch the resulting integrity exception,
    and respond with a meaningful conflict instead of inserting a duplicate.
"""


# ============================================================================
# 24. PRACTICE PROBLEMS WITH SMALL WORKING SOLUTIONS
# ============================================================================
"""
TRY EACH WITHOUT LOOKING AT THE SOLUTION:

TASK 1: Convert a text input to int; on failure, return None.
TASK 2: Safely access a list item; return 'Invalid index' if missing.
TASK 3: Safely look up a required dictionary key; return a helpful message.
TASK 4: Raise a custom exception if an order quantity is not positive.
TASK 5: Make a retry loop accepting 'abc' and '0' as bad inputs for 100 / n.

Your task after running this file:
- Change the example values.
- Write the functions again in a blank file without copying.
- Describe what exception each line could raise.
- Explain why each handler is appropriate in a mock interview.
"""


def practice_1_safe_int(text: str) -> int | None:
    try:
        return int(text)
    except ValueError:
        return None


def practice_2_safe_list_access(items: list[int], index: int) -> int | str:
    try:
        return items[index]
    except IndexError:
        return "Invalid index"


def practice_3_required_key(data: dict[str, str], key: str) -> str:
    try:
        return data[key]
    except KeyError:
        return f"Required key {key!r} is missing"


class InvalidOrderQuantityError(Exception):
    """Raised when an order contains a nonpositive quantity."""


def practice_4_order_total(price: float, quantity: int) -> float:
    if quantity <= 0:
        raise InvalidOrderQuantityError("Quantity must be at least one")
    return price * quantity


def practice_5_first_valid_division(inputs: list[str]) -> float | None:
    """Simulates retrying bad terminal inputs; returns first valid result."""
    for raw in inputs:
        try:
            return 100 / int(raw)
        except ValueError:
            print(f"Retry: {raw!r} is not an integer")
        except ZeroDivisionError:
            print("Retry: denominator cannot be zero")
    return None


def demo_24_practice_solutions() -> None:
    print("Task 1:", practice_1_safe_int("abc"), practice_1_safe_int("42"))
    print("Task 2:", practice_2_safe_list_access([10, 20], 5))
    print("Task 3:", practice_3_required_key({"name": "Riya"}, "age"))
    try:
        practice_4_order_total(100, 0)
    except InvalidOrderQuantityError as error:
        print("Task 4:", error)
    print("Task 5:", practice_5_first_valid_division(["abc", "0", "4"]))


# ============================================================================
# 25. OPTIONAL INTERACTIVE PROGRAMS (RUN MANUALLY IF YOU WANT TO TYPE INPUT)
# ============================================================================
"""
These programs are NOT called automatically. When you want user input,
uncomment the correct line in main() below and run the file.

PROGRAM A: Ask age until the user enters a valid whole number:

    while True:
        try:
            age = int(input('Enter your age: '))
            if age < 0:
                raise ValueError('Age cannot be negative')
        except ValueError as e:
            print('Try again:', e)
        else:
            print('Age accepted:', age)
            break

PROGRAM B: Calculator using try / except / else / finally:

    try:
        numerator = float(input('Numerator: '))
        denominator = float(input('Denominator: '))
        result = numerator / denominator
    except ValueError:
        print('Enter numbers only')
    except ZeroDivisionError:
        print('Cannot divide by zero')
    else:
        print('Answer:', result)
    finally:
        print('Calculation attempt complete')

PROGRAM C: Raise custom bank exception:

    try:
        remaining = withdraw_money(1000, 5000)
    except InsufficientFundsError as e:
        print('Withdrawal declined:', e)
    else:
        print('Remaining amount:', remaining)

Tip: Don't put input() at the top level if the file is meant to be reused
in imports or automated tests. Use functions and the __main__ guard.
"""


# ============================================================================
# 26. QUICK REVISION: INTERVIEW CHEAT SHEET
# ============================================================================
"""
+----------------------+-----------------------------------------------+
| KEYWORD              | SIMPLE MEANING                                |
+----------------------+-----------------------------------------------+
| try                  | Run code that may fail.                       |
| except ValueError    | Handle a particular failure.                  |
| except (A, B)        | Handle either A or B in one block.            |
| except Exception     | Catch most regular exceptions (broad).        |
| as error             | Save exception object to a variable.          |
| else                 | Run only if try succeeded.                    |
| finally              | Run cleanup on leaving the try statement.     |
| raise ValueError(..) | Deliberately create an exception.             |
| raise                | Re-raise currently handled exception.         |
| class X(Exception)   | Define a custom exception type.               |
+----------------------+-----------------------------------------------+

MOST IMPORTANT INTERVIEW CODE:

    try:
        n = int('abc')
        answer = 100 / n
    except ValueError as e:
        print('Invalid input:', e)
    except ZeroDivisionError:
        print('Cannot divide by zero')
    else:
        print(answer)
    finally:
        print('Done')

MOST IMPORTANT REAL-WORLD RULE:
Don't just catch an error: decide whether to RETRY, RECOVER, RESPOND,
ROLL BACK, or RE-RAISE it.

YOUR MINI REVISION ROUTINE (20 MINUTES)
--------------------------------------
5 min  -> Explain try, except, else, finally in your own words.
5 min  -> Write a calculator that handles bad input and division by zero.
5 min  -> Write validate_age() using raise; catch error from caller.
5 min  -> Define InsufficientFundsError and explain 'raise' vs 're-raise'.

SOURCE-BASED COVERAGE NOTE
--------------------------
Sections 01-14 follow the subject order and examples in the supplied video
(age validation, division, multiple handlers, exception objects, else/finally,
raise/re-raise, custom insufficient-funds exception). Sections 15-26 are
extra clarifications, working project examples, and interview practice.

YOU ARE READY TO MOVE ON WHEN YOU CAN:
[ ] Predict which parts of try/except/else/finally execute.
[ ] Catch ValueError and ZeroDivisionError individually.
[ ] Explain IndexError, KeyError, TypeError, AttributeError and NameError.
[ ] Explain the difference between a general and a specific catch.
[ ] Print an error's message and type name.
[ ] Raise an error in one function and catch it in its caller.
[ ] Re-raise an error when higher-level code must know it failed.
[ ] Create and use one custom exception.
[ ] Handle malformed JSON and database conflicts in small examples.
[ ] Explain how to avoid revealing traceback/secrets to API clients.

===============================================================================
                              END OF NOTES
===============================================================================
"""


def main() -> None:
    """Runs all SAFE, non-interactive examples from this study file."""
    demos = [
        ("01", "Why exceptions matter", demo_01_why_exceptions_matter),
        ("02", "Traceback and error details", demo_02_traceback_details),
        ("03", "try/except flow", demo_03_execution_flow),
        ("04", "ValueError in age input", demo_04_age_input),
        ("05", "Separate exception handlers", demo_05_multiple_handlers),
        ("06", "Common built-in exception types", demo_06_common_exceptions),
        ("07", "Grouped exception handlers", demo_07_grouped_handlers),
        ("08", "Why specific catches are better", demo_08_specific_vs_generic),
        ("09", "The exception object: as e", demo_09_exception_object),
        ("10", "else", demo_10_else),
        ("11", "finally", demo_11_else_and_finally),
        ("12", "raise", demo_12_raise),
        ("13", "re-raise", demo_13_reraise),
        ("14", "Custom exception", demo_14_custom_exceptions),
        ("15", "File handling", demo_15_file_handling),
        ("16", "Error context and chaining", demo_16_error_context),
        ("18", "SQLite database conflict", demo_18_sqlite_errors),
        ("19", "JSON / API validation", demo_19_json_api),
        ("20", "AST code analyzer", demo_20_code_analysis),
        ("22", "finally and return", demo_22_finally_and_return),
        ("24", "Practice solutions", demo_24_practice_solutions),
    ]
    print("PYTHON EXCEPTION HANDLING | COMPLETE RUNNABLE EXAMPLES")
    for number, title, func in demos:
        section(number, title)
        func()
    print("\nFinished: All safe examples ran successfully!")


if __name__ == "__main__":
    main()
