from pathlib import Path

# Carpetas
list_of_folders = [
    "artifacts",
    "config",
    "custom_jenkins",
    "logs",
    "notebook",
    "pipeline",
    "src/logger",
    "src/exception",
    "static",
    "templates",
]

# Archivos
list_of_files = [
    # raíz
    ".gitignore",
    "Dockerfile",
    "Jenkinsfile",
    "requirements.txt",
    "README.md",

    # config
    "config/__init__.py",
    "config/config.yaml",
    "config/paths_config.py",

    # pipeline
    "pipeline/__init__.py",

    # notebook
    "notebook/notebook.ipynb",

    # src
    "src/__init__.py",
    "src/data_ingestion.py",
    "src/data_processing.py",
    "src/base_model.py",
    "src/model_training.py",

    # logger
    "src/logger/__init__.py",
    "src/logger/logger.py",

    # exception
    "src/exception/__init__.py",
    "src/exception/exception.py",

    # web
    "templates/index.html",
    "static/styles.css",

    # docker jenkins
    "custom_jenkins/Dockerfile",
]

def create_project_structure():
    print("🚀 Creando estructura del proyecto...")

    for folder in list_of_folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"📁 {folder}")

    for file in list_of_files:
        path = Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
        print(f"📄 {file}")

    print("✅ Proyecto creado correctamente")

if __name__ == "__main__":
    create_project_structure()