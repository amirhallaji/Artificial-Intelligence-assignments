from copy import deepcopy

class CSP:

    def __init__(self, unassigned):
        self.unassigned = unassigned

    def is_consistent(self, assigned: dict, person: str, t):
        if person == 'Sohrab':
            return True

        elif person == 'Mehdi':
            if t in assigned['Sohrab']:
                    return True

        elif person == 'Nima':
            if t in assigned['Sohrab']:
                    return True

        return False

    # ------------------------------------------

    def backtrack_search(self, unassigned: dict, assigned: dict) -> dict:
        if len(unassigned) == 0:
            return assigned

        person = list(unassigned.keys())[0]
        times = unassigned[person]
        del unassigned[person]

        for t in times:
            consistent = self.is_consistent(assigned, person, t)
            if consistent:
                # adding it to our assigned dictionary if not added before
                if person in assigned:
                    assigned[person].append(t)
                else:
                    assigned[person] = list()
                    assigned[person].append(t)

                res = self.backtrack_search(unassigned, assigned)

                if res and len(res) == 3:
                    return res
                elif res and len(res) == 2:
                    return res
                else:
                    del assigned[person]

        return {}

    # ----------------------------------------


if __name__ == '__main__':

    # these 3 are our variable
    sohrab = input('Sohrab: ').split()
    mehdi = input('Mehdi: ').split()
    nima = input('Nima:').split()

    unassigned = {
        'Sohrab': sohrab,
        'Mehdi': mehdi,
        'Nima': nima,
    }

    assigned = {}
    csp = CSP(unassigned)
    res = csp.backtrack_search(unassigned, assigned)

    if res:
        print(res)
    else:
        print('No answer found!')