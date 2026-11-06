# Planning and analysis

**Problem Formulation**  
You are a cybersecurity researcher analyzing two distinct strains of a new, highly obfuscated ransomware. The first binary is a sequence of $n$ assembly instructions, and the second is $m$ instructions. The malware authors have inserted junk code and deleted operational functions to evade antivirus signatures. You can align the binaries by matching identical instructions, or by inserting gaps in either sequence. Matching instructions score positive points, while inserting gaps incurs a penalty. Design an algorithm to align the sequences to maximize the similarity score, revealing the exact structural mutations the authors made.

Goal - align the sequences to maximize similarity score

**Baseline Solutions**
To establish a functional baseline, we can implement a naive recursive strategy. This approach checks if the current index of the 2 strands are equal to each other, then making a recusive branch to capture every possibility.

Inputs:
starting: an list of operations
modified: another list of operations
correct: how much to reward correct parings
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
Our algorithemic dyanmic, and our method is to store any already computered calaulations into a dictoarny and to return that value instead of repeating already computered soultions.

Inputs:
starting: an list of operations
modified: another list of operations
correct: how much to reward correct parings
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


Our solution - 
$O$ - O(nm) the recusrive function becames closer to O(1) as the dictoanary fills up, and the dictonaray only has n*m possible elements to store
$Ω$ - The input of data does not change the logic of code blocks the code runs, as it needs to complete a each walk before dedicing the best score therefor Big Ω is the same as Big O of O(nm) = n*m
$ϴ$ - since Big O and Big Ω are the same, Big ϴ is ϴ(nm) = n*m
Baseline solution -
$O$ - O(3^(n+m)) as each walk fuction runs until completeion even if it was already computed, and at each step 3 walk functions are called. 
$Ω$ - The input of data does not change the logic of code blocks the code runs, as it needs to complete a each walk before dedicing the best score therefor Big Ω is the same as Big O of O(nm) = 3^n+m
$ϴ$ - since Big O and Big Ω are the same, Big ϴ is ϴ(n) = 3^n+m

