import sys
from ui import ClientAppUI
from client import ChatNoirClient

def main():
    app = ClientAppUI(sys.argv, ChatNoirClient())
    app.show_ui()
    sys.exit(app.execute())

if __name__ == "__main__":
    main()
