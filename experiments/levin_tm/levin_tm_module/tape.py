class TuringMachineTape:
    def __init__(self):
        self.working_tape = []
        self.program_tape = []

    def append_to_working_tape(self, item):
        self.working_tape.append(item)

    def append_to_program_tape(self, item):
        self.program_tape.append(item)

    def pop_from_working_tape(self):
        return self.working_tape.pop() if self.working_tape else None

    def pop_from_program_tape(self):
        return self.program_tape.pop() if self.program_tape else None

    def __getitem__(self, index):
        if index >= 0:
            if index < len(self.working_tape):
                return self.working_tape[index]
            else:
                return None
        else:
            index = abs(index) - 1
            if index < len(self.program_tape):
                return self.program_tape[index]
            else:
                return None

    def __setitem__(self, index, value):
        if index >= 0:
            if index < len(self.working_tape):
                self.working_tape[index] = value
            else:
                self.working_tape.extend([None] * (index - len(self.working_tape) + 1))
                self.working_tape[index] = value
        else:
            index = abs(index) - 1
            if index < len(self.program_tape):
                self.program_tape[index] = value
            else:
                self.program_tape.extend([None] * (index - len(self.program_tape) + 1))
                self.program_tape[index] = value

    def __str__(self):
        return str(list(reversed(self.program_tape))) + str(self.working_tape)
    
    def verbose(self):
        s = (
            "Program Tape: " + str(self.program_tape) + "\n"
            "Working Tape: " + str(self.working_tape) + "\n"
            "Number Line Indexed: " + str(list(reversed(self.program_tape))) + str(self.working_tape)
            )
        return s
    
    def length_of_working_tape(self):
        return len(self.working_tape)

    def length_of_program_tape(self):
        return len(self.program_tape)
       

if __name__ == "__main__":
    print("TESTING TuringMachineTape")
    tape = TuringMachineTape()    # [program_tape][working_tape]
    
    # Test append
    print("\nTesting Append Fns")
    tape.append_to_working_tape('a')
    print("Working append 'a': ", tape) # [][a]

    tape.append_to_working_tape('b')
    print("Working append 'b': ", tape) # [][a, b]
    
    tape.append_to_program_tape('1')
    print("Program append '1': ", tape) # [1][a, b]
    
    tape.append_to_program_tape('2')
    print("Program append '2': ", tape) # [2, 1][a, b]
       # Index:   -2,-1, 0, 1

    # Test len
    print("\nTesting Length Fns")
    print("tape.length_of_working_tape(): ", tape.length_of_working_tape())  # Output: 2
    print("tape.length_of_program_tape(): ", tape.length_of_program_tape())  # Output: 2

    # Test positive index access
    print("\nTesting Positive Indexing")
    print("tape[0] = ", tape[0])    # Output: 'a'
    print("tape[1] = ", tape[1])    # Output: 'b'
    print("tape[2] = ", tape[2])    # Output: None

    # Test negative index access
    print("\nTesting Negative Indexing")
    print("tape[-1] = ", tape[-1])   # Output: '2'
    print("tape[-2] = ", tape[-2])   # Output: '1'
    print("tape[-3] = ", tape[-3])   # Output: None


    # Test pop
    print("\nTesting Pop Fns")
    print("tape.pop_from_working_tape(): ", tape.pop_from_working_tape())  # Output: 'b'
    print("tape.pop_from_program_tape(): ", tape.pop_from_program_tape())  # Output: '2'
    print("tape.pop_from_working_tape(): ", tape.pop_from_working_tape())  # Output: 'a'
    print("tape.pop_from_program_tape(): ", tape.pop_from_program_tape())  # Output: '1'
    print("tape.pop_from_working_tape(): ", tape.pop_from_working_tape())  # Output: None
    print("tape.pop_from_program_tape(): ", tape.pop_from_program_tape())  # Output: None
