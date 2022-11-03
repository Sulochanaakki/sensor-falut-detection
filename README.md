# sensor-falut-detection
Identifying  air pressure system is a critical component of a heavy-duty vehicle that uses compressed air to force a position to provide pressure to the brake pads, slowing the vehicle down. The benifits of using an APS instead of a hydralic system are the easy availability and long term sustainability of natture air.

To create virtual environment
```
conda create -n sensor python=3.8 -y
```
To activate virtual environment
```
conda activate sensor
```
To Install the requirements
```
pip install -r requirements.txt

pip freeze > requirements.txt(If you are using virtual env)
```

###  Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```

###  Run the application server
```bash
python app.py
```

To run setup.py file
```
python setup.py install
