import importlib
import inspect


def load_model_class(identifier: str, prefix: str = "models."):
    module_path, class_name = identifier.split('@')

    # Import the module
    module = importlib.import_module(prefix + module_path) #动态导入模块
    cls = getattr(module, class_name) #从模块中获取类
    
    return cls


def get_model_source_path(identifier: str, prefix: str = "models."):
    module_path, class_name = identifier.split('@')

    module = importlib.import_module(prefix + module_path)
    return inspect.getsourcefile(module)
