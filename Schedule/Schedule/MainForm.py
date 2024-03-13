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
		self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(15, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(295, 417)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(340, 139)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(120, 46)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Show"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(466, 139)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(120, 46)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Clear"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(592, 139)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(120, 46)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Exit"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(814, 449)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Schedule"
		self.ResumeLayout(False)



	def Label1Click(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		self._label1.Text = "1st Freshman Seminar \n 2nd Algebra \n 3rd Computer Programming \n 4th Global Studies \n 5th Automotive Systems \n 6th Biology \n 7th English \n 8th Art 1 B"

	def RadioButton2CheckedChanged(self, sender, e):
		self._label1.Text = ""

	def RadioButton3CheckedChanged(self, sender, e):
		Application.Exit()