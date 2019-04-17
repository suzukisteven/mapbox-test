1. Create a table in your DB such as Trip (and the model), where the columns (attributes) should include: latitude(decimalfield), longitude(decimalfield), address(charfield) and youll need user_id(foreignkeyfield) eventually.

2. Make environment 
```PYTHON
conda create -n project_name python=3.7
```
<br>

3. install all dependencies from requirements.txt
```PYTHON
pip install -r requirements.txt
```
<br>

4. add your mapbox api key to .env file
5. change DATABASE_URL to match your db in .env file
