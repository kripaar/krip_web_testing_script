# The application, the center of everything.
from kripweb.app import App
app = App()

# The responses, the things server send to clients.
from kripweb.response import ImageResponse, FileResponse, HTMLResponse
ImageResponse = ImageResponse()
FileResponse = FileResponse()
HTMLResponse = HTMLResponse()


# The shortcuts, the faster way to write the code.
from kripweb.shortcut import Render
render = Render(app, HTMLResponse)


