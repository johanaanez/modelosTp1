import csv

from laundry.laundry import Laundry


class LaundryFactory:

    @staticmethod
    def Load(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=' ')
            next(reader)
            next(reader)
            row3 = next(reader)

            quantity_clothes = int(row3[2])
            quantity_incompatibilities = int(row3[3])
            wash = Laundry(quantity_incompatibilities, quantity_clothes)

            for row in reader:
                if row[0] == 'e':
                    wash.add_incompatibilities(int(row[1]), int(row[2]))
                if row[0] == 'n':
                    wash.add_clothes(int(row[1]), int(row[2]))

        file.close()

        return wash

    @staticmethod
    def output(washes):
        washes_formated = []
        j = 0
        for wash in washes:
            j += 1
            for i in wash[0]:
                washes_formated.append([i,j])

        with open("primer_problema.txt", "w", newline='') as file:
            writer = csv.writer(file, delimiter=' ')
            writer.writerows(washes_formated)

        file.close()
