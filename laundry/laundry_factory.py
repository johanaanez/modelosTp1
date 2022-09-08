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
