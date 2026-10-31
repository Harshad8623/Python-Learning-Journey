# ============================================================
#        PYTHON INTRODUCTION, HISTORY & INTERVIEW QUESTIONS
# ============================================================



# ============================================================
# 1. WHAT IS PYTHON?
# ============================================================

"""
Python is a high-level, general-purpose, dynamically typed,
interpreted programming language.


1. What is High-level programming language
Meaning: A high-level programming language is a language that is easy for humans to read, write 
and understand because its syntax is closer to human language than machine language.

2. Why is Python called a high-level language?
"Python is called a high-level language because its syntax is simple and readable. 
We don't need to manage low-level details like memory allocation manually in normal Python programming. 
It allows developers to focus more on solving problems rather than hardware-level operations."

3. What is General-purpose programming language
Meaning: A general-purpose programming language is a language that can be used to develop different 
types of applications rather than being limited to one specific task.
Example:

We can use Python for:
Web development Example: Django, Flask, FastAPI.
AI and Machine Learning Example: TensorFlow, PyTorch.
Data Science Example: NumPy, Pandas.
Automation Example: Automating repetitive tasks using Python scripts.

4. What is Dynamically typed programming language
Meaning: In a dynamically typed language, we don't need to explicitly declare the data type of a variable. 
Python determines the type of the object at runtime.

a = 10
print(type(a))
a = "Harshad"
print(type(a))

Initially, a refers to an integer object (10).
Later, a refers to a string object ("Harshad").
Python determines the type at runtime.
We don't need to write int a = 10 or string a = "Harshad".

5. What is dynamic typing?
"Dynamic typing means we don't need to explicitly declare the data type of a variable. 
Python determines the type at runtime, and the same variable name can refer to objects of different 
data types during program execution."

x = 100
x = 10.5
x = "Python"
x = True


6. Interpreted programming language
Meaning: An interpreted language uses a runtime system to execute the program rather than requiring 
the programmer to manually compile the source code into a standalone machine-code executable beforehand.

Example:
Suppose you create a Python file: main.py
a = 10
b = 20

print(a + b)

python main.py
Python handles the execution process.

How Python executes code internally:
Python Source Code

main.py

Python Compiler

Compiles source code into bytecode

Python Bytecode

Intermediate instructions

Python Virtual Machine (PVM)

Executes bytecode

Program Output

7. What is Programming language
Meaning: A programming language is a language that allows developers to give instructions to a computer 
to perform specific tasks.

Python was designed with a strong focus on:

    - Readability
    - Simplicity
    - Developer productivity
    - Code maintainability

Python is widely used in:

    - Web Development
    - Data Science
    - Artificial Intelligence
    - Machine Learning
    - Automation
    - Scripting
    - Software Development
    - Data Analysis
    - Cybersecurity
    - Testing
    - Scientific Computing
    - DevOps
"""


# ============================================================
# 2. WHO CREATED PYTHON?
# ============================================================

"""
Python was created by:

        Guido van Rossum

He is a Dutch programmer.

A Dutch programmer is simply a computer programmer (software developer) from the Netherlands. 
The adjective "Dutch" refers to someone or something from the Netherlands.

Python was created as a successor to the ABC programming language.

Guido van Rossum started working on Python in the late
1980s and released the first public version in 1991.
"""

# ============================================================
# 2.1. WHAT IS DUTCH PROGRAMMER ?
# ============================================================
"""
The "Dutch programmer" you are seeing mentioned is Guido van Rossum, 
the famous computer scientist from the Netherlands who created the Python programming language in 1989.
If you recently typed import this into a Python terminal, 
you probably saw a famous list of design rules called the Zen of Python. 
One of the lines in that famous poem says: "There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch.
"Who is the Dutch Programmer? Name: Guido van Rossum 
What he did : Invented Python as a fun holiday project in December 1989.
His Role : He led Python's development for decades as the "Benevolent Dictator for Life" (BDFL) before stepping back. 
He has worked for major tech giants like Google, Dropbox, and Microsoft.
Why does the code mention "unless you're Dutch"? Inside Joke: The line in the Zen of Python is a playful joke by the author of the poem (Tim Peters) honoring Guido's Dutch heritage.
The Meaning : It pokes fun at the idea that Python's "one obvious way" to do things might sometimes only make sense in the clever mind of its creator from the Netherlands.
"""
# ============================================================
# 3. WHY WAS PYTHON CREATED?
# ============================================================

