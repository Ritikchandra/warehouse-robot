class State:
    def __init__(self, x, y, remaining_items, collected_items, energy):
        self.x = x
        self.y = y
        self.remaining_items = tuple(sorted(remaining_items))
        self.collected_items = tuple(sorted(collected_items))
        self.energy = energy

    def __hash__(self):
        return hash((self.x, self.y,
                     self.remaining_items,
                     self.collected_items,
                     self.energy))

    def __eq__(self, other):
        return (self.x, self.y,
                self.remaining_items,
                self.collected_items,
                self.energy) == \
               (other.x, other.y,
                other.remaining_items,
                other.collected_items,
                other.energy)