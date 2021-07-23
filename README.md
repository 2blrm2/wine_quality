install the requirements
'''bash
pip install -r requirements.txt
'''

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"