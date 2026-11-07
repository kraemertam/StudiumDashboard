from data.base_repository import BaseRepository
from data.create_database import start_databank
from setup.import_initial_data import import_initial_data
from ui.app import App
from ui.login_view import LoginView

# "def main()" defines the Mainfunction with which the Project starts. ------------------------------------------------
def main():
    if not BaseRepository.DB_PATH.exists():
        start_databank()
        import_initial_data()
    
    app = App()
    app.show(LoginView)
    app.mainloop()

# Ensures that main() is only executed when the script starts directly and not during import.--------------------------
if __name__ == "__main__":
    main()