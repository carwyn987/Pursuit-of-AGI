import random

def generate_random_program():
    
    # write_program_to = [-20, -1]
    # program_write_range = [0,13] # based off of potential instructions
    # working_tape_writing_range = [0, 20]

    # how_many_working_to_write_post_which_program_instr = {
    #     0: 2,
    #     1: 0,
    #     2: 0,
    #     3: 0,
    #     4: 2,
    #     5: 0,
    #     6: 2,
    #     7: 1,
    #     8: 1,
    #     9: 1,
    #     10: 3,
    #     11: 3,
    #     12: 1,
    # }

    # pick a number of instructions to write
    num_instr_to_write = 10*3 # *3 to account for arguments
    range_to_pick_from = (-13,10)

    program = []

    for i in range(num_instr_to_write):
        program.append(random.randint(*range_to_pick_from))

    return program
