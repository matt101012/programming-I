import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(313, 45)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(259, 91)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._radioButton1.ForeColor = System.Drawing.SystemColors.ControlLight
		self._radioButton1.Location = System.Drawing.Point(179, 285)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Go Cougars!"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._radioButton2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._radioButton2.Location = System.Drawing.Point(397, 280)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(106, 33)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Clear"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._radioButton3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._radioButton3.Location = System.Drawing.Point(620, 278)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(95, 31)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Exit"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(891, 439)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Craig"
		self.ResumeLayout(False)

	def Label1Click(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		self._label1.Text = "Go Cougars"

	def RadioButton2CheckedChanged(self, sender, e):
			self._label1.Text = ""

	def RadioButton3CheckedChanged(self, sender, e):
		Application.Exit()