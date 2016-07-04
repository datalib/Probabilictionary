debug = True


class Probabilictionary():
    def __init__(self, events):
        self.events = [set(event) for event in events]

    def __getitem__(self, key):
        return Probabilictionary([event - set(key) for event in self.events if key in event])
        # return [event - set(key) for event in self.events if key in event]

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