"""
Guido van Rossum wanted to create a programming language
that was:

    - Easy to read
    - Easy to write
    - Simple to learn
    - Powerful
    - Suitable for scripting
    - Better suited for rapid development

Python was designed to emphasize code readability and
developer productivity.
"""


# ============================================================
# 4. WHERE DID THE NAME "PYTHON" COME FROM?
# ============================================================

"""
The name "Python" did NOT come from the snake.

Guido van Rossum named the language after the British
comedy group:

        Monty Python

He was a fan of the comedy show:

        "Monty Python's Flying Circus"

Therefore, the name Python is related to Monty Python,
not originally to the snake.
"""


# ============================================================
# 5. PYTHON HISTORY TIMELINE
# ============================================================

"""
IMPORTANT PYTHON HISTORY:

1989
    Guido van Rossum started working on Python.

1991
    Python's first public release.

1994
    Python 1.0 was released.

2000
    Python 2.0 was released.

2008
    Python 3.0 was released.

2020
    Python 2 officially reached End of Life.

Today
    Python 3 is the standard and actively maintained
    major version family.


IMPORTANT:

Python 2 and Python 3 are significantly different.

Modern Python development uses Python 3.
"""


# ============================================================
# 6. PYTHON 1.0
# ============================================================

"""
Python 1.0 was released in 1994.

It established many of the core ideas that made Python
popular:

    - Simple syntax
    - Readability
    - Modular programming
    - High-level programming
"""


# ============================================================
# 7. PYTHON 2.0
# ============================================================

"""
Python 2.0 was released in 2000.

It introduced important improvements such as:

    - List comprehensions
    - Garbage collection improvements
    - Unicode support improvements

Python 2 became very popular.

However, Python 2 eventually reached its official
End of Life on:

        January 1, 2020

New projects should use Python 3.
"""


# ============================================================
# 8. PYTHON 3.0
# ============================================================

"""
Python 3.0 was released in 2008.

Python 3 was designed to improve the language and fix
some historical design limitations.

Python 3 was NOT completely backward compatible with
Python 2.

Modern Python programming uses Python 3.
"""


# ============================================================
# 9. PYTHON 2 VS PYTHON 3
# ============================================================

"""
Python 2:

    - Legacy
    - Officially discontinued
    - End of Life : January 1, 2020

Python 3:

    - Modern Python
    - Actively developed
    - Recommended for new projects


INTERVIEW ANSWER:

"Python 2 is a legacy version that reached end of life
in 2020, while Python 3 is the modern and actively
maintained version used for current development."
"""

"""
Legacy version means an old version of software that is no longer actively supported or recommended for new projects.

In your example:

Python 2 → Legacy version
Python 3 → Current/modern version
Simple example 🧠

Imagine a college uses an old computer system from 2015. It may still work, but:

It doesn't receive new updates.
Security problems may not be fixed.
New software may not support it.
Developers generally don't build new projects for it.

That system is called legacy.

For Python

Python 2 officially reached End of Life (EOL) on January 1, 2020.

This means Python 2:

❌ No new features
❌ No official bug fixes
❌ No security updates
❌ Not recommended for new projects

Python 3 is the version you should learn and use today.

In one line:

Legacy = an old technology that may still exist/work, but is no longer actively supported and is generally replaced by a newer version.
"""


# ============================================================
# 10. CURRENT PYTHON
# ============================================================

