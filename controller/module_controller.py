from data.module_repository import ModuleRepository
from domains.module import Module

# ---- MODULE --------------------------------------------------------------------------------------------------------------------------------
class ModuleController:
    def __init__(self):
        self.module_repository = ModuleRepository()

    def add_module_to_course(self, course_id: str, module_id: str) -> Module | None:
        try:
            new_module = Module(module_id, module_name, int(module_ects))
        except ValueError as e:
            print(f"Module konnte nicht anlegt werden: {e}")
            raise
        try:
            self.module_repository.create(module_id, module_name, int(module_ects))
        except ValueError as e:
            print(f"Modul konnte nicht anlegt werden: {e}")
            raise
        print(f"Das Module {module_name} wurde anlegt.")
        return new_module
    
    def get_module(self, module_id) -> Module | None:
        module = self.module_repository.get_by_id(module_id)
        if module is None:
            print("Das Module ist in der Datenbank nicht vorhanden.")
            return None

        module_id = module[0]
        module_name = module[1]
        module_ects = int(module[2])
        module = Module(module_id, module_name, module_ects)
        print(f" Das Module {module.name} wurde geladen.")
        return module