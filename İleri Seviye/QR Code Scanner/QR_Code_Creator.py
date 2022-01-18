# pip install pypng
# pip install pyqrcode

import pyqrcode

code = pyqrcode.create("https://www.subu.edu.tr/tr/ana-sayfa")
code.png("example_output.png",scale=9)
