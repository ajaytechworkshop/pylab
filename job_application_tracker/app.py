from flask import Flask, Response
from pathlib import Path
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_applications():
    file_path:Path = Path("/Users/grosglockner/Dropbox/Job_Applications/applicartions.md")
    
    content:str = file_path.read_text(encoding="utf-8")
    response = markdown.markdown(content)

    return Response(response=response, mimetype="text/html")

if __name__ == "__main__":
    app.run