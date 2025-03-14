if [ ! -d venv ]; then
  echo "installing venv"
  python3 -mvenv venv
else
  echo "env already exists"
fi

source venv/bin/activate

pip install -r requirements.txt