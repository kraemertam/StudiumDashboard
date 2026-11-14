from data.base_repository import BaseRepository
from data.create_database import start_databank
from setup.import_initial_data import import_initial_data
from ui.app import App
from ui.login_view import LoginView


def main():
    """Start the application. Creates database and sample data on first start."""
    if not BaseRepository.DB_PATH.exists():
        start_databank()
        import_initial_data()
    
    app = App()
    app.show(LoginView)
    app.mainloop()


if __name__ == "__main__":
    """Entry point of the StudiumDashboard application."""
    main()