def is_present_in_any_wash(clothe, washes):
    is_present = False

    for wash in washes:
        if clothe in wash[0]:
            is_present = True
    return is_present


def is_compatible_with_wash(incompatibilities, incompatibility, wash):
    is_compatible = True
    for i in wash:
        if i in incompatibilities[incompatibility]:
            is_compatible = False
    return is_compatible


def are_compatibles(clothe, incompatibility, incompatibilities, wash):
    return clothe != incompatibility and is_compatible_with_wash(incompatibilities, incompatibility, wash)


class LaundryManager:

    def __init__(self, laundry):
        self.laundry = laundry

    def apply(self):
        washes = []
        self.laundry.clothes = sorted(self.laundry.clothes, key=lambda x: getattr(x, 'duration'), reverse=True)

        for clothe in self.laundry.clothes:
            wash = []
            if not is_present_in_any_wash(clothe.id, washes):
                wash = [clothe.id]
            for incompatibility in self.laundry.incompatibilities:
                if are_compatibles(clothe.id, incompatibility, self.laundry.incompatibilities, wash) and not is_present_in_any_wash(incompatibility, washes):
                    wash.append(incompatibility)
            if len(wash) > 0:
                durations = list(map(lambda k: k.duration, list(filter(lambda x: x.id in wash, self.laundry.clothes))))
                max_duration = max(durations)
                washes.append([wash, max_duration])
        return washes

