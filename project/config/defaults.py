from .cfg_node import CfgNode as CN

_C = CN()


_C.FIX_SEED = 19


_C.LEVEL1 = CN()
_C.LEVEL1.V1 = False
_C.LEVEL1.V2 = 3.0

_C.LEVEL1.LEVEL2 = CN()
_C.LEVEL1.LEVEL2.A = 0.1
_C.LEVEL1.LEVEL2.B = 0.2
_C.LEVEL1.LEVEL2.C = 0.3


_C.OUTPUT_DIR = "logs/"


