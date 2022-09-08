def is_present_in_any_wash(clothe, washes):
    is_present = False

    for wash in washes:
        if clothe in wash[0]:
            is_present = True
    return is_present


class LaundryManager:

    def __init__(self, laundry):
        self.laundry = laundry

    def calculate_washes(self):
        quantity_washes = 0

        wash = []
        washes = []
        self.laundry.clothes = sorted(self.laundry.clothes, key=lambda x: getattr(x, 'duration'), reverse=True)

        for clothe in self.laundry.clothes:
            wash = [clothe.id]
            #if is_not_present_in_any_wash(incompatibility, washes):
            for incompatibility in self.laundry.incompatibilities:
                if self.are_compatibles(clothe.id, incompatibility) and not is_present_in_any_wash(incompatibility, washes):
                    wash.append(incompatibility)
            if len(wash) > 1:
                washes.append([wash, clothe.duration])
        return washes

    def are_compatibles(self, clothe, incompatibility):
        return clothe not in self.laundry.incompatibilities[incompatibility] and clothe != incompatibility
