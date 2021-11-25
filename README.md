# Yacs Example

An example to demonstrate how to organize experimental code using `yacs` package.

## Basic Structure
When integrating `yacs`, the only things to do is:
- Inherit `CfgNode` class and define some custom logics;
- Define default values about the configuration;
- Do little modification when parsing the arguments from command line;
- Setup `cfg` variable at the begining of the program.


## Usage

When using `yacs` as the strategy to control experimental configs, values of configuration can be defined in defaults, config file or command augments.

```
$ PYTHONPATH=. python demo/main.py --config-file configs/sample.yml LEVEL1.LEVEL2.B 0.22
Command Line Args: Namespace(argument1=1, config_file='configs/sample.yml', opts=['LEVEL1.LEVEL2.B', '0.22'])
[FUNCTION_1] cfg content:
FIX_SEED: 19
LEVEL1:
  LEVEL2:
    A: 0.11
    B: 0.22
    C: 0.3
  V1: True
  V2: 3.0
OUTPUT_DIR: logs/sample/
```

Here we can analyze the cfg config content:
- `FIX_SEED` is defined in `project/config/defaults.py`, and it is not be overrided;
- `LEVEL1.V1` in `project/config/defaults.py` is `False`, but in `base.yml` it is overrided as `True`, and `sample.yml` inherits the value from `base.yml`;
- `LEVEL1.V2` is overrided by `base.yml` to `3.0` and overrided by `sample.yml` again, so it is `4.0` finally;
- `LEVEL1.LEVEL2.A` is overrided by `sample.yml` to `0.11`;
- `LEVEL1.LEVEL2.B` is overrided by command line argument to `0.22`;
- `LEVEL1.LEVEL2.C` is not overrided, so it is the default value `0.3`;

As the example shows, the configuration content can be easily controlled by config files or command line arguments.
Hope it will help to split and record the experimental configs.

## Reference
- https://github.com/rbgirshick/yacs
- https://github.com/facebookresearch/Detectron
- https://github.com/JDAI-CV/fast-reid
