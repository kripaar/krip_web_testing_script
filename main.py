from handler import app, render, ImageResponse, TextResponse, FileResponse
from urllib.parse import unquote
from pytube import YouTube
import asyncio
import os


@app.route("/")
async def home():
    return render("ytdl.html")


@app.route("/", method="post")
async def home_post(request):
    link = unquote(request.POST.form["video-link"])
    yt = YouTube(link)
    video_name = yt.streams.get_highest_resolution().download("download")
    return FileResponse(open(video_name, "rb"), video_name.split("\\")[-1], delete_file_afterwards=True)


@app.route("/favicon.ico")
async def favicon():
    return ImageResponse(open("static/logo.png", "rb").read())
