#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# Turing Machine simulator for Busy Beaver problem.
# More info at: http://www.catonmat.net/blog/busy-beaver
#
# Version 1.0
#

import sys

class Error(Exception):
    pass

class TuringMachine(object):
    def __init__(self, program, start, halt, init):
        self.program = program
        self.start = start
        self.halt = halt
        self.init = init
        self.tape = [self.init]
        self.pos = 0
        self.state = self.start
        self.set_tape_callback(None)
        self.tape_changed = 1
        self.movez = 0

    def run(self):
        tape_callback = self.get_tape_callback()
        while self.state != self.halt:
            if tape_callback:
                tape_callback(self.tape, self.tape_changed)

            lhs = self.get_lhs()
            rhs = self.get_rhs(lhs)

            new_state, new_symbol, move = rhs

            old_symbol = lhs[1]
            self.update_tape(old_symbol, new_symbol)
            self.update_state(new_state)
            self.move_head(move)

        if tape_callback:
            tape_callback(self.tape, self.tape_changed)

    def set_tape_callback(self, fn):
        self.tape_callback = fn

    def get_tape_callback(self):
        return self.tape_callback

    property(get_tape_callback, set_tape_callback)

    @property
    def moves(self):
        return self.movez

    def update_tape(self, old_symbol, new_symbol):
        if old_symbol != new_symbol:
            self.tape[self.pos] = new_symbol
            self.tape_changed += 1
        else:
            self.tape_changed = 0

    def update_state(self, state):
        self.state = state

    def get_lhs(self):
        under_cursor = self.tape[self.pos]
        lhs = self.state + under_cursor
        return lhs

    def get_rhs(self, lhs):
        if lhs not in self.program:
            raise Error('Could not find transition for state "%s".' % lhs)
        return self.program[lhs]

    def move_head(self, move):
        if move == 'l':
            self.pos -= 1
        elif move == 'r':
            self.pos += 1
        else:
            raise Error('Unknown move "%s". It can only be left or right.' % move)

        if self.pos < 0:
            self.tape.insert(0, self.init)
            self.pos = 0
        if self.pos >= len(self.tape):
            self.tape.append(self.init)

        self.movez += 1

beaver_programs = [
    { },

    {'a0': 'h1r' },

    {'a0': 'b1r', 'a1': 'b1l',
     'b0': 'a1l', 'b1': 'h1r'},

    {'a0': 'b1r', 'a1': 'h1r',
     'b0': 'c0r', 'b1': 'b1r',
     'c0': 'c1l', 'c1': 'a1l'},

    {'a0': 'b1r', 'a1': 'b1l',
     'b0': 'a1l', 'b1': 'c0l',
     'c0': 'h1r', 'c1': 'd1l',
     'd0': 'd1r', 'd1': 'a0r'},

    {'a0': 'b1l', 'a1': 'a1l',
     'b0': 'c1r', 'b1': 'b1r',
     'c0': 'a1l', 'c1': 'd1r',
     'd0': 'a1l', 'd1': 'e1r',
     'e0': 'h1r', 'e1': 'c0r'},

    {'a0': 'b1r', 'a1': 'e0l',
     'b0': 'c1l', 'b1': 'a0r',
     'c0': 'd1l', 'c1': 'c0r',
     'd0': 'e1l', 'd1': 'f0l',
     'e0': 'a1l', 'e1': 'c1l',
     'f0': 'e1l', 'f1': 'h1r'}
]

def busy_beaver(n):
    def tape_callback(tape, tape_changed):
        print ''.join(tape)

    program = beaver_programs[n]

    print "Running Busy Beaver with %d states." % n
    tm = TuringMachine(program, 'a', 'h', '0')
    tm.set_tape_callback(tape_callback)
    tm.run()
    print "Busy beaver finished in %d steps." % tm.moves

def usage():
    print "Usage: %s [1|2|3|4|5|6]" % sys.argv[0]
    print "Runs Busy Beaver problem for 1 or 2 or 3 or 4 or 5 or 6 states."
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv[1:]) < 1:
        usage()

    n = int(sys.argv[1])

    if n < 1 or n > 6:
        print "n must be between 1 and 6 inclusive"
        print
        usage()

    busy_beaver(n)

