mkdir -p data
cd data
curl -LO https://datahub.io/machine-learning/credit-g/r/credit-g.json
cd ..
apt install python3-venv 
python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt  
