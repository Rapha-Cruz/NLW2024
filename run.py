from src.main.server.server import app
#importar o gerente de conexoes
from src.models.settings.db_connection_handler import db_connection_handler

if __name__ == "__main__":
    db_connection_handler.connect()
    app.run(host="localhost", port=3000, debug=True)
