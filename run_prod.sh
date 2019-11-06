source .env/bin/activate
pip -r requirements.txt
cd src/
nohup python bot.py > ../bot.log 2>&1 & 