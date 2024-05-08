from argparse import Namespace, ArgumentParser

from util import make_dir
from runner import runner

from mySeriesIds import us_macro_ids_D, us_macro_ids_W_wed, us_macro_ids_W_sat, us_macro_ids_M, us_macro_ids_Q
from mySeriesIds import us_macro_dir_D, us_macro_dir_W_wed, us_macro_dir_W_sat, us_macro_dir_M, us_macro_dir_Q

def setup_args() -> Namespace:
    parser = ArgumentParser(description='fred api')
    parser.add_argument('--freq', type=str)
    return parser.parse_args()

if __name__ == '__main__':
    args = setup_args()

    if args.freq == 'D':
        series_ids=us_macro_ids_D
        dir_name=us_macro_dir_D
    elif args.freq == 'W_wed':
        series_ids=us_macro_ids_W_wed
        dir_name=us_macro_dir_W_wed
    elif args.freq == 'W_sat':
        series_ids = us_macro_ids_W_sat
        dir_name = us_macro_dir_W_sat
    elif args.freq == 'M':
        series_ids=us_macro_ids_M
        dir_name=us_macro_dir_M
    elif args.freq == 'Q':
        series_ids=us_macro_ids_Q
        dir_name=us_macro_dir_Q
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