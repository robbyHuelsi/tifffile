# tifffile/tests/conftest.py

import os
import sys

if os.environ.get('VSCODE_CWD'):
    # work around pytest not using PYTHONPATH in VSCode
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    )

if os.environ.get('SKIP_CODECS', None):
    sys.modules['imagecodecs'] = None  # type: ignore


def pytest_report_header(config, start_path, startdir):
    try:
        from numpy import __version__ as numpy
        from tifffile import __version__ as tifffile
        from test_tifffile import config

        try:
            from imagecodecs import __version__ as imagecodecs
        except ImportError:
            imagecodecs = 'N/A'
        try:
            from zarr import __version__ as zarr
        except ImportError:
            zarr = 'N/A'
        try:
            from dask import __version__ as dask
        except ImportError:
            dask = 'N/A'
        try:
            from xarray import __version__ as xarray
        except ImportError:
            xarray = 'N/A'
        try:
            from fsspec import __version__ as fsspec
        except ImportError:
            fsspec = 'N/A'
        return (
            f'versions: tifffile-{tifffile}, '
            f'imagecodecs-{imagecodecs}, '
            f'numpy-{numpy}, '
            f'zarr-{zarr}, '
            f'dask-{dask}, '
            f'xarray-{xarray}, '
            f'fsspec-{fsspec}\n'
            f'test config: {config()}'
        )
    except Exception:
        pass


collect_ignore = ['_tmp', 'data', 'data-']
