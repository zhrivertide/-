print(f" {__name__}的__init__.py被调用")
GLOBAL_PRAM = "S20243081876"

from Tool.hist import show_hist, get_hist
from Tool.display import show_img_plt, show_two_plt, show_img_cv

# 函数的可见性， 若没有则form import * 则什么也不能导入
__all__ = [
    'show_hist',

    ]
