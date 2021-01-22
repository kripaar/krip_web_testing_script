# The application, the center of everything.
from kripweb.app import App
app = App()

# The responses, the things server send to clients.
from kripweb.response import Response
TextResponse = Response(b"text/plain")
ImageResponse = Response(b"image/jpg", encode=False)
HTMLResponse = Response(b"text/html")

import asyncio
def FileResponse(file, filename, delete_file_afterwards=False):
    if delete_file_afterwards:
        async def remove_downloaded_file(filename):
            while True:
                await asyncio.sleep(10)
                try:
                    os.remove(filename)
                except:
                    pass
                else:
                    break
        asyncio.get_running_loop().create_task(remove_downloaded_file(file.name))
    return Response(b"application/octet-stream", {b"Content-Disposition": b"attachment; filename={filename}"}, encode=False)(file.read(), {b"Content-Disposition": {"filename": filename}})




# The shortcuts, the faster way to write the code.
from kripweb.shortcut import Render
render = Render(app, HTMLResponse)


