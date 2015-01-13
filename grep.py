import sys
import getopt
import glob
import os

displayFileName = False


def print_grep(line, filename):
    if displayFileName:
        print filename + ':' + line.strip()
    else:
        print line.strip()


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "vx")
    except getopt.GetoptError:
        print 'grep.py -x string filename'
        sys.exit(2)

    # check os to determine method for file globbing
    if os.name == 'posix':

        files = args[1:]
    # not posix will require the use of glob module
    else:
        for filename in glob.glob(args[1]):
            files.append(filename)

    # If more than 1 file has been found then display filename in output
    if len(files) > 1:
        global displayFileName
        displayFileName = True

    for filename in files:
        ''' For each file in files the file is opened and checked according to opts'''
        try:
            f = open(filename)
        except IOError:
            print "File :" + filename + " not found"
            continue

        if opts:
            for opt, arg in opts:
                ''' Loop through each opt '''

                # -x displays results that match the whole line
                if opt == '-x':
                    for line in f:
                        ''' Loop through each line in file f '''
                        if line.strip() == args[0]:
                            print_grep(line, filename)

                # -v prints lines that do not contain the search string
                elif opt == '-v':

                    for line in f:
                        ''' Loop through each line in the file f and print the line if the search string is not in it'''
                        if args[0] not in line:
                            print_grep(line, filename)
        # if no opts
        else:
            for line in f:
                ''' Loop through each line in the file and see if search string is in the line'''
                if args[0] in line:
                    print_grep(line, filename)

        f.close()


if __name__ == "__main__":
    main(sys.argv[1:])