import random


def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]


def dpll(cnf, assignments={}):

    if len(cnf) == 0:
        return True, assignments

    if any([len(c) == 0 for c in cnf]):
        return False, None

    l = __select_literal(cnf)

    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals

    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals

    return False, None


def random_kcnf(n_literals, n_conjuncts, k=3):
    result = []
    for _ in range(n_conjuncts):
        conj = set()
        for _ in range(k):
            index = random.randint(0, n_literals)
            conj.add((
                str(index).rjust(10, '0'),
                bool(random.randint(0, 2)),
            ))
        result.append(conj)
    return result


print(dpll(random_kcnf(2, 7)))
