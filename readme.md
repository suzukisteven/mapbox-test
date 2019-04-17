1. You have to create a DB called Trip, where the columns should include: latitude(decimalfield), longitude(decimalfield), address(charfield) and youll need user_id(foreignkeyfield) later.

2. Make environment 
```PYTHON
conda create -n project_name python=3.7
```
<br>

3. install all dependencies
```PYTHON
pip install -r requirements.txt
```
<br>

4. add your mapbox api key to .env file
5. change DATABASE_URL to match your db in .env file
