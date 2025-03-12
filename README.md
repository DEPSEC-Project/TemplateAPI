# DEPSEC-TemplateAPI
Template d'API flask qui correspond à l'architecture d'APIs définie pour l'ensemple du projet DEPSEC

## Comment s'en servir ? 
Tout d'abord, un dépot template sert de modèle à un nouveau template, dans les faits, un nouveau template copiera l'ensemble du modèle, sans conserver l'historique git du dépot, à l'inverse d'un fork, pour ce faire en premier lieu :
![image](https://github.com/user-attachments/assets/ba4ed3c8-360a-4582-8e36-26ebc39f6748)
<br></br>
Il faut ensuite choisir le nom de votre nouveau repo,  copier les branches de la template puis créer le dépot.
![image](https://github.com/user-attachments/assets/f8d44895-9f8a-40ce-b4fa-72e30ad0b8bf)

Vous aurez ensuite votre nouveau dépot reprenant tout l'ensemble de l'ancien dépot. 

Il restera à modifier encore : 
- Fichier README.md avec les informations relatives à votre API
- Fichier DOCKERFILE de configuration de l'image docker
- Fichier app/__ init__.py :
  ```python
  from app.routes.fichier.py import <nom_blueprint>
  app.register_blueprint(<nom _blueprint>, url_prefix='/route1')
  app.register_blueprint<nom _blueprint>, url_prefix='/route2')
  ```
- fichiers app/routes/*, définir les endpoints associés aux blueprints ainsi que les méthodes et chemins associés:
  ```python
  <nom_blueprint> = Blueprint("<nom>", __name__) # exemple de nom : users / auth
  @<nom_blueprint>.route('/tutu', methods=['POST'])
  @limiter.limit("5 per minute") #comme on veut
  def <nom_fonction>():
    data = request.json
    #implémentation de la fonction etc
    return jsonify({"msg": ""}), 401
  #autant d'endpoints qu'on veut...
  ```
- Fichier requirements.txt dans le cas où vous utilisez des bibliothèques supplémentaires
