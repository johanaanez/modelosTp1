import args
from laundry.laundry_factory import LaundryFactory
from laundry.laundry_manager import LaundryManager

def main():
    # obtención de argumentos
    arguments = args.parse_arguments()
    #file = arguments.file
    file = 'laundry/input.txt'

    # cargar datos de los lavados
    laundry = LaundryFactory.Load(file)

    # calcular cantidad de lavados
    manager = LaundryManager(laundry)
    washes = manager.apply_ordered()

    # escribir en el archivo de salida
    LaundryFactory.output(washes)
    
if __name__ == '__main__':
    main()
