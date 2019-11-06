source .env/bin/activate
pip install -r requirements.txt
cd src/
nohup python bot.py > ../bot.log 2>&1 & 