from gs2.problem1 import solution as problem1


def test_bs_between_ws(solution):
    expected = "Bob"
    actual =  solution.winner("wwwbbbbwww")
    # print('actual:{0} '.format(actual))
    assert actual == expected

def test_allws(solution):
    expected = "Wendy"
    actual =  solution.winner("www")
    # print('actual:{0} '.format(actual))
    assert actual == expected

#driver code:
'''
games = [
         ("wwwbbbbwww","Bob"),
         ("www","Wendy"),
         ("bbbbbwwwwwwbbwwwbwbwww","Wendy"),
         ("wbbbbw","Bob"),
         ("wwwbbb","Bob")
]
result = list(map(lambda x : winner(x[0]) == x[1],games))
if sum(result) == len(games):
  print("tests passed!")
else:
  print("tests failed! results: ", result)   
'''
def main():
    solution = problem1.Solution(9, "Wendy and Bob game", "Easy")
    test_bs_between_ws(solution)    
    test_allws(solution)
    # TODO:  MP, AG3 - there are other test cases here?


if __name__ == "__main__":
    main()
