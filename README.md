# fastapi-playground

Create and activate virtual env

```shell script
python3.7 -m venv venv 
source venv/bin/activate
pip install --upgrade pip
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
source env-dev.sh
python -m api
```
