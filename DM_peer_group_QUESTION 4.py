import random


# we are going to first find the relation in set A
class Relation:
    def __init__(self, setA, sub, product):
        self.setA = setA
        self.product = product
        self.sub = sub

    def relationA(self):
        for x in range(len(self.setA)):
            for y in range(len(self.setA)):
                self.product.extend([[self.setA[x], self.setA[y]]])
        print(f"set A {self.setA}")
        print(f"the relation AxA is {self.product}")

    def checkSubset(self, Subset, notSubset):
        print(f"set R {self.sub}")
        if len(self.sub) != 0:
            for a in range(len(self.sub)):
                if self.sub[a] in self.product:
                    Subset.append(self.sub[a])

                else:
                    notSubset.append(self.sub[a])

            if len(self.sub) == len(Subset):
                print("")
                print(f"subsets of AxA in set R is(are) {Subset}")
                print(f"set R is a subset of relation of AxA because all elements of R are in relation AxA")
                print("")
                print(f"R is a relation to A")

            else:
                print("")
                print(f"subsets of AxA in set R is(are) {Subset}")
                print(f"set R is a proper subset of relation AxA because it has {notSubset} element(s) that are not in relation AxA ")
                print("")
                print(f"R is a relation to A")

        elif len(self.sub) == 0:
            print("")
            print(f"set R is not a subset of relation AxA, it has no elements")
            print("")
            print(f"R is not a relation to A")


# relation = Relation([1, 2, 3, 4], [], [[2, 2], [3, 2], [2, 5]])
# relation.relationA()
# relation.checkSubset([], [])

# we are going to find The Reflexive relation
class Reflexive(Relation):
    def reflexive(self, a):
        print("")
        for z in range(len(self.sub)):
            for x in range(len(self.sub[z])):
                if self.sub[z][0] == self.sub[z][1]:
                    a.extend([[self.sub[z][0], self.sub[z][1]]])
                    break
                else:
                    continue
        if len(a) != 0:
            print(f"set R is reflexive to AxA relation, {a}")

        elif len(a) == 0:
            print(f"set R is not reflexive to AxA relation, {a}")


# relation = Reflexive([1, 2, 3, 4], [], [[2, 2], [3, 2], [2, 5]])
# relation.relationA()
# relation.checkSubset([], [])
# relation.reflexive([])

# we are going to find the Transitive relation
class Transitive(Reflexive):
    def trans(self, b, c):
        """
        transitive of a set is when (a,b)∈ AxA and (b,c)∈ AxA, then (a,c)∈ AxA
        so in this function we need to find (a,b), (b,c) and show that (a,c)∈ AxA
        :param c:
        :param b:
        :return:
        """
        print(" ")
        for n in range(len(self.sub)):
            if self.sub[n] in self.product:
                rand = random.randint(1, 5)
                b.extend([[self.sub[n][1], rand]])
                c.extend([[self.sub[n][0], rand]])

                for j in range(len(b)):
                    for q in range(len(c)):
                        if n == j == q:
                            if b[j] and c[q] in self.product:
                                print(f"{self.sub[n]} and {b[j]}, then {c[q]}, it is transitive because {b[j]} and {c[q]} are in relation AxA")
                                break
                            else:
                                print(f"{self.sub[n]} and {b[j]}, then {c[q]}, it is not transitive because {b[j]} and {c[q]} aren't in relation AxA")
                                break
                        else:
                            continue
            else:
                print(f"{self.sub[n]} is not in relation AxA, hence it has no transitive relation")


# trans = Transitive([1, 2, 3, 4], [], [[2, 2], [3, 2], [2, 5]])
# trans.relationA()
# trans.checkSubset([], [])
# trans.trans([], [])


# we are going to find the Symmetry relation
class Symmetric(Transitive):
    def symmetry(self, d):
        print("")
        for o in range(len(self.sub)):
            if self.sub[o] in self.product:
                d.extend([[self.sub[o][1], self.sub[o][0]]])
                for g in range(len(d)):
                    if d[g] in self.product:
                        if o == g:
                            print(f"{self.sub[o]} and {d[g]} are in relation AxA, there is symmetry relation")
                        else:
                            continue
                    else:
                        print(f"{d[g]} is not relation AxA, so there is no symmetry")

            else:
                print(f"{self.sub[o]} is not in relation AxA, hence it has no symmetry relation")
                continue


# output result of our program
relation = Symmetric([1, 2, 3, 4], [[1, 2], [2, 2], [3, 2], [2, 5]], [])
relation.relationA()
relation.checkSubset([], [])
relation.reflexive([])
relation.trans([], [])
relation.symmetry([])

