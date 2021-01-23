from handler import app, render, ImageResponse


@app.route("/")
async def home():
    return render("home.html")


@app.route("/favicon.ico")
async def favicon():
    return ImageResponse(open("static/logo.png", "rb").read())
