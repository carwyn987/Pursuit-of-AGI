def MSE(output_tape, labels, penalize_size_mismatch=True):
    # Store shorter list as x
    if len(output_tape) > len(labels):
        x = labels
        y = output_tape
    else:
        x = output_tape
        y = labels

    mse = 0
    for i in range(len(x)):
        mse += (x[i] - y[i])**2

    if len(y) > len(x):
        for i in range(len(x), len(y)):
            mse += y[i]**2
            if penalize_size_mismatch:
                mse += 1

    return mse

def index_match_MSE(output_tape, indx_label_tuples):
    """
    Arguments:
    ----------
     - output_tape (list): output of tm
     - indx_label_tuples (list): A list of tuples specifying specific outputs. E.g. [(0,1), (1,1), (2,1), (3,1)]

    Returns:
    ----------
     - MSE of output with specified labels
    """

    mse = 0
    for tup in indx_label_tuples:
        if tup[0] < len(output_tape) and sum([1 for x in output_tape if x is None]) == 0:
            try:
                mse += (tup[1]-output_tape[tup[0]])**2
            except:
                print(tup, output_tape)
                raise ValueError()
        else:
            mse += tup[1]**2 + 1 # penalize anything that's not written on output tape

    return mse