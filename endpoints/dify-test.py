import time
from typing import Mapping
from werkzeug import Request, Response
from flask import render_template_string
from dify_plugin import Endpoint

class DifyTestEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        ascii_art = '''
            ⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛⬛️⬜️⬜️⬜️⬜️⬜⬜️⬜️️
            🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟥🟥🟥🟥🟥🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️⬜️⬜️⬜️⬜️⬜⬜️️
            🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧🥧💟💟💟💟💟💟💟💟💟💟💟💟💟🥧🥧🥧⬛️⬜️⬜️⬜️⬜⬜️️
            🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥⬛️🥧🥧💟💟💟💟💟💟🍓💟💟🍓💟💟💟💟💟🥧🥧⬛️⬜️⬜️⬜️⬜️⬜️️
            🟧🟧🟥🟥🟥🟥🟥🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧🟧🟥🟥🟥🟥🟥🟥🟥⬛🥧💟💟🍓💟💟💟💟💟💟💟💟💟💟💟💟💟💟🥧⬛️⬜️⬜️⬜️⬜⬜️️
            🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟💟⬛️⬛️💟💟🍓💟💟🥧⬛️⬜️⬛️️⬛️️⬜⬜️️
            🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫⬛💟💟💟💟🥧⬛️⬛️🌫🌫⬛⬜️️
            🟨🟨🟧🟧🟧🟧🟧🟧🟧🟧🟨🟨🟨🟨🟨🟨🟨🟨🟧⬛️⬛️⬛️⬛️🟧🟧⬛️🥧💟💟💟💟💟💟🍓💟💟⬛️🌫🌫🌫⬛💟💟💟🥧⬛️🌫🌫🌫⬛⬜️️
            🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️🌫🌫⬛️⬛️🟧⬛️🥧💟💟💟💟💟💟💟💟💟⬛️🌫🌫🌫🌫⬛️⬛️⬛️⬛️🌫🌫🌫🌫⬛⬜️️
            🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛️⬛️🌫🌫⬛️⬛️⬛️🥧💟💟💟🍓💟💟💟💟💟⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛⬜️️
            🟩🟩🟨🟨🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩🟩🟨🟨⬛⬛️🌫🌫⬛️⬛️🥧💟💟💟💟💟💟💟🍓⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️
            🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️🌫🌫⬛️🥧💟🍓💟💟💟💟💟💟⬛️🌫🌫🌫⬜️⬛️🌫🌫🌫🌫🌫⬜️⬛️🌫🌫⬛️
            ️🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩⬛️⬛️⬛️⬛️🥧💟💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️🌫🌫🌫⬛️🌫⬛️⬛️🌫🌫⬛️
            🟦🟦🟩🟩🟩🟩🟩🟩🟩🟩🟦🟦🟦🟦🟦🟦🟦🟦🟩🟩🟩🟩🟩🟩⬛️⬛️🥧💟💟💟💟💟🍓💟💟⬛🌫🟥🟥🌫🌫🌫🌫🌫🌫🌫🌫🌫🟥🟥⬛️
            🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧💟🍓💟💟💟💟💟⬛️🌫🟥🟥🌫⬛️🌫🌫⬛️🌫🌫⬛️🌫🟥🟥⬛️
            🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛️🥧🥧🥧💟💟💟💟💟💟💟⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️🌫🌫⬛️⬜️
            🟪🟪🟦🟦🟦🟦🟦🟦🟦🟦🟪🟪🟪🟪🟪🟪🟪🟪🟦🟦🟦🟦🟦🟦⬛️⬛️⬛️🥧🥧🥧🥧🥧🥧🥧🥧🥧🥧⬛️🌫🌫🌫🌫🌫🌫🌫🌫🌫🌫⬛️⬜️⬜️
            🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫🌫⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️
            🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪⬛️🌫🌫⬛️⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️⬜️⬛️🌫🌫⬛️⬜️⬛️🌫🌫⬛️⬜️⬜️⬜️⬜️
            ⬜️⬜️🟪🟪🟪🟪🟪🟪🟪🟪⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️🟪🟪🟪🟪🟪⬛️⬛️⬛️⬛⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬜️️
        '''

        ascii_art_lines = ascii_art.strip().split('\n')

        return Response(render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            background-color: black;
            color: white;
            overflow: hidden;
            margin: 0;
            padding: 0;
        }
        #ascii-art {
            font-family: monospace;
            white-space: pre;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            display: inline-block;
            font-size: 16px;
            line-height: 1;
        }
    </style>
</head>
<body>
    <div id="ascii-art"></div>
    <script>
        var asciiArtLines = {{ ascii_art_lines | tojson }};
        var asciiArtDiv = document.getElementById("ascii-art");
        var index = 0;

        function displayNextLine() {
            if (index < asciiArtLines.length) {
                var line = asciiArtLines[index];
                var lineElement = document.createElement("div");
                lineElement.innerHTML = line;
                asciiArtDiv.appendChild(lineElement);
                index++;
                setTimeout(displayNextLine, 100);
            } else {
                animateCat();
            }
        }

        function animateCat() {
            var pos = 0;
            var screenWidth = window.innerWidth;
            var catWidth = asciiArtDiv.offsetWidth;
            function move() {
                asciiArtDiv.style.left = pos + "px";
                pos += 2;
                if (pos > screenWidth) {
                    pos = -catWidth;
                }
                requestAnimationFrame(move);
            }
            move();
        }

        displayNextLine();
    </script>
</body>
</html>
    ''', ascii_art_lines=ascii_art_lines), status=200, content_type="text/html")