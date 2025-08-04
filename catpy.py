import sys

__version__ = "0.70.1"
__author__ = "soonsimple, sun_chengbo@126.com"
__help__   = """
catpy - A Python version of the classic Unix command 'cat'.
Usage: catpy [options] [file ...]

Options:
  -n, --number  -   Number the output lines.
  -E, --ending  -   Display a '$' at the end of each line.
  -h, --help    -   Show this help message and exit.
  -v, --version -   Show the version of catpy and exit.
  
If no files are specified, catpy will read from standard input, 
and write to standard output.
"""

__license__ = "MIT License"

class Catpy:
    def __init__(self, args):
        self.numbered = False
        self.ending = False

        self.n = 0

        if "-v" in args or "--version" in args:
            print(__version__)
            exit(0)

        if "-h" in args or "--help" in args:
            print(__help__)
            exit(0)                                                             

        if "-n" in args:
            self.numbered = True
            args.remove("-n")
        elif "--number" in args:
            self.numbered = True
            args.remove("--number")

        if "-E" in args:
            self.ending = True
            args.remove("-E")
        elif "--ending" in args:
            self.ending = True
            args.remove("--ending")

        if len(args) == 0:
            self.interactive()

        for file in args:
            with open(file, "r") as f:
                for line in f.readlines():
                    self.display(line.strip("\n"))
                    self.n += 1


    def interactive(self):
        try:
            while True:
                #print("Entering interactive mode. Type your input (Ctrl+C to exit):")
                user = input()
                self.display(user)
                self.n += 1
        except KeyboardInterrupt:
            #print("\nExiting interactive mode.")
            exit(0)
        except EOFError:
            #print("\nExiting interactive mode.")
            exit(0)

    def display(self, line):
        print(f"{f'{self.n} ' if self.numbered else ''}{line}{'$' if self.ending else ''}")


def main():
    Catpy(sys.argv[1:])
    

if __name__ == '__main__':
    main()
