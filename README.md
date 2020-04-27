# fastapi-playground

Create and activate virtual env

```shell script
python3.7 -m venv venv 
pip install --upgrade pip
source venv/bin/activate
```

Install dependencies

```shell script
pip install -r requirements.txt
pip install -r requirements-test.txt
```

Run the dependency services

```shell script
docker-compose up -d
```

Run the app

```shell script
python -m api
```
