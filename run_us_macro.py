from argparse import Namespace, ArgumentParser

from util import make_dir
from runner import runner

from mySeriesIds.us_macro import dir, ids_Q, ids_M, ids_W_wed, ids_W_sat, ids_D


def setup_args() -> Namespace:
    parser = ArgumentParser(description='fred api')
    parser.add_argument('--freq', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = setup_args()

    if args.freq == 'D':
        series_ids=ids_D
    elif args.freq == 'W_wed':
        series_ids=ids_W_wed
    elif args.freq == 'W_sat':
        series_ids=ids_W_sat
    elif args.freq == 'M':
        series_ids=ids_M
    elif args.freq == 'Q':
        series_ids=ids_Q
    else:
        print('')
        print('There is NO VALID term unit!')
        print('')
        exit()

    dir_name = '{}({})'.format(dir, args.freq)

    output_dir = './output'
    make_dir(output_dir)

    type_dir = '{}/{}'.format(output_dir, dir)
    make_dir(type_dir)

    save_dir = '{}/{}'.format(type_dir, dir_name)
    make_dir(save_dir)

    runner(series_ids=series_ids, save_dir=save_dir, file_name=dir_name)