"""
For interviews, remember:

    Python 3 is the modern Python version family.

Python continues to receive:

    - New features
    - Performance improvements
    - Security updates
    - Standard library improvements
"""


# ============================================================
# 11. WHY IS PYTHON POPULAR?
# ============================================================

"""
Python became popular because it provides:

    1. Simple and readable syntax
    2. Large standard library
    3. Huge third-party ecosystem
    4. Cross-platform support
    5. Large developer community
    6. Rapid development
    7. Strong support for automation
    8. Strong AI/ML ecosystem
    9. Strong data science ecosystem
    10. Extensive frameworks and libraries
"""


# ============================================================
# 12. MAIN FEATURES OF PYTHON
# ============================================================

"""
Important Python features:

    - High-level
    - General-purpose
    - Interpreted
    - Dynamically typed
    - Object-oriented
    - Supports multiple programming paradigms
    - Open source
    - Cross-platform
    - Extensive standard library
    - Large third-party ecosystem
    - Readable syntax
    - Automatic memory management
"""

"""
What is a programming paradigm?
A programming paradigm is basically a particular approach to structuring and solving problems using code.

For example, Python supports several paradigms:

Paradigm	                      Main idea	                             Python example
Procedural	            Step-by-step instructions	                     if, for, functions
Object-Oriented (OOP)	Organize code using classes/objects	             class Student:
Functional	            Treat functions as first-class objects	         map(), filter(), lambda
Imperative	            Tell the computer exactly how to do something	 Loops, assignments
Declarative	            Describe what you want	                         List comprehensions, SQL-like approaches

"""


# ============================================================
# 13. PYTHON IS HIGH-LEVEL
# ============================================================

"""
Python is a high-level programming language.

This means Python provides abstractions that make it easier
for programmers to write software without dealing directly
with low-level hardware details.

Example:

Python code is generally much easier to read than
machine-level instructions.
"""

"""
What is High Level language?
A high-level programming language is a programming language designed to be easy for humans to understand and use, 
while hiding the low-level hardware details of the computer.


what is Low level language?
A low-level language is a programming language that is closely related to the hardware and provides 
direct control over computer resources such as CPU and memory.
"""

# ============================================================
# 14. PYTHON IS GENERAL-PURPOSE
# ============================================================

"""
Python is general-purpose because it can be used for many
different types of applications.

Examples:
    Web Development
    AI
    Machine Learning
    Data Science
    Automation
    Desktop Applications
    Testing
    Scientific Computing
    DevOps
    Scripting
"""


# ============================================================
# 15. PYTHON IS INTERPRETED - INTERVIEW EXPLANATION
# ============================================================

"""
Python is commonly described as an interpreted language.

However, an interview-quality answer should be more precise:

Python source code is generally compiled to an intermediate
bytecode representation, which is then executed by the
Python interpreter/virtual machine.

For standard CPython:

    Python source code
            ↓
       Bytecode
            ↓
       Python VM
            ↓
        Execution


IMPORTANT:

Do NOT simply say:

"Python is only interpreted and not compiled."

That is an oversimplification.

CPython does perform a compilation step to bytecode.
"""

"""
If an interviewer asks “Is Python interpreted or compiled?”, the best answer is:

“Python is generally considered an interpreted language, but technically Python code is first compiled into bytecode, 
and that bytecode is then executed by the Python interpreter.”

If they ask you to explain further

You can say:

Python code → Bytecode → Python Virtual Machine (PVM) → Execution

For example:
print("Hello")
When you run it:

Python source code (.py) is processed.
It is compiled into bytecode (.pyc conceptually).
The Python interpreter/PVM executes that bytecode.
You see the output.
So is Python both?

Technically: yes, it has both compilation and interpretation steps.

But in interviews, avoid simply saying:

❌ “Python is both compiled and interpreted.”

A better, more precise answer is:

✅ “Python is commonly called an interpreted language. 
Internally, CPython compiles the source code into bytecode, 
which is then executed by the Python Virtual Machine.”
"""

