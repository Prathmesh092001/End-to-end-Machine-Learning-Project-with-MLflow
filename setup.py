import setuptools

import os

# Get the current directory
current_directory = os.path.abspath(os.path.dirname(__file__))

# Define the path to your README.md file
readme_path = os.path.join(current_directory, 'README.md')

# Open and read the content of the README.md file
#with open(readme_path, 'r', encoding='utf-8') as readme_file:
#    readme_content = readme_file.read()

# Now you can work with the content of the README.md file
#print(readme_content)



with open(readme_path, "r", encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__= "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "HAMBARDE PRATHMESH EKNATH"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "prathmeshhambarde1@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for ML app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)