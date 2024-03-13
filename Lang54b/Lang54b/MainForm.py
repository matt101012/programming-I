import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Location = System.Drawing.Point(174, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(546, 128)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 449)
		self.Controls.Add(self._label1)
		self.Location = System.Drawing.Point(0, 17)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass