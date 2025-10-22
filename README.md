




Get Going!
Check version of Python
Check what version of Python you have. The Makefile uses PYTHON=python as default.

# Check you Python installation
make version

Python virtual environment
Install a Python virtual environment and activate it.

# Create the virtual environment
make venv

# Activate on Windows
. .venv/Scripts/activate

# Activate on Linx/Mac
. .venv/bin/activate


When you are done you can leave the venv using the command deactivate.


The project uses Sphinx for generating automic documentation from docstrings in the code.

🔹To create a HMTL documentation use the command:
🔹Make first sure you have sphinx installed, if not use the command:

<< pip install sphinx>> All the dependencies are in requirements.txt. You can install them with:
pip install -r requirements.txt

🔹To see the documentation, use the command: 
make doc 

This command runs sphinx-build to generate dokumentation to the catalog:
<< doc/api/build/html >>

🔹To open the documentation open the file:
doc/api/build/html/index.html - make sure to click on the
go live button go see the documentation in your web browser-



## 🧪 Run Tests and Coverage
🔹To run all tests:
```bash
python -m unittest discover -s tests

🔹To measure code coverage:
coverage run -m unittest discover -s tests
coverage report -m

🔹To generate an HTML report:
Coverage HTML

🔹Open the report in your browser:

start htmlcov/index.html #For Windows
open htmlcov/index.html #For macOS