# ============================================================
# 16. WHAT IS CPYTHON?
# ============================================================

"""
CPython is the reference implementation of Python and
the implementation most commonly used.

It is written primarily in C.

When people install Python from python.org, they generally
use CPython.

CPython:

    Python source
        ↓
    Bytecode
        ↓
    Python Virtual Machine
        ↓
    Execution
"""


# ============================================================
# 17. PYTHON IS DYNAMICALLY TYPED
# ============================================================

"""
Python is dynamically typed.

The type is associated with the object at runtime, and
a variable name can refer to objects of different types
during execution.

Interview example:

    x = 10

    x = "Python"

The same variable name can refer to different types
of objects at different times.
"""

"""
    x = 10

    x = "Python"

So where does 10 go?
If nothing else is referring to the object 10, Python's memory-management system can eventually remove/reclaim that object.
This is called garbage collection / reference-count-based memory management in CPython.
"""

# ============================================================
# 18. PYTHON IS CASE-SENSITIVE
# ============================================================

"""
Python is case-sensitive.

For example:

    name

and

    Name

are different identifiers.

Similarly:

    print

and

    Print

are different names.
"""


# ============================================================
# 19. PYTHON IS OPEN SOURCE
# ============================================================

"""
Python is open-source software.

Its source code is publicly available, and Python is
developed through a community-driven process.

Python is managed by the Python Software Foundation
(PSF), a non-profit organization that supports the
Python community.

Q. What is Open Source?
Open-source software is software whose source code is publicly available, 
so people can inspect it, use it, modify it, 
and often distribute modified versions, depending on its license.
"""


# ============================================================
# 20. PYTHON IS CROSS-PLATFORM
# ============================================================

"""
Python programs can run on many operating systems,
including:

    - Windows
    - Linux
    - macOS

Python therefore supports cross-platform development,
although platform-specific dependencies can still exist.
"""


# ============================================================
# 21. PYTHON PROGRAMMING PARADIGMS
# ============================================================

"""
Python supports multiple programming paradigms.

Examples include:

    - Procedural programming
    - Object-oriented programming
    - Functional programming

Therefore Python is often described as a
multi-paradigm programming language.
"""

"""
🎯 Interview answer

If an interviewer asks:

"What do you mean by Python supports multiple programming paradigms?"

Say:

"It means Python allows programmers to use different programming approaches, 
such as procedural, object-oriented, and functional programming, 
depending on the problem and requirement."
"""

# ============================================================
# 22. PYTHON APPLICATIONS
# ============================================================

"""
Python is used in many fields.

1. WEB DEVELOPMENT

Popular frameworks:

    Django
    Flask
    FastAPI


2. DATA SCIENCE

Libraries:

    NumPy
    Pandas
    Matplotlib


3. MACHINE LEARNING

Libraries:

    Scikit-learn
    PyTorch
    TensorFlow


4. ARTIFICIAL INTELLIGENCE

Python is heavily used for:

    - Machine Learning
    - Deep Learning
    - Generative AI
    - NLP
    - Computer Vision


5. AUTOMATION

Python can automate:

    - Repetitive tasks
    - File operations
    - Data processing
    - Testing
    - Web tasks


6. DEVOPS

Python can be used for:

    - Automation
    - Infrastructure scripting
    - Monitoring
    - Tooling


7. SCIENTIFIC COMPUTING

Python is widely used in scientific and engineering
applications.
"""


# ============================================================
# 23. ADVANTAGES OF PYTHON
# ============================================================

"""
Major advantages:

1. Easy to learn
2. Readable syntax
3. Large ecosystem
4. Huge community
5. Cross-platform
6. Rapid development
7. Large standard library
8. Excellent AI/ML ecosystem
9. Good for automation
10. Supports multiple programming paradigms
"""


