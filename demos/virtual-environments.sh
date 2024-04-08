# Venv
python3 -m venv venv
source venv/bin/activate
deactivate

# Pipenv, still wonky
pip3 install --user pipenv
pipenv install matplotlib
pipenv shell
exit