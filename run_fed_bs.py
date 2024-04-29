from argparse import Namespace, ArgumentParser

from util import make_dir
from runner import runner

from mySeriesIds import fed_bs_ids_D, fed_bs_ids_W_wed, fed_bs_ids_W_mon, fed_bs_ids_M, fed_bs_ids_Q
from mySeriesIds import fed_bs_dir_D, fed_bs_dir_W_wed, fed_bs_dir_W_mon, fed_bs_dir_M, fed_bs_dir_Q

def setup_args() -> Namespace:
    parser = ArgumentParser(description='fred api')
    parser.add_argument('--freq', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = setup_args()

    if args.freq == 'D':
        series_ids=fed_bs_ids_D
        dir_name=fed_bs_dir_D
    elif args.freq == 'W_w':
        series_ids=fed_bs_ids_W_wed
        dir_name=fed_bs_dir_W_wed
    elif args.freq == 'W_m':
        series_ids = fed_bs_ids_W_mon
        dir_name = fed_bs_dir_W_mon
    elif args.freq == 'M':
        series_ids=fed_bs_ids_M
        dir_name=fed_bs_dir_M
    else:
        series_ids=fed_bs_ids_Q
        dir_name=fed_bs_dir_Q

    output_dir = './output'
    make_dir(output_dir)

    save_dir = '{}/{}'.format(output_dir, dir_name)
    make_dir(save_dir)

    runner(series_ids=series_ids, save_dir=save_dir, file_name=dir_name)