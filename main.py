import args
from laundry.laundry_factory import LaundryFactory
from laundry.laundry_manager import LaundryManager

def main():
    # obtención de argumentos
    arguments = args.parse_arguments()
    verbose = bool(arguments.verbose)
    #file = arguments.file
    file = 'laundry/input.txt'

    # cargar grafo
    laundry = LaundryFactory.Load(file)

    # procesar grafo
    manager = LaundryManager(laundry)
    result = manager.calculate_washes()

    print(result)
    
if __name__ == '__main__':
    main()
