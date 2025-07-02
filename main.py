from fastapi import FastAPI, Form, Request  # permet de lire les données d’un formulaire HTML (<form>) envoyé en POST
from fastapi.templating import Jinja2Templates  # moteur de template
from fastapi.responses import HTMLResponse #La réponse que je renvoie à cette route est une page HTML, pas du JSON
from add import add  # ma logique métier dans mon autre fichier

app = FastAPI()  # Crée une instance de l'application FastAPI, appelée app
templates = Jinja2Templates(
    directory="templates"
)  # Tous mes fichiers HTML sont dans le dossier templates/


@app.post("/calculator/add", response_class=HTMLResponse) # précise l'url et que j'utilise du HTML
def add_api( request: Request, val1: int = Form(...), val2: int = Form(...)):  # request: Request > Requis par FastAPI/Jinja2 pour afficher un template
    
    result = add(val1, val2)

    return templates.TemplateResponse("add.html", {
            "request": request, #l’objet de requête FastAPI (obligatoire)
            "resultat": result} #la valeur retournée par la logique métier
    )


@app.get("/calculator", response_class=HTMLResponse) #display the calculator 
def calculator_api (request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@app.get("/", response_class=HTMLResponse) #display the homepage 
def root_api(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})