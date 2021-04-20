import argparse

import config
import filesvc
import utils

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('nargs',nargs='*',default=None,help=argparse.SUPPRESS)
    args = parser.parse_args()
    args = vars(args)

    if len(args['nargs']) == 2:
        if args['nargs'][0] == 'create':
            try:
                args['nargs'][1] = int(args['nargs'][1])
            except:
                print ('File name lengh not integer')
            else:
                try:
                    filesvc.createfile(config.basepath + utils.genname(args['nargs'][1]))
                except Exception as e:
                    print (e)

        elif args['nargs'][0] == 'delete':
            try:
                filesvc.deletefile(config.basepath + args['nargs'][1])
            except Exception as e:
                print (e)

        elif args['nargs'][0] == 'read':
            try:
                print(filesvc.readfile(config.basepath + args['nargs'][1]))
            except Exception as e:
                print (e)

        elif args['nargs'][0] == 'getmeta':
            try:
                print(filesvc.getfilemeta(config.basepath + args['nargs'][1]))
            except Exception as e:
                print (e)

if __name__ == "__main__":
    main()