# ============================================================
# 24. DISADVANTAGES OF PYTHON
# ============================================================

"""
Major disadvantages:

1. Generally slower than compiled languages such as C/C++
   for CPU-intensive workloads.

2. Higher memory usage in many workloads.

3. Dynamic typing can allow some type-related problems
   to appear at runtime.

4. Not always the best choice for:
       - Low-level systems programming
       - Extremely performance-sensitive applications
       - Some mobile application development scenarios

5. Python's Global Interpreter Lock (GIL) in traditional
   CPython implementations has historically limited
   execution of Python bytecode across multiple threads
   for CPU-bound workloads.

IMPORTANT:

Modern Python versions have also introduced free-threaded
builds as an optional direction, so avoid saying:

"Python can NEVER run Python code in parallel."

That statement is too absolute.
"""


# ============================================================
# 25. PYTHON STANDARD LIBRARY
# ============================================================

"""
Python comes with a large standard library.

This means many useful capabilities are available without
installing third-party packages.

Examples include modules for:

    - Mathematics
    - Dates and time
    - File handling
    - Operating system interaction
    - Networking
    - JSON
    - Regular expressions
    - Testing
"""


# ============================================================
# 26. PYPI
# ============================================================

"""
PyPI stands for:

    Python Package Index

PyPI is a large repository of Python packages.

Developers can install many third-party packages from
PyPI using package management tools such as pip.
"""


# ============================================================
# 27. PIP 
# ============================================================

"""
pip does not officially stand for a specific phrase (No full form).
The Python Packaging User Guide describes pip simply as the package installer for Python. 
The name is commonly explained historically as a recursive acronym:

“pip installs packages”
pip is the standard package installer commonly used
with Python.

It is used to install and manage Python packages.

Example:

    pip install requests

This installs the requests package.
"""


# ============================================================
# 28. PYTHON SOFTWARE FOUNDATION
# ============================================================

"""
PSF stands for:

    Python Software Foundation

The PSF is a non-profit organization that supports:

    - Python development
    - Python community
    - Python conferences
    - Python education
    - Python ecosystem
"""


# ============================================================
# 29. PEP
# ============================================================

"""
PEP stands for:

    Python Enhancement Proposal

PEPs are documents that propose changes, improvements,
standards, or processes related to Python.

Important examples:

    PEP 8
        Python style guide.

    PEP 20
        The Zen of Python.

    PEP 484
        Type hints.

    PEP 572
        Assignment expressions.
"""


# ============================================================
# 30. PEP 8
# ============================================================

"""
PEP 8 is the main style guide for Python code.

It provides recommendations for:

    - Naming
    - Indentation
    - Whitespace
    - Code layout
    - Imports
    - Readability

Interview answer:

"PEP 8 is the official Python style guide that provides
conventions for writing readable and consistent Python code."
"""


# ============================================================
# 31. ZEN OF PYTHON
# ============================================================

"""
PEP 20 contains the Zen of Python.

PEP 20 is the Zen of Python. It contains 19 principles that describe the philosophy of Python programming, 
emphasizing simplicity, readability, clarity, and practicality.

You can display it in Python using:

    import this

It contains guiding principles emphasizing:

    - Readability
    - Simplicity
    - Explicitness
    - Clarity

PEP 8 = How to write Python code
PEP 20 = How to think about writing Python code

PEP 8 vs PEP 20
	                PEP 8	                                PEP 20
Full name	        Style Guide for Python Code	            The Zen of Python
Main purpose	    Coding style and formatting	            Python's philosophy/principles
Focus	            How code should look	                How code should be designed/thought about
Contains	        Rules/recommendations	                19 principles
Example	            Naming, indentation, spaces	            Simplicity, readability, clarity
Used for	        Writing consistent, readable code	    Guiding programming decisions

🎯 Interview answer

If asked "What is the difference between PEP 8 and PEP 20?", say:

"PEP 8 is Python's style guide that provides recommendations for writing clean and consistent code, 
such as indentation, naming conventions, and formatting. PEP 20, known as the Zen of Python, 
describes the philosophy and principles behind Python, emphasizing simplicity, readability, and clarity."
"""


