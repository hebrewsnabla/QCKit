from yapf.yapflib.yapf_api import FormatFile
import sys

file = sys.argv[1]
FormatFile(file, in_place=True)
