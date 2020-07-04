import sys
from time import ctime
from argparse import ArgumentParser, FileType 
from os import path

def valid_file_path(filepath):
    absolute_path = path.abspath(filepath)
    (dirpath, _) = path.split(absolute_path)
    if not path.exists(dirpath):
        return (False, "Directory path does not exist")
    return (True, None)

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("filepath", help="The filepath to edit.")
    parser.add_argument("note", help="The note to add to the file.")

    parser.add_argument("-m", "--mode", 
            choices=("a", "append", "o", "overwrite"),
            help = "The mode of operation on the file.  Both modes will create a new file\
                if it does not exit.  Append will add to a file while overwrite will recreate\
                the file and add the note after.\
                Default: append",
            default="a"
    )

    args = parser.parse_args()
    
    file_handle = None

    valid = valid_file_path(args.filepath)

    if valid[0] == False:
        print(valid[0])
        sys.exit(1)
    
    if args.mode in ("a", "append"):
        file_handle = open(args.filepath, "a")
    elif args.mode in ("o", "overwrite"):
        file_handle = open(args.filepath, "w")
    else:
        parser.print_help()
        sys.exit(2)

    print("test")
    print (file_handle)
    file_handle.write(f"{ctime()}\n")
    file_handle.write(f"{str(args.note)}\n\n")

    file_handle.close()