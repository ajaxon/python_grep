import sys
import getopt
import glob
import os


def main(argv):
   
   try:
      opts, args = getopt.getopt(argv, "vx")
   except getopt.GetoptError:
      print 'grep.py -x string filename'
      sys.exit(2)
   
   globbed = False

   
   if os.name == 'posix':
    
      files = args[1:]
      
    
   else:
      for filename in glob.glob(args[1]):
         files.append(filename)
   

   if len(files) > 1:
      globbed = True


   for filename in files:

      f = open(filename)
      if opts:
         for opt, arg in opts:
            ''' -x matches that exactly match the whole line '''
            if opt == '-x':
               for line in f:
                  ''' Loop through each line in file f '''
                  if line.strip() == args[0]:
                     if globbed:
                        print filename + ':' + line.strip()
                     else:
                        print line.strip()


            elif opt == '-v':

               for line in f:
                  ''' Loop through each line in the file f and print the line if the search string is not in it'''
                  if args[0] not in line:
                     if globbed:
                        print filename + ':' + line.strip()
                     else:
                        print line.strip()
      else:
         for line in f:
            if args[0] in line:
               if globbed:
                  print filename + ':' + line.strip()
               else:
                  print line.strip()

      f.close()


if __name__ == "__main__":
    main(sys.argv[1:])