def baseline(starting: list[str], modified: list[str], correct: int = 2, incorrect: int = 1):
    scores = [None, None]

    def walk(i, j, score, aligment: list): # 3 options, ran across i and j, Big O should be 3^(n+m)
        if i == len(starting) and j == len(modified):
            if scores[0] is None or scores[0] < 0:
                scores[0] = score
                scores[1] = aligment[:]
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



def main():
    list1 = ["NOP", "MOV", "JMP", "NOP"]
    list2 = ["MOV", "JMP"]
    print(baseline(list1, list2))

if __name__ == "__main__":
    main()