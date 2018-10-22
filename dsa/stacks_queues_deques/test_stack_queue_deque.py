from .stack_queue_deque import *


def test_balance_paren():
    assert balance_check('[]') is True
    assert balance_check('[](){([[[]]])}') is True
    assert balance_check('()(){]}') is False
    assert balance_check('[](){([[[]]])}(') is False
    assert balance_check('[{{{(())}}}]((()))') is True
    assert balance_check('[[[]])]') is False


def test_queue_stack():
    q = Queue2Stacks()
    answer = []

    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        answer.append(q.dequeue())
    assert answer == [0, 1, 2, 3, 4]