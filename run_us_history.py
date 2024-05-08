from argparse import Namespace, ArgumentParser

from util import make_dir
from runner import runner

from mySeriesIds import us_history_ids_Q, us_history_ids_M, us_history_ids_W,  us_history_ids_D
from mySeriesIds import us_history_dir_Q, us_history_dir_M, us_history_dir_W,  us_history_dir_D

def setup_args() -> Namespace:
    parser = ArgumentParser(description='fred api')
    parser.add_argument('--freq', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = setup_args()

    if args.freq == 'D':
        series_ids=us_history_ids_D
        dir_name=us_history_dir_D
    elif args.freq == 'W':
        series_ids=us_history_ids_W
        dir_name=us_history_dir_W
    # elif args.freq == 'W_m':
    #     series_ids = fed_bs_ids_W_mon
    #     dir_name = fed_bs_dir_W_mon
    elif args.freq == 'M':
        series_ids=us_history_ids_M
        dir_name=us_history_dir_M
    else:
        series_ids=us_history_ids_Q
        dir_name=us_history_dir_Q

    output_dir = './output'
    make_dir(output_dir)

    save_dir = '{}/{}'.format(output_dir, dir_name)
    make_dir(save_dir)

    runner(series_ids=series_ids, save_dir=save_dir, file_name=dir_name)