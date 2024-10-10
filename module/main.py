import importlib


def main():
    # this works.
    module = importlib.import_module("script_case1")
    print(module.foo())
    
    module = importlib.import_module("script_case2")
    print(module.foo())
    
    module = importlib.import_module("script_case_folder.script_folder")
    print(module.foo())
    
if __name__=="__main__":
    main()
