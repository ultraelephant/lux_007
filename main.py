"""File server solution."""

import argparse

import config
import filesvc
import logging
import utils


def main():
    """Main handler."""
    logging.basicConfig(level=logging.DEBUG)
    root = config.basepath
    pars = argparse.ArgumentParser()
    pars.add_argument('nargs', nargs='*', default=None, help=argparse.SUPPRESS)
    args = pars.parse_args()
    args = vars(args)

    if len(args['nargs']) == 2:
        if args['nargs'][0] == 'create':
            try:
                args['nargs'][1] = int(args['nargs'][1])
            except Exception as e:
                logging.error('File name lengh not integer:\n{}'.format(e))
            else:
                try:
                    filesvc.createfile(root + utils.genname(args['nargs'][1]))
                except Exception as e:
                    logging.error(e)

        elif args['nargs'][0] == 'delete':
            try:
                filesvc.deletefile(root + args['nargs'][1])
            except Exception as e:
                logging.error(e)

        elif args['nargs'][0] == 'read':
            try:
                print(filesvc.readfile(root + args['nargs'][1]))
            except Exception as e:
                logging.error(e)

        elif args['nargs'][0] == 'getmeta':
            try:
                print(filesvc.getfilemeta(root + args['nargs'][1]))
            except Exception as e:
                logging.error(e)

        else:
            print("unknow command")


if __name__ == "__main__":
    main()
