import argparse

def main():
    parser = argparse.ArgumentParser(description='Descripción de tu script')
    parser.add_argument('--opcion1', help='Descripción de la opción 1')
    parser.add_argument('--opcion2', help='Descripción de la opción 2')
    parser.add_argument('--opcion3', help='Descripción de la opción 3')
    parser.add_argument('--opcion4', help='Descripción de la opción 4')
    parser.add_argument('--opcion5', help='Descripción de la opción 5')
    parser.add_argument('--opcion6', help='Descripción de la opción 6')
    parser.add_argument('--opcion7', help='Descripción de la opción 7')
    parser.add_argument('--opcion8', help='Descripción de la opción 8')
    args = parser.parse_args()

    print("Opción 1:", args.opcion1)
    print("Opción 2:", args.opcion2)
    print("Opción 3:", args.opcion3)
    print("Opción 4:", args.opcion4)
    print("Opción 5:", args.opcion5)
    print("Opción 6:", args.opcion6)
    print("Opción 7:", args.opcion7)
    print("Opción 8:", args.opcion8)

if __name__ == "__main__":
    main()
