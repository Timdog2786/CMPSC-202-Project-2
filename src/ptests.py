from main import baseline, soultion, strand_generator

def test_baseline():
    list1, list2 = strand_generator(4, 4, 11062026)
    answer = baseline(list1, list2)
    assert answer[0] == 2
    assert answer[1] == [('INC', '-'), ('-', 'JMP'), ('-', 'CWD'), ('NOP', 'NOP'), ('-', 'INC'), ('DIV', 'DIV'), ('DEC', 'DEC')]

def test_soultion():
    list1, list2 = strand_generator(4, 4, 11062026)
    answer = soultion(list1, list2)
    assert answer[0] == 2
    assert answer[1] == [('INC', '-'), ('-', 'JMP'), ('-', 'CWD'), ('NOP', 'NOP'), ('-', 'INC'), ('DIV', 'DIV'), ('DEC', 'DEC')]

def test_same_result():
    list1, list2 = strand_generator(4, 4, 11062026)
    answer, answer2 = baseline(list1, list2), soultion(list1, list2)
    assert answer == answer2

def test_empty_input():
    answer, answer2 = baseline([], []), soultion([], [])
    assert answer == [0, []]
    assert answer2 == answer
    answer, answer2 = baseline([], ["MOV"]), soultion([], ["MOV"])
    assert answer == [-1, [("-", "MOV")]]
    assert answer == answer2