# ============================================================
# 32. PYTHON LOGO
# ============================================================

"""
Python's logo uses two intertwined snakes.

The name Python itself, however, was inspired by
Monty Python's comedy show, not by the snake.
"""


# ============================================================
# 33. WHY PYTHON IS IMPORTANT FOR AI/ML
# ============================================================

"""
Python became extremely important in AI and ML because
of its ecosystem.

Popular tools include:

    NumPy
    Pandas
    Matplotlib
    Scikit-learn
    TensorFlow
    PyTorch

It is also widely used for:

    - Generative AI
    - LLM applications
    - NLP
    - Computer Vision
    - Data analysis
    - AI automation
"""


# ============================================================
# 34. WHY PYTHON IS IMPORTANT FOR DSA
# ============================================================

"""
Python is popular for DSA practice because:

    - Syntax is concise
    - Built-in data structures are powerful
    - Many operations are easy to express
    - Coding solutions can be written quickly

This allows you to focus more on:

    Algorithm
    Logic
    Time Complexity
    Space Complexity
"""


# ============================================================
# 35. PYTHON FOR INTERVIEWS
# ============================================================

"""
Python interviews commonly start with questions such as:

    - What is Python?
    - Who created Python?
    - Why was Python created?
    - Why is it called Python?
    - What are Python's features?
    - Is Python interpreted or compiled?
    - What is CPython?
    - What is dynamic typing?
    - What is PEP 8?
    - What is PEP?
    - What is PyPI?
    - What is pip?
    - What is the Python Software Foundation?
    - Python 2 vs Python 3?
    - Advantages of Python?
    - Disadvantages of Python?
    - Where is Python used?
"""


# ============================================================
#          INTERVIEW QUESTIONS AND ANSWERS
# ============================================================


# ============================================================
# Q1. What is Python?
# ============================================================

"""
ANSWER:

Python is a high-level, general-purpose programming
language known for its readable syntax and developer
productivity.

It supports multiple programming paradigms and is widely
used in web development, automation, data science,
AI/ML, and software development.
"""


# ============================================================
# Q2. Who created Python?
# ============================================================

"""
ANSWER:

Python was created by Guido van Rossum.
"""


# ============================================================
# Q3. When was Python first released?
# ============================================================

"""
ANSWER:

Python's first public release was in 1991.
"""


# ============================================================
# Q4. When was Python 1.0 released?
# ============================================================

"""
ANSWER:

Python 1.0 was released in 1994.
"""


# ============================================================
# Q5. When was Python 2.0 released?
# ============================================================

"""
ANSWER:

Python 2.0 was released in 2000.
"""


# ============================================================
# Q6. When was Python 3.0 released?
# ============================================================

"""
ANSWER:

Python 3.0 was released in 2008.
"""


# ============================================================
# Q7. Why is Python called Python?
# ============================================================

"""
ANSWER:

Guido van Rossum named the language after the British
comedy group Monty Python and its show
"Monty Python's Flying Circus."
"""


# ============================================================
# Q8. Is Python open source?
# ============================================================

"""
ANSWER:

Yes.

Python is open-source software and is developed with
community participation.
"""


# ============================================================
# Q9. Is Python case-sensitive?
# ============================================================

"""
ANSWER:

Yes.

Python is case-sensitive.
"""


# ============================================================
# Q10. Is Python cross-platform?
# ============================================================

"""
ANSWER:

Yes.

Python is available on major operating systems such as
Windows, Linux, and macOS.
"""


# ============================================================
# Q11. Is Python compiled or interpreted?
# ============================================================

