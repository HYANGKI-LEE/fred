from argparse import Namespace, ArgumentParser

from util import make_dir
from runner import runner

from mySeriesIds.us_liquidity import dir, ids_D, ids_W_wed, ids_W_mon, ids_M, ids_Q

def setup_args() -> Namespace:
    parser = ArgumentParser(description='fred api')
    parser.add_argument('--freq', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = setup_args()

    if args.freq == 'D':
        series_ids=ids_D
    elif args.freq == 'W_w':
        series_ids=ids_W_wed
    elif args.freq == 'W_m':
        series_ids=ids_W_mon
    elif args.freq == 'M':
        series_ids=ids_M
    elif args.freq == 'Q':
        series_ids=ids_Q
    else:
        print('')
        print('There is NO VALID term unit!')
        print('')
        exit()

    output_dir = './output'
    make_dir(output_dir)

    save_dir = '{}/{}'.format(output_dir, dir_name)
    make_dir(save_dir)

    runner(series_ids=series_ids, save_dir=save_dir, file_name=dir_name)