# Mainprogramm --------------------------------------------------------------------------------------------------------
from ui.app import App
from ui.login_view import LoginView

# "def main()" defines the Mainfunction with which the Project starts. ------------------------------------------------
def main():
    app = App()
    app.show(LoginView)
    app.mainloop()

# Ensures that main() is only executed when the script starts directly and not during import.--------------------------
if __name__ == "__main__":
    main()