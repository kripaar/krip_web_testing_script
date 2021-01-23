# The requirements
from handler import app
from uvicorn import run

# The views you want to include to the page
import main
import ytdl

# The command to run the server
run(app, host="192.168.0.187", port=80)

