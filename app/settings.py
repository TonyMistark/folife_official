import os
import os.path as osp
import sys


PYWEB_PATH = osp.dirname(osp.abspath(__file__))
PROJECT_PATH = osp.dirname(PYWEB_PATH)
sys.path.insert(0, PROJECT_PATH)

settings = dict(
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    template_path=os.path.join(os.path.dirname(__file__), "template"),
)