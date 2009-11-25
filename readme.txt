This is an implementation of The Busy Beaver Problem in Python and C++.

It was written by Peteris Krumins (peter@catonmat.net).
His blog is at http://www.catonmat.net  --  good coders code, great reuse.

The code is licensed under the MIT license.

The code was written as a part of article "The Busy Beaver Problem" on my
website. The whole article can be read at:

    http://www.catonmat.net/blog/busy-beaver/

------------------------------------------------------------------------------

Table of contents:
    [1] Introduction to The Busy Beaver Problem.
    [2] Example Busy Beaver Turing Machine with 2 states.
    [3] Busy Beaver Turing Machines for 1, 2, 3, 4, 5, and 6 states.
    [4] busy-beaver.cpp and busy-beaver.py C++ and Python programs.
    [5] draw_turing_machine.pl Perl program.


[1]-Introduction-to-The-Busy-Beaver-Problem-----------------------------------

The busy beaver problem is a fun theoretical computer science problem to know.
Intuitively, the problem is to find the smallest program that outputs as many
data as possible and eventually *halts*.

More formally it goes like this - given an n-state Turing Machine with a two
symbol alphabet {0, 1}, what is the maximum number of 1s that the machine may
print on an initially blank tape (0-filled) before halting?

It turns out that this problem can't be solved. For a small number of states
it can be reasoned about, but it can't be solved in general. Theorists call
such problems non-computable.

Currently people have managed to solve it for n=1,2,3,4 (for Turing Machines
with 1, 2, 3 and 4 states) by reasoning about and running all the possible
Turing Machines, but for n = 5 this task has currently been impossible.
While most likely it will be solved for n=5, theorists doubt that it shall
ever be computed for n=6.

...

Continue reading on http://www.catonmat.net/blog/busy-beaver/


[2]-Example-Busy-Beaver-Turing-Machine-with-2-states--------------------------

Here is an example of a 2-state busy beaver. It's a Turing machine.

    a0 -> b1r    a1 -> b1l
    b0 -> a1l    b1 -> h1r

The initial tape is filled with 0's. The starting state is 'a' and the halting
state is 'h'. The notation 'a0 -> b1r' means "if we are in the state 'a' and
the current symbol on the tape is '0', then put a '1' in the current cell,
switch to state 'b' and move to the right 'r'. This process repeats until the
machine ends up in the halting state 'h'.

When run, it produces 4 ones on the tape and halts.

Here are all the tape changes. The tape is infinite and initially blank
(filled with 0's).

                . starting state
                | 
                v                  state change
                                   ------------
    ...|0|0|0|0|0|0|0|0|0|0|...    a0 -> b1r
    ...|0|0|0|0|1|0|0|0|0|0|...    b0 -> a1l
    ...|0|0|0|0|1|1|0|0|0|0|...    a1 -> b1l
    ...|0|0|0|0|1|1|0|0|0|0|...    b0 -> a1l
    ...|0|0|0|1|1|1|0|0|0|0|...    a0 -> b1r
    ...|0|0|1|1|1|1|0|0|0|0|...    b1 -> h1r  HALT
    ...|0|0|1|1|1|1|0|0|0|0|...

The busy beaver stopped after 6 steps and the tape got filled with 4 ones.
    

[3]-Busy-Beaver-Turing-Machines-for-1-2-3-4-5-and-6-states--------------------

Turing Machine for 1-state Busy Beaver:

    a0 -> h1r

    The tape gets filled with 1 one and it terminates after 1 step.

Turing Machine for 2-state Busy Beaver:

    a0 -> b1r    a1 -> b1l
    b0 -> a1l    b1 -> h1r

    The tape gets filled with 4 ones and it terminates after 6 steps.

Turing Machine for 3-state Busy Beaver:

    a0 -> b1r    a1 -> h1r
    b0 -> c0r    b1 -> b1r
    c0 -> c1l    c1 -> a1l

    The tape gets filled with 6 ones and it terminates after 14 steps.

Turing Machine for 4-state Busy Beaver:

    a0 -> b1r    a1 -> b1l
    b0 -> a1l    b1 -> c0l
    c0 -> h1r    c1 -> d1l
    d0 -> d1r    d1 -> a0r

    The tape gets filled with 13 ones and it terminates after 107 steps.

Turing Machine for 5-state Busy Beaver:

    a0 -> b1l    a1 -> a1l
    b0 -> c1r    b1 -> b1r
    c0 -> a1l    c1 -> d1r
    d0 -> a1l    d1 -> e1r
    e0 -> h1r    e1 -> c0r

    The tape gets filled with 4098 ones and it terminates after
    47176870 steps.

Turing Machine for 6 state Busy Beaver:

    a0 -> b1r    a1 -> e0l
    b0 -> c1l    b1 -> a0r
    c0 -> d1l    c1 -> c0r
    d0 -> e1l    d1 -> f0l
    e0 -> a1l    e1 -> c1l
    f0 -> e1l    f1 -> h1r

    Currently best 6 state Busy Beaver outputs 4.6e1439 ones and
    terminates after 2.8e2879 steps.

    This result is a theoretical approximation. There are aproximately
    0.3% of unchecked Turing Machines left.


[4]-busy-beaver.cpp-and-busy-beaver.py-programs-------------------------------

I decided to play with the busy beaver myself to verify the known results for
n <= 5. I implemented a Turing Machine in Python, which turned out to be too
slow, so I reimplemented it in C++.

I also wrote a visualization tool in Perl that shows how the Turing Machine's
tape changes from the start to the finish (see [5]).

The Python program is called busy-beaver.py and it takes one argument -
which n-state busy beaver to run.

The C++ program is called busy-beaver.cpp and takes the same argument.

Here is how to invoke the Python program:

    $ ./busy-beaver.py 2
    Running Busy Beaver with 2 states.
    0
    10
    11
    011
    0111
    1111
    1111
    Busy beaver finished in 6 steps.

The output is the tape changes and the final line tells us how many steps it
took.

You can use the tape change output and generate an image that shows the tape
changes in a much visual way. See the Perl program [5] below.

To use the C++ program, you have to first compile it:
    
    $ g++ busy-beaver.cpp -o busy-beaver

And then you can run it as any other program:

    $ ./busy-beaver 3
    Running Busy Beaver with 3 states.
    0
    10
    101
    111
    1111
    111101
    111111
    Busy Beaver finished in 14 steps.

[5]-draw_turing_machine.pl-Perl-program.

I also wrote a visualization program for the output from busy-beaver program.
It takes the 0's and 1's you see above and turns into a nice png image.

Take a look at the original article http://www.catonmat.net/blog/busy-beaver/
to see how these images look.

------------------------------------------------------------------------------

That's it. Enjoy the beavers! :)


Sincerely,
Peteris Krumins
http://www.catonmat.net

