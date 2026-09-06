
from data.module import new_module_db, get_module_db
from domains.module import Module

# ---- MODULE --------------------------------------------------------------------------------------------------------------------------------
def get_module(module_id) -> Module | None:
    module = get_module_db(module_id)
    if module is None:
        print("Das Module ist in der Datenbank nicht vorhanden.")
        return None

    module_id = module[0]
    module_name = module[1]
    module_etc = int(module[2])
    module = Module(module_id, module_name, module_etc)
    print(f" Das Module {module.name} wurde geladen.")
    return module


def create_new_module(module_id, module_name, module_etc) -> Module | None:
    try:
        new_module = Module(module_id, module_name, module_etc)
    except ValueError as e:
        print(f"Module konnte nicht anlegt werden: {e}")
        return None
    try:
        new_module_db(module_id, module_name, module_etc)
    except ValueError as e:
        print(f"Modul konnte nicht anlegt werden: {e}")
        return None
    print(f"Das Module {module_name} wurde anlegt.")
    return new_module