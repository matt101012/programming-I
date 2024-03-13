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
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(379, 46)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(156, 102)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton1.Location = System.Drawing.Point(88, 296)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Taco Bell"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton2.Location = System.Drawing.Point(244, 296)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "McDonald's"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton3.Location = System.Drawing.Point(411, 296)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Culver's"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton4.Location = System.Drawing.Point(587, 296)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 4
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Wendy's"
		self._radioButton4.UseVisualStyleBackColor = False
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton5.Location = System.Drawing.Point(750, 296)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(104, 24)
		self._radioButton5.TabIndex = 5
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "Denny's"
		self._radioButton5.UseVisualStyleBackColor = False
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._radioButton6.Location = System.Drawing.Point(411, 390)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 6
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "Exit"
		self._radioButton6.UseVisualStyleBackColor = False
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(949, 449)
		self.Controls.Add(self._radioButton6)
		self.Controls.Add(self._radioButton5)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "phone numbers"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def RadioButton1CheckedChanged(self, sender, e):
		self._label1.Text = "608 563-4114"

	def RadioButton2CheckedChanged(self, sender, e):
		self._label1.Text = "608 752-7521"

	def RadioButton3CheckedChanged(self, sender, e):
		self._label1.Text = "608 554-3712"

	def RadioButton4CheckedChanged(self, sender, e):
		self._label1.Text = "608 752-1744"

	def RadioButton5CheckedChanged(self, sender, e):
		self._label1.Text = "608 563-4114"

	def RadioButton6CheckedChanged(self, sender, e):
		Application.Exit()