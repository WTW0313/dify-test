import platform
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint


class DifyTestEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        def generator():
            yield f"{platform.system()} <br>"
            yield f"{platform.processor()} <br>"
            yield f"{platform.version()} <br>"
            yield f"{platform.platform()} <br>"

        return Response(generator(), status=200, content_type="text/html")
