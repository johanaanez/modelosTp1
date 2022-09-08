from laundry.clothe import Clothe


class Laundry:

    def __init__(self, quantity_incompatibilities, quantity_clothes):
        self.quantity_incompatibilities = quantity_incompatibilities
        self.incompatibilities = {}
        self.quantity_clothes = quantity_clothes
        self.clothes = []

    def add_incompatibilities(self, id_clothe1, id_clothe2):
        if id_clothe1 not in self.incompatibilities:
            self.incompatibilities[id_clothe1] = []

        self.incompatibilities[id_clothe1].append(id_clothe2)

    def add_clothes(self, id, duration):
        self.clothes.append(Clothe(id, duration))
