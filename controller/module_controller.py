from data.module_repository import ModuleRepository
from domains.module import Module


class ModuleController:
    """Coordinates loading and creating modules."""
    def __init__(self):
        self.module_repository = ModuleRepository()

    def create_new_module(self, module_id, module_name, module_ects) -> Module | None:
        """Create a new module: validate via the domain class, then save in the database."""
        try:
            new_module = Module(module_id, module_name, int(module_ects))
        except ValueError as e:
            print(f"Modul konnte nicht angelegt werden: {e}")
            raise
        try:
            self.module_repository.create(module_id, module_name, int(module_ects))
        except ValueError as e:
            print(f"Modul konnte nicht angelegt werden: {e}")
            raise
        return new_module
    
    def get_module(self, module_id) -> Module | None:
        """Load a module. Returns None if it does not exist."""
        module = self.module_repository.get_by_id(module_id)
        if module is None:
            print("Das Modul ist in der Datenbank nicht vorhanden.")
            return None

        module_id = module[0]
        module_name = module[1]
        module_ects = int(module[2])
        module = Module(module_id, module_name, module_ects)
        return module