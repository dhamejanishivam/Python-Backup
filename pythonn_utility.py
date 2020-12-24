import argparse
import sys


def calc(args):
    if args.o=='add':
        return args.x + args.y
    if args.o=='mul':
        return args.x * args.y
    if args.o=='div':
        return args.x / args.y
    if args.o=='sub':
        return args.x - args.y

    else: return ("Eror")
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x' , type=float , default=0 ,
                        help="1")
    parser.add_argument('--y' , type=float , default=0 ,
                        help="2")
    parser.add_argument('--o' , type=str , default="add" ,
                        help="3")


    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))