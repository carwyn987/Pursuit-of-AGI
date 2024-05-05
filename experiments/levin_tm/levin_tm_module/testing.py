from levin_tm_module.losses.mse import index_match_MSE
import matplotlib.pyplot as plt

def test(best_tms, inputs, labels):
    """
    Takes a list of turing machines, and tests them, reporting results.
    """

    losses = []

    for tm in best_tms:

        print("Final TM: ", tm[1].program_working_tape)
        # print("Path through TM: ", tm[1].save_ran_instructions)
        # print("Output Tape: ", tm[1].output_tape)
        # print("Train Loss: ", fitness)
        test_loss = index_match_MSE(tm[1].output_tape, list(zip(list(range(len(labels))), labels)))
        print("Test Loss: ", test_loss) # I can simply use output tape for now since we haven't implemented input tape.
        losses.append(test_loss)
        # print("Exit: ", status)
        # print(f"in {steps} steps")

    print(sum(1 for x in losses if x == 0), " / ", len(losses), " were zero test loss (perfect generalization) = ", float(sum(1 for x in losses if x == 0))/len(losses))
    
    plt.hist(losses)
    plt.show() 