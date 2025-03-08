import inspect
import os


def get_test_context_from_stack() -> (str, str):
    """
    Inspects the call stack to find:
      1) The folder name in which that test file resides.
      2) The first function name that starts with 'test_' (the test function).

    Returns:
      (folder_name, function_name)
    """
    frames = inspect.stack()
    for frame_info in frames:
        func_name = frame_info.function
        if func_name.startswith("test_"):
            # e.g. 'test_home_page' from /path/to/repo/tests/home/test_home_page.py
            filename = frame_info.filename
            # e.g. 'home' from '/path/to/repo/tests/home'
            folder_name = os.path.basename(os.path.dirname(filename))
            return folder_name, func_name

    return "", ""