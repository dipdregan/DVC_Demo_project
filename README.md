### Creating new env and activation env
```bash
conda create -p env python=3.8 -y 
conda activate env/
```

### Creating New Env
```bash
pip install requirements.txt
```

### Initilizing Git and changing the branch
```bash
git init
git branch -M main
```

### Initilizing DVC
```bash
dvc init
```

### adding the data "we want to track the data"
```bash
dvc add "path the data set"
        my case
dvc add data_given/winequality.csv
```
