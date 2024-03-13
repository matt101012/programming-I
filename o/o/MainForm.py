import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label1.Location = System.Drawing.Point(340, 33)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(245, 111)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Location = System.Drawing.Point(195, 243)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 68)
		self._button1.TabIndex = 0
		self._button1.Text = "Go Cougars!"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button2.Location = System.Drawing.Point(407, 243)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 68)
		self._button2.TabIndex = 2
		self._button2.Text = "Craig Rules"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button3.Location = System.Drawing.Point(627, 243)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 68)
		self._button3.TabIndex = 0
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(0, 0)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 23)
		self._button4.TabIndex = 0
		self._button4.Text = "button4"
		self._button4.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.White
		self.ClientSize = System.Drawing.Size(929, 433)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "o"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)

	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = "Go Cougars!"

	def Button2Click(self, sender, e):
		self._label.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

