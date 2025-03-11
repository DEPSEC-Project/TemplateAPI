from app import create_app # import de la fonction create_app du fichier app/__init__.py
from app.extensions import db, migrate # import des extensi
from DEPSECModels import *

app = create_app()

if __name__ == "__main__": #lancement de l'app si on execute le script python
    app.run(debug=True)
