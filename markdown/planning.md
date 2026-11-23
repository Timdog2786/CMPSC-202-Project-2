# Planning and analysis

**Problem Formulation**  
You are a cybersecurity researcher analyzing two distinct strains of a new, highly obfuscated ransomware. The first binary is a sequence of $n$ assembly instructions, and the second is $m$ instructions. The malware authors have inserted junk code and deleted operational functions to evade antivirus signatures. You can align the binaries by matching identical instructions, or by inserting gaps in either sequence. Matching instructions score positive points, while inserting gaps incurs a penalty. Design an algorithm to align the sequences to maximize the similarity score, revealing the exact structural mutations the authors made.

Goal - align the sequences to maximize similarity score.

**Baseline Solutions**
To establish a functional baseline, we can implement a naive recursive strategy. This approach checks if the current indices of the two strands are equal to each other, then makes a recursive branch to capture every possibility. The algorithm is looking at one instruction in the list at a time and making three branches. The first one is to add a gap within the first strand, the second branch is to add a gap within the second strand, or if the alignment on both strands is correct, it will advance both strands while adding no gap. This will ensure that even if the strands are aligned, it checks the possibility that breaking that alignment to align further strands could result in a better score.

Inputs:
starting: a list of operations  
modified: another list of operations  
correct: how much to reward correct pairings  
incorrect: how much to punish adding gaps
```
def baseline(starting, modified, correct, incorrect):
    scores = points, the strand

    def walk(s_i, m_i, score, aligment: list):
        if s_i is the last index and m_i is the last index):
            if scores[points] is None or scores[points] < interation score:
                scores[points] = score
                scores[strand] = aligment[:]
            return

        if s_i isnt at the end of starting and m_i isnt at the end of starting and the strands are the same:
            aligment.append((starting[i], modified[j]))
            walk(s_i + 1, m_i + 1, score + correct, aligment)
            aligment.pop()

        if s_i isnt at the end of starting: # option 2
            aligment.append((starting[i], "-"))
            walk(s_i + 1, m_i, score - incorrect, aligment)
            aligment.pop()

        if m_i < isnt at the end of modified: # option 3
            aligment.append(("-", modified[j]))
            walk(s_i, m_i + 1, score - incorrect, aligment)
            aligment.pop()

    walk(start the recursive calss)
    return(scores)
``` 

**Algorithmic Strategy**
Our algorithmic strategy is dynamic programming, and our method is to store any already computed calculations in a dictionary and to return that value instead of repeating already computed solutions. Each branch's checks are nearly identical to the baseline algorithm. The main change is that it appends and records the score and alignment of each branch and stores them, to ensure further branches do not recompute already found solutions. This works because i and j represent how far the algorithm has gotten into each respective branch, and the best score it can achieve up to that point. We use memoization instead of a bottom-up approach because it allowed us to only have to tweak our baseline algorithm slightly, while making a bottom-up approach would have required a lot more brainstorming. Dynamic programming is required for this problem because each individual strand can be split into a subproblem of whether inserting a gap will increase the overall total score or not, so recursively checking every option is more efficient than testing every solution.

Inputs:  
starting: a list of operations  
modified: another list of operations  
correct: how much to reward correct pairings  
incorrect: how much to punish adding gaps
```
def soultion(starting: list[str], modified: list[str], correct: int = 2, incorrect: int = 1):
    len_i, len_j = length of starting list, length of modified list
    already_computed = empty dict

    def walk(i, j): 
        if (i, j) in already_computed:
            return score
        if base case:
            return [0, []]

        score = [points, strand]
        
        if i < len_i and j < len_j and starting[i] == modified[j]:
            inter_score, inter_aligment = walk(i + 1, j + 1)
            canident = [inter_score + correct, [(starting[i], modified[j])] + inter_aligment]
            if canident is better:
                score = canident

        if i < len_i: # option 2
            inter_score, inter_aligment = walk(i + 1, j)
            canident = [inter_score - incorrect, [(starting[i], "-")] + inter_aligment]
            if canident is better:
                score = canident

        if j < len(modified): # option 3
            inter_score, inter_aligment = walk(i, j + 1)
            canident = [inter_score - incorrect, [("-", modified[j])] + inter_aligment]
            if canident is better:
                score = canident

        already_computed[(i, j)] = score
        return score

    score = walk(0, 0)
    return(score)
```

# Complexity Analysis:


Our solution —
$O$ — $O(nm)$; the recursive function becomes closer to $O(1)$ as the dictionary fills up, and the dictionary only has $n \cdot m$ possible elements to store.  
$\Omega$ — The input data does not change the logic of the code blocks that run, as it needs to complete each walk before deciding the best score; therefore, Big $\Omega$ is the same as Big $O$, $O(nm)$.  
$\Theta$ — Since Big $O$ and Big $\Omega$ are the same, Big $\Theta$ is $\Theta(nm)$.

Baseline solution —
$O$ — $O(3^{n+m})$, as each walk function runs until completion even if it was already computed, and at each step three walk functions are called.  
$\Omega$ — The input data does not change the logic of the code blocks that run, as it needs to complete each walk before deciding the best score; therefore, Big $\Omega$ is the same as Big $O$, $O(3^{n+m})$.  
$\Theta$ — Since Big $O$ and Big $\Omega$ are the same, Big $\Theta$ is $\Theta(3^{n+m})$.
