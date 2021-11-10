class Sets:
    def __init__(self, set_a, set_b):
        self.set_a = set_a
        self.set_b = set_b
        print(''' \n
            We are going to first define set A and set B, then answer:
                  a) if B is A 
                  b) the set difference of A, (i.e., A - B)
                  c) the cross product of A and B, (i.e., A × B\n''')
        asking_a = input('Please add elements in set A ')
        set_a.update(asking_a)
        asking_b = input('Please add elements in set B ')
        set_b.update(asking_b)

        print(f'\n  Your sets are: \n Set A = {set_a} \n Set B = {set_b}')

    def B_subset_of_A(self):
        truth_value = 0
        for element in self.set_a:
            for member in self.set_b:
                if member == element:
                    truth_value += 1
        if len(self.set_b) == truth_value:
            return f'\n  a) The truth value of B ⊆ A is {True}.\n  Hence, B is a subset of A '
        else:
            return f'\n  a) The truth value of B ⊆ A is {False}.\n Hence, B is not a subset of A'

    def set_A_minus_set_B(self):
        set_a_minus_b = set()
        for element in self.set_a:
            if element not in self.set_b:
                set_a_minus_b.add(element)
        return f'\n  b) The set A − B = {set_a_minus_b}'

    def A_cross_B(self):
        a_cross_b = set()
        for element in self.set_a:
            for member in self.set_b:
                a_cross_b.add((element, member))
        return f'\n  c) The set A × B = {a_cross_b}'


c = Sets(set_a=set(), set_b=set())
print(c.B_subset_of_A())
print(c.set_A_minus_set_B())
print(c.A_cross_B())