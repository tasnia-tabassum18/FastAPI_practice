<h1>Setup</h1>
<h3>Set up your virtual environment</h3>

<p>python -m venv env</p>
<p>.\env\Scripts\activate</p>
<p>pip install -r requirements.txt</p>
<p>If you're running Linux or MacOS you'll instead run:</p>
<p>python -m venv env</p>
<p>source ./env/bin/activate</p>
<p>pip install -r requirements.txt</p>
<br>
<h3>Running the app</h3>
uvicorn main:app --reload
