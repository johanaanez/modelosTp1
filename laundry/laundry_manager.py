from laundry.wash import Wash


def is_present_in_any_wash(clothe, washes):
    is_present = False

    for wash in washes:
        if clothe in wash.clothes:
            is_present = True
    return is_present


class LaundryManager:

    def __init__(self, laundry):
        self.laundry = laundry

    def calculate_washes(self):
        washes = []
        self.laundry.clothes = sorted(self.laundry.clothes, key=lambda x: getattr(x, 'duration'), reverse=True)

        for clothe in self.laundry.clothes:
            wash = []
            if not is_present_in_any_wash(clothe.id, washes):
                wash = [clothe.id]
            for incompatibility in self.laundry.incompatibilities:
                if self.are_compatibles(clothe.id, incompatibility) and not is_present_in_any_wash(incompatibility, washes):
                    wash.append(incompatibility)
            if len(wash) > 1:
                durations = list(map(lambda k: k.duration, list(filter(lambda x: x.id in wash, self.laundry.clothes))))
                max_duration = max(durations)
                washes.append(Wash(wash, max_duration))
        return washes

    def are_compatibles(self, clothe, incompatibility):
        return clothe not in self.laundry.incompatibilities[incompatibility] and clothe != incompatibility
