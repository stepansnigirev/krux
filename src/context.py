# The MIT License (MIT)

# Copyright (c) 2021 Tom J. Sun

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import gc
from display import Display
from input import Input
from camera import Camera
from light import Light
from printer import Printer
import settings

class Context:
	def __init__(self):
		self.version = open('/sd/VERSION').read().strip()
		self.net = settings.load('network', 'main')
		self.display = Display()
		self.input = Input()
		self.camera = Camera()
		self.light = Light()
		self.printer = Printer(
	  		int(settings.load('printer.baudrate', '9600')),
			int(settings.load('printer.paper_width', '384'))
		)
		self.wallet = None
		self.multisig_policy = None
  
	def clear(self):
		self.wallet = None
		self.multisig_policy = None
		self.printer.clear()
		gc.collect()