import random

def strand_generator(length: int, mutations: int, s: int | None = None):
    """
    Generate a starting strand and a mutated strand of instructions.

    The function first creates a random starting strand of the given length
    by sampling from a fixed set of instruction strings. It then makes a copy
    of this strand as the modified strand. Finally, it applies a number of
    random mutations (insertions or deletions) to either the starting strand
    or the modified strand, chosen independently for each mutation.

    Parameters
    ----------
    length : int
        Initial length of both strands.
    mutations : int
        Number of mutation operations to perform.
    s : int or None, optional
        If not None, seed the random number generator with this value for
        reproducible results. Default is None.

    Returns
    -------
    starting_strand : list of str
        The (possibly mutated) starting strand.
    modified_strand : list of str
        The (possibly mutated) modified strand.
    """
    INSTRUCTIONS = ["CMP", "CBW", "NOP", "CWD", "DIV", "DEC", "INC", "JMP", "MOV"]
    if s is not None:
        random.seed(s)

    # Build the initial starting strand
    starting_strand = []
    for _ in range(length):
        new_inst = INSTRUCTIONS[random.randint(0, len(INSTRUCTIONS) - 1)]
        starting_strand.append(new_inst)

    # Make a copy for the modified strand
    modified_strand = starting_strand[:]

    # Apply mutations
    for _ in range(mutations):
        # Randomly choose which strand to mutate: 0 = starting, 1 = modified
        list_pic = random.randint(0,1)

        if list_pic == 0:
            add_remove = random.randint(0,1)
            if add_remove == 0:
                 # Insert a random instruction at a random position
                starting_strand.insert(random.randint(0, len(starting_strand) - 1), INSTRUCTIONS[random.randint(0, len(INSTRUCTIONS) - 1)])
            else:
                # Remove a random instruction
                starting_strand.pop(random.randint(0, len(starting_strand) - 1)) 

        if list_pic == 1:
            add_remove = random.randint(0,1)
            if add_remove == 0:
                modified_strand.insert(random.randint(0, len(modified_strand) - 1), INSTRUCTIONS[random.randint(0, len(INSTRUCTIONS) - 1)])
            else:
                modified_strand.pop(random.randint(0, len(modified_strand) - 1))

    return starting_strand, modified_strand 
    

def baseline(starting: list[str], modified: list[str], correct: int = 2, incorrect: int = 1):
    """
    Compute the optimal alignment score and alignment path using brute force.

    This function exhaustively explores all possible alignments (match, gap in
    modified, gap in starting) via recursion.

    Parameters
    ----------
    starting : list of str
        The starting sequence of instructions.
    modified : list of str
        The modified sequence of instructions.
    correct : int, optional
        Score awarded for a matching pair. Default is 2.
    incorrect : int, optional
        Penalty (positive value) subtracted for a gap. Default is 1.

    Returns
    -------
    list
        A two-element list: [best_score, best_alignment], where best_alignment
        is a list of tuples (starting_elem, modified_elem) representing the
        aligned pairs, with '-' used for gaps.
    """
    scores = [None, None] # [best_score, best_alignment]

    def walk(i: int, j: int, score: int, aligment: list): # 3 options, ran across i and j, Big O should be 3^(i+j)
        """
        Recursive helper that explores all alignment paths from (i, j).

        Parameters
        ----------
        i : int
            Current index in the starting strand.
        j : int
            Current index in the modified strand.
        score : int
            Accumulated alignment score so far.
        aligment : list of tuple
            Current alignment path (list of (a, b) pairs).
        """
        # Base case: both strands fully explored
        if i == len(starting) and j == len(modified):
            if scores[0] is None or scores[0] < score:
                scores[0] = score
                scores[1] = aligment[:] # copy the alignment
            return

        if i < len(starting) and j < len(modified) and starting[i] == modified[j]: # option 1
            aligment.append((starting[i], modified[j]))
            walk(i + 1, j + 1, score + correct, aligment)
            aligment.pop()

        if i < len(starting): # option 2
            aligment.append((starting[i], "-"))
            walk(i + 1, j, score - incorrect, aligment)
            aligment.pop()

        if j < len(modified): # option 3
            aligment.append(("-", modified[j]))
            walk(i, j + 1, score - incorrect, aligment)
            aligment.pop()

    walk(0, 0, 0, [])
    return(scores)


def soultion(starting: list[str], modified: list[str], correct: int = 2, incorrect: int = 1):
    """
    Compute the optimal alignment score and path using memoized recursion.

    Parameters
    ----------
    starting : list of str
        The starting sequence of instructions.
    modified : list of str
        The modified sequence of instructions.
    correct : int, optional
        Score awarded for a matching pair. Default is 2.
    incorrect : int, optional
        Penalty (positive value) subtracted for a gap. Default is 1.

    Returns
    -------
    list
        A two-element list: [best_score, best_alignment], where best_alignment
        is a list of tuples (starting_elem, modified_elem) representing the
        aligned pairs, with '-' used for gaps.
    """
    len_i, len_j = len(starting), len(modified)
    already_computed = {} # memoization cache: (i, j) -> [score, alignment]

    def walk(i: int, j: int): # 3 options, ran across i and j, Big O should be ij
        """
        Recursive helper that returns the best [score, alignment] from (i, j).

        Parameters
        ----------
        i : int
            Current index in the starting strand.
        j : int
            Current index in the modified strand.

        Returns
        -------
        list
            [best_score, best_alignment] for the suffix starting at (i, j).
        """
        # strand is already in memory
        if (i, j) in already_computed:
            return already_computed[(i, j)]

        # Base case: both strands fully consumed
        if i == len_i and j == len_j:
            return [0, []]

        score = [None, None]
        
        if i < len_i and j < len_j and starting[i] == modified[j]: # option 1
            inter_score, inter_aligment = walk(i + 1, j + 1)
            canident = [inter_score + correct, [(starting[i], modified[j])] + inter_aligment]
            if score[0] is None or canident[0] > score[0]:
                score = canident

        if i < len_i: # option 2
            inter_score, inter_aligment = walk(i + 1, j)
            canident = [inter_score - incorrect, [(starting[i], "-")] + inter_aligment]
            if score[0] is None or canident[0] > score[0]:
                score = canident

        if j < len(modified): # option 3
            inter_score, inter_aligment = walk(i, j + 1)
            canident = [inter_score - incorrect, [("-", modified[j])] + inter_aligment]
            if score[0] is None or canident[0] > score[0]:
                score = canident

        already_computed[(i, j)] = score
        return score

    score = walk(0, 0)
    return(score)



def main():
    list1, list2 = strand_generator(7, 4)
    print(baseline(list1, list2))
    print(soultion(list1, list2))

if __name__ == "__main__":
    main()