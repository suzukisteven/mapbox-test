# How 2 use dis
<hr>

1. Create a table in your DB such as Trip (make model -> migrate), where the columns (attributes) should include: latitude(decimalfield), longitude(decimalfield), address(charfield) and youll need user_id(foreignkeyfield) eventually.

2. Create environment if its a new project. Otherwise use an existing one.
```PYTHON
conda create -n project_name python=3.7
```
<br>

3. Install all dependencies from requirements.txt
```PYTHON
pip install -r requirements.txt
```
<br>

4. Add your mapbox api key to .env file
5. Change DATABASE_URL to match your database name in your .env file

### Refer to __init__.py (controller), and map.html (template)
