import sys
import os

# This adds the parent directory (mpesa_accounting) to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
