debug = True


class Probabilictionary():
    def __init__(self, events, ordered=False):
        if ordered:
            from ordered_set import OrderedSet
            set_constructor = OrderedSet
        else:
            set_constructor = set

        self.ordered = ordered

        self.S = {outcome for event in events for outcome in event}

        self.events = [set_constructor(event) for event in events]

    def __getitem__(self, key):
        if self.ordered:
            factored_subspaces = [event - {key} for event in self.events if key == event[0]]
        else:
            factored_subspaces = [event - {key} for event in self.events if key in event]

        return Probabilictionary(factored_subspaces, ordered=self.ordered)

    def __repr__(self):
        return str(self.events)

    def P(self, *args, **kwargs):
        if debug:
            print("args:", args)
            print("len(args)", len(args))
            print("type(args)", type(args))
            print("kwargs:", kwargs)
            print("len(kwargs)", len(kwargs))
            print("type(kwargs)", type(kwargs))

        return sum(1 for event in self.events if set(args).issubset(event)) / len(self.events)
