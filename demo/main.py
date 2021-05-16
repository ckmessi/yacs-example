
from project.config import get_cfg
from project.core import core

def parse_yacs_args():
    import argparse
    parser = argparse.ArgumentParser(description='args parser for yacs example.')
    parser.add_argument('--config-file', default='', help='')
    parser.add_argument('--argument1', default=1, help='')
    parser.add_argument(
        "opts",
        help="Modify config options using the command-line",
        default=None,
        nargs=argparse.REMAINDER,
    )
    args = parser.parse_args()
    return args

def setup(args):
    """
    Create configs and perform basic setups.
    """
    cfg = get_cfg()
    cfg.merge_from_file(args.config_file)
    cfg.merge_from_list(args.opts)
    cfg.freeze()
    # TODO: other setup operations
    return cfg


if __name__ == "__main__":

    args = parse_yacs_args()
    print("Command Line Args:", args)
    cfg = setup(args)
    core.function_1(cfg)
    