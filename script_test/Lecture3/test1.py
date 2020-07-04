from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('a')
parser.add_argument('-b', '--build')

#nargs says you must pass in this many arguments
#to this switch
parser.add_argument('-c', nargs=2)

args = parser.parse_args()