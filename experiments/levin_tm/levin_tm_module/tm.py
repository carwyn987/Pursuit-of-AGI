from levin_tm_module.tape import TuringMachineTape

class TM:
    def __init__(self):
        # Define tapes
        self.program_working_tape = TuringMachineTape()
        self.input_tape = []
        self.output_tape = []

        # Define "pointers"
        self.input_ptr_idx = 0
        self.working_ptr_idx = 0
        self.program_ptr_idx = -1 # This pointer is required to stay negative in program space
        self.output_ptr_idx = 0

    def setup_program(self, program):
        self.program_working_tape.program_tape = program # replace with setter

    """
    Return Values:
    --------------
     -  0: Success
     - -1: Failure
     -  1: Halt
    """
    def apply(self):
        instruction_number = self.program_working_tape[self.program_ptr_idx]

        # Try to apply current program instruction
        try:
            match instruction_number:
                case -1:
                    # jumpleq(address1, address2, address3)
                    # If the contents of address1 is less than or equal to the contents of address2, the InstructionPointer is set equal to address3
                    move_forward = 4 # CONDITIONAL
                case -2:
                    # output(...)
                    # A primitive for interaction with the external environment. It corresponds to the TM action of "writing the output tape"
                    move_forward = 1
                case -3:
                    # jump(address1)
                    # The InstructionPointer is set equal to address1
                    self.program_ptr_idx = self.program[self.program_ptr_idx+1]
                    move_forward = 0
                case -4:
                    # stop()
                    # Halt the current program
                    return 1
                case -5:
                    # add(address1, address2, address3)
                    # The contents of address1 is added to the contents of address2, the result is written into address3
                    move_forward = 4
                case -6:
                    # getInput(address1, address2)
                    # Reads the current value of the ith input (value at address1) into address2.
                    move_forward = 3
                case -7:
                    # move(address1, address2)
                    # The contents of address1 is copied into address2
                    move_forward = 3
                case -8:
                    # allocate(address1)
                    # The size of the working tape is increased by the value found in address1, initializing all cells to zero. Allocate is limited to 5 at any one invocation.
                    move_forward = 2
                case -9:
                    # Increment(address1) - on working tape
                    # The contents of address1 is incremented
                    self.working_tape[self.program[self.program_ptr_idx+1]] += 1
                    move_forward = 2
                case -10:
                    # Decrement(address1) - on working tape
                    # The contents of address1 is decremented
                    self.working_tape[self.program[self.program_ptr_idx+1]] -= 1
                    move_forward = 2
                case -11:
                    # subtract(address1, address2, address3)
                    # The contents of address1 is subtracted from the contents of address2, the result is written to address3
                    move_forward = 4
                case -12:
                    # multiply(address1, address2, address3)
                    # The contents of address1 is multiplied by the contents of address2, the result is written to address3
                    move_forward = 4
                case -13:
                    # free(address1)
                    # The size of the workig tape is decreased by the value found in address1. Min is updated accordingly.
                    move_forward = 2
                case _:
                    raise NotImplementedError()
            
        except:
            # Executing program instruction failed
            return -1.
            
        # Move program pointer
        self.program_ptr_idx += -1*move_forward

        # Check bounds of program
        if self.program_working_tape[self.program_ptr_idx] is None:
            return 1.
        
        # Executed correctly and still within program bounds
        return 0.