"""
INTERVIEW-QUALITY ANSWER:

Python is commonly described as interpreted, but the
implementation matters.

In CPython, Python source code is compiled into bytecode,
which is then executed by the Python virtual machine.

Therefore, saying Python is "only interpreted" is an
oversimplification.
"""


# ============================================================
# Q12. What is CPython?
# ============================================================

"""
ANSWER:

CPython is the reference implementation of Python and
is primarily written in C.

It compiles Python source code into bytecode and executes
that bytecode using its runtime.
"""


# ============================================================
# Q13. What is Python 2?
# ============================================================

"""
ANSWER:

Python 2 is an older major version of Python.

It reached official End of Life on January 1, 2020.

Modern projects should use Python 3.
"""


# ============================================================
# Q14. What is Python 3?
# ============================================================

"""
ANSWER:

Python 3 is the modern Python version family and is the
standard choice for current Python development.
"""


# ============================================================
# Q15. What is PEP?
# ============================================================

"""
ANSWER:

PEP stands for Python Enhancement Proposal.

PEPs are documents used to propose and document
improvements, standards, and processes related to Python.
"""


# ============================================================
# Q16. What is PEP 8?
# ============================================================

"""
ANSWER:

PEP 8 is Python's primary style guide.

It provides recommendations for writing readable,
consistent, and maintainable Python code.
"""


# ============================================================
# Q17. What is PyPI?
# ============================================================

"""
ANSWER:

PyPI stands for Python Package Index.

It is a repository containing a large collection of
Python packages.
"""


# ============================================================
# Q18. What is pip?
# ============================================================

"""
ANSWER:

pip is a package installer commonly used to install
and manage Python packages.
"""


# ============================================================
# Q19. What is the Python Software Foundation?
# ============================================================

"""
ANSWER:

The Python Software Foundation (PSF) is a non-profit
organization that supports Python and its community.
"""


# ============================================================
# Q20. Why is Python so popular?
# ============================================================

"""
ANSWER:

Python is popular because of:

    - Readable syntax
    - Ease of development
    - Large ecosystem
    - Huge community
    - Cross-platform support
    - Extensive libraries
    - Strong AI/ML ecosystem
    - Strong automation capabilities
    - Rapid development
"""


# ============================================================
# Q21. What are the major uses of Python?
# ============================================================

"""
ANSWER:

Python is widely used for:

    - Web development
    - AI
    - Machine learning
    - Data science
    - Data analysis
    - Automation
    - Testing
    - DevOps
    - Scientific computing
    - Scripting
"""


# ============================================================
# Q22. What are the advantages of Python?
# ============================================================

"""
ANSWER:

Major advantages include:

    - Easy to learn
    - Readable
    - Large ecosystem
    - Cross-platform
    - Rapid development
    - Large community
    - Excellent AI/ML support
"""


# ============================================================
# Q23. What are the disadvantages of Python?
# ============================================================

"""
ANSWER:

Some disadvantages include:

    - Can be slower than compiled languages for some
      CPU-intensive workloads.
    - Can use more memory for some workloads.
    - Dynamic typing can move some errors to runtime.
    - Not always ideal for low-level programming.
"""


# ============================================================
# Q24. What type of programming language is Python?
# ============================================================

"""
ANSWER:

Python is:

    - High-level
    - General-purpose
    - Dynamically typed
    - Multi-paradigm
    - Commonly described as interpreted
    - Object-oriented capable
    - Open source
"""


# ============================================================
# Q25. Why is Python called a high-level language?
# ============================================================

"""
ANSWER:

Because Python provides a high level of abstraction from
the underlying hardware and machine-level operations,
making programs easier for humans to write and understand.
"""


# ============================================================
# Q26. Why is Python called dynamically typed?
# ============================================================

"""
ANSWER:

Because type information is associated with objects at
runtime, and a variable name can refer to objects of
different types during program execution.
"""


# ============================================================
# Q27. Is Python object-oriented?
# ============================================================

