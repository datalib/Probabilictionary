debug = True


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l)):
        yield l[i:i + n]


def weighted_choice(choices):
    import random
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w

    assert False, "Shouldn't get here"


def normalize(freq_dist):
    norm_const = sum(freq_dist.values())
    return Counter({k: v / norm_const for k, v in freq_dist.items()})


from collections import Counter


class Probabilictionary():
    # TODO: Rename *events* to *outcomes*
    # TODO: Check *outcomes* type and add appropriate logic
    def __init__(self, events, ordered=False):
        # check *events* type
        if ordered:
            from ordered_set import OrderedSet
            set_constructor = OrderedSet
        else:
            set_constructor = set

        self.ordered = ordered

        # Temporary
        self._prob_dist = normalize(Counter([outcome for event in events
                                             for outcome in event]))

        self.events = [set_constructor(event) for event in events]

    def __getitem__(self, key):
        if self.ordered:
            factored_subspaces = [event - {key} for event in self.events if key == event[0]]
        else:
            factored_subspaces = [event - {key} for event in self.events if key in event]

        return Probabilictionary(factored_subspaces, ordered=self.ordered)

    def __repr__(self):
        return str(self.events)

    def S(self):
        return set(self.freq_dist)

    def P(self, *args, **kwargs):
        if debug:
            print("args:", args)
            print("len(args)", len(args))
            print("type(args)", type(args))
            print("kwargs:", kwargs)
            print("len(kwargs)", len(kwargs))
            print("type(kwargs)", type(kwargs))

        return sum(1 for event in self.events if set(args).issubset(event)) / len(self.events)
