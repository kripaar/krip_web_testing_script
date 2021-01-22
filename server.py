# The requirements
from handler import app
from uvicorn import run

# The optional views
import main

# The command to run the server
run(app, host="192.168.0.187", port=80)

