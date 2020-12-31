__version__ = '0.9.0.dev20201210'
git_version = 'e337103f2c222528f505772f1289dfee06117de4'
from torchvision.extension import _check_cuda_version
if _check_cuda_version() > 0:
    cuda = _check_cuda_version()
