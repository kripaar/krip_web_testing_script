from handler import app, render, FileResponse
from urllib.parse import unquote
from pytube import YouTube


@app.route("/ytdl")
async def ytdl():
    return render("ytdl.html")


@app.route("/ytdl", method="post")
async def home_post(request):
    link = unquote(request.POST.form["video-link"])
    yt = YouTube(link)
    video_name = yt.streams.get_highest_resolution().download("download")
    return FileResponse(open(video_name, "rb"), video_name.split("\\")[-1], as_attachment=True, delete_original_file_after_sending_out=True)
