import sys
from hash_table import *

prog_name = "DictDemo"

# /** Default initial hash table size. */
DEFAULT_HASH_SIZE = 10

# /** Default max load factor before rehashing occurs. */
MAX_LOAD_FACTOR = 0.75

# List of operations.
# op = ["END", "LIST", "REMOVE", "LOOKUP", "UNKNOWN"]


def print_help():
    # Print help information.
    print("Available commands:")
    print("    delete <key>")
    print("    lookup <key>")
    print("    list")
    print("    end/exit/quit")


def get_next_option(table):
    """
    * Process next operation.
    * 
    * @param table Hash table.   
    """
    operation = "UNKNOWN"


    while operation != "END":
        command = input("Enter command: ").split()

        # deletion
        if command[0] == "delete":
            operation = "REMOVE"
            key = command[1]
            table.delete(key)

        # lookup/search
        elif command[0] == "lookup":
                operation = "LOOKUP"
                key = command[1]
                value = table.lookup(key)
                
                if value == None:
                    print(f"key {key} not found!")
                else:
                    print(f"{key} : {value}")

        # list contents of hash table
        elif command[0] =="list":
            operation = "LIST"
            print(table)

        # quit
        elif command[0] == "end":
                operation = "END"
        elif command[0] == "exit":
            operation = "END"
        elif command[0] == "quit":
            operation = "END"
        else:
            operation = "UNKNOWN"
            print("Unknown command")
            print_help()


def main():


    args = sys.argv[1:]
    if (len(args) != 1):
        print(f"Usage: {prog_name} <datafile.dat>")
        exit(1)


    # create empty hash table
    print("creating hash table.")
    table =  HashTable(DEFAULT_HASH_SIZE, MAX_LOAD_FACTOR)

    file_name = args[0]
    with open(file_name) as f:
        lines = f.readlines()
    print("reading data")

    # read in data from file and construction hash table

    for line in lines:
        fields = line.split(",")

        key = fields[0]
        value = fields[1]

        table.insert(key, value)

    print_help()

    # /* enter the 'mini' shell */
    get_next_option(table)

if __name__ == "__main__":
    main()