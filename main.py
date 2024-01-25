from flask import Flask, request, jsonify
from flask_cors import CORS
from tinydb import TinyDB, Query


db = TinyDB("db.json")
projects = db.table("projects")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api/createProject", methods=["POST"])
def createProject():
    data = request.json
    # check if project already exists
    project = Query()
    if projects.search(project.projectname == data["projectName"]):
        return jsonify({"error": "Project already exists"})
    projects.insert(data)
    return jsonify(data)


@app.route("/api/getProjects", methods=["GET"])
def getProjects():
    return jsonify(projects.all())


@app.route("/api/getProject", methods=["GET"])
def getProject():
    project = Query()
    return jsonify(projects.search(project.projectName == request.args.get("name"))[0])


@app.route("/api/saveSelected", methods=["POST"])
def saveSelected():
    project = Query()
    projects.update(
        {"selected": request.json["likedImages"]},
        project.projectName == request.json["name"],
    )
    return jsonify({"success": True})


@app.route("/api/deleteProject", methods=["POST"])
def deleteProject():
    projectName = request.json["projectName"]
    print(projectName)
    project = Query()
    projects.remove(project.projectName == projectName)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")