"""
ANSWER:

Yes.

Python supports object-oriented programming, but it is
not limited to OOP.

It also supports procedural and functional programming
styles.
"""


# ============================================================
# Q28. Is Python suitable for large projects?
# ============================================================

"""
ANSWER:

Yes.

Python is used in large-scale software systems and
organizations.

However, good architecture, testing, documentation,
performance optimization, and maintainability are still
important regardless of the language.
"""


# ============================================================
# Q29. Why is Python used in AI and Machine Learning?
# ============================================================

"""
ANSWER:

Python has a very strong AI/ML ecosystem and provides
libraries and frameworks such as:

    NumPy
    Pandas
    Scikit-learn
    PyTorch
    TensorFlow

It also has readable syntax and supports rapid
experimentation and development.
"""


# ============================================================
# Q30. Why should we learn Python for DSA?
# ============================================================

"""
ANSWER:

Python allows algorithms to be implemented with relatively
little code.

Its built-in data structures and concise syntax allow
developers to focus on algorithmic logic rather than
language syntax.

It is widely used for coding interviews and competitive
programming.
"""


# ============================================================
#        RAPID-FIRE INTERVIEW REVISION
# ============================================================

"""
Q: Creator?
A: Guido van Rossum

Q: First public release?
A: 1991

Q: Python 1.0?
A: 1994

Q: Python 2.0?
A: 2000

Q: Python 3.0?
A: 2008

Q: Python 2 EOL?
A: January 1, 2020

Q: Name inspired by?
A: Monty Python

Q: Modern Python?
A: Python 3

Q: Reference implementation?
A: CPython

Q: Package repository?
A: PyPI

Q: Package installer?
A: pip

Q: Style guide?
A: PEP 8

Q: Python proposal document?
A: PEP

Q: Python organization?
A: Python Software Foundation (PSF)

Q: Is Python case-sensitive?
A: Yes

Q: Is Python open source?
A: Yes

Q: Is Python cross-platform?
A: Yes

Q: Is Python dynamically typed?
A: Yes

Q: Is Python high-level?
A: Yes

Q: Is Python general-purpose?
A: Yes

Q: Is Python multi-paradigm?
A: Yes
"""


# ============================================================
#             10 QUESTIONS YOU MUST KNOW
# ============================================================

"""
If an interviewer says:

"Tell me about Python."

Your answer should cover:

1. What Python is
2. Who created it
3. When it was first released
4. Why it was created
5. Why it is called Python
6. Major features
7. Python 2 vs Python 3
8. Major applications
9. Advantages
10. Why Python is popular


A GOOD 30-SECOND INTERVIEW ANSWER:

"Python is a high-level, general-purpose programming
language created by Guido van Rossum. Its first public
release was in 1991. Python was designed with a strong
focus on readability and developer productivity.

It supports multiple programming paradigms and is widely
used in web development, automation, data science,
artificial intelligence, machine learning, and software
development.

Python is popular because it has simple syntax, a large
ecosystem, extensive libraries, and a large developer
community."


# ============================================================
#                    FINAL REVISION
# ============================================================

""
PYTHON
   |
   +---- Created by Guido van Rossum
   |
   +---- First public release: 1991
   |
   +---- Python 1.0: 1994
   |
   +---- Python 2.0: 2000
   |
   +---- Python 3.0: 2008
   |
   +---- Python 2 EOL: 2020
   |
   +---- Modern version family: Python 3
   |
   +---- Reference implementation: CPython
   |
   +---- Package repository: PyPI
   |
   +---- Package installer: pip
   |
   +---- Style guide: PEP 8
   |
   +---- Enhancement proposals: PEPs
   |
   +---- Organization: PSF
   |
   +---- Name inspired by: Monty Python
   |
   +---- Major areas:
          |
          +-- Web Development
          +-- AI / ML
          +-- Data Science
          +-- Automation
          +-- DevOps
          +-- Testing
          +-- Scientific Computing
          +-- Scripting
"""
