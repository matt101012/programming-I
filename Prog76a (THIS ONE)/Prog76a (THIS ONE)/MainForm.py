import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton11 = System.Windows.Forms.RadioButton()
		self._radioButton12 = System.Windows.Forms.RadioButton()
		self._radioButton13 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._groupBox1.Controls.Add(self._radioButton10)
		self._groupBox1.Controls.Add(self._radioButton9)
		self._groupBox1.Controls.Add(self._radioButton8)
		self._groupBox1.Controls.Add(self._radioButton7)
		self._groupBox1.Controls.Add(self._radioButton6)
		self._groupBox1.Controls.Add(self._radioButton5)
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(7, 188)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(193, 227)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(0, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(89, 34)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "0"
		self._radioButton1.UseVisualStyleBackColor = True
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(0, 59)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(89, 34)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "1"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(0, 99)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(89, 34)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "2"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(0, 139)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(89, 34)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "3"
		self._radioButton4.UseVisualStyleBackColor = True
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(0, 179)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(89, 34)
		self._radioButton5.TabIndex = 4
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "4"
		self._radioButton5.UseVisualStyleBackColor = True
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(104, 19)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(89, 34)
		self._radioButton6.TabIndex = 5
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "5"
		self._radioButton6.UseVisualStyleBackColor = True
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(104, 59)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(89, 34)
		self._radioButton7.TabIndex = 6
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "6"
		self._radioButton7.UseVisualStyleBackColor = True
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(104, 99)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(89, 34)
		self._radioButton8.TabIndex = 7
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "7"
		self._radioButton8.UseVisualStyleBackColor = True
		self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(104, 139)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(89, 34)
		self._radioButton9.TabIndex = 8
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "8"
		self._radioButton9.UseVisualStyleBackColor = True
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(104, 179)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(89, 34)
		self._radioButton10.TabIndex = 9
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "9"
		self._radioButton10.UseVisualStyleBackColor = True
		self._radioButton10.CheckedChanged += self.RadioButton10CheckedChanged
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(192, 150)
		self._label1.TabIndex = 1
		self._label1.Text = "Choose a number below:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radioButton11
		# 
		self._radioButton11.BackColor = System.Drawing.SystemColors.Window
		self._radioButton11.Location = System.Drawing.Point(198, 123)
		self._radioButton11.Name = "radioButton11"
		self._radioButton11.Size = System.Drawing.Size(323, 60)
		self._radioButton11.TabIndex = 2
		self._radioButton11.TabStop = True
		self._radioButton11.Text = "Calculate"
		self._radioButton11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton11.UseVisualStyleBackColor = False
		self._radioButton11.CheckedChanged += self.RadioButton11CheckedChanged
		# 
		# radioButton12
		# 
		self._radioButton12.BackColor = System.Drawing.SystemColors.Window
		self._radioButton12.Location = System.Drawing.Point(198, 33)
		self._radioButton12.Name = "radioButton12"
		self._radioButton12.Size = System.Drawing.Size(152, 76)
		self._radioButton12.TabIndex = 3
		self._radioButton12.TabStop = True
		self._radioButton12.Text = "Clear"
		self._radioButton12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton12.UseVisualStyleBackColor = False
		self._radioButton12.CheckedChanged += self.RadioButton12CheckedChanged
		# 
		# radioButton13
		# 
		self._radioButton13.BackColor = System.Drawing.SystemColors.Window
		self._radioButton13.Location = System.Drawing.Point(366, 32)
		self._radioButton13.Name = "radioButton13"
		self._radioButton13.Size = System.Drawing.Size(155, 77)
		self._radioButton13.TabIndex = 4
		self._radioButton13.TabStop = True
		self._radioButton13.Text = """Exit
"""
		self._radioButton13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._radioButton13.UseVisualStyleBackColor = False
		self._radioButton13.CheckedChanged += self.RadioButton13CheckedChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.Window
		self._label2.Location = System.Drawing.Point(228, 200)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(292, 214)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(545, 457)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radioButton13)
		self.Controls.Add(self._radioButton12)
		self.Controls.Add(self._radioButton11)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Prog76a (THIS ONE)"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def RadioButton1CheckedChanged(self, sender, e):
		self._label2.Text = "0 \nx9 \n__________"

	def RadioButton2CheckedChanged(self, sender, e):
		self._label2.Text = "1 \nx9 \n__________"

	def RadioButton3CheckedChanged(self, sender, e):
		self._label2.Text = "2 \nx9 \n__________"

	def RadioButton4CheckedChanged(self, sender, e):
		self._label2.Text = "3 \nx9 \n__________"

	def RadioButton5CheckedChanged(self, sender, e):
		self._label2.Text = "4 \nx9 \n__________"

	def RadioButton6CheckedChanged(self, sender, e):
		self._label2.Text = "5 \nx9 \n__________"

	def RadioButton7CheckedChanged(self, sender, e):
		self._label2.Text = "6 \nx9 \n__________"

	def RadioButton8CheckedChanged(self, sender, e):
		self._label2.Text = "7 \nx9 \n__________"

	def RadioButton9CheckedChanged(self, sender, e):
		self._label2.Text = "8 \nx9 \n__________"

	def RadioButton10CheckedChanged(self, sender, e):
		self._label2.Text = "9 \nx9 \n__________"

	def RadioButton11CheckedChanged(self, sender, e):
		selnum = 0 
		if self._radioButton1.Checked == True:
			selnum = 0
		elif self.RadioButton2.Checked: # == True
			selnum = 1
		elif self.RadioButton3.Checked: # == True
			selnum = 2
		elif self.RadioButton4.Checked: # == True
			selnum = 3
		elif self.RadioButton5.Checked: # == True
			selnum = 4
		elif self.RadioButton6.Checked: # == True
			selnum = 5
		elif self.RadioButton7.Checked: # == True
			selnum = 6
		elif self.RadioButton8.Checked: # == True
			selnum = 7
		elif self.RadioButton9.Checked: # == True
			selnum = 8
		elif self.RadioButton10.Checked: # == True
			selnum = 9

		step1 = selnum * 9
		step2 = step1 * 12345679
	
	
		self._label2.Text += "\n" + str(step1) + "\nx12345679" + \
						 	 "\n__________\n" + str(step2)
	
	def RadioButton12CheckedChanged(self, sender, e):
		self._label1.Text = ""
	def RadioButton13CheckedChanged(self,ender, e):
		Application.Exit()
	def Label2Click(self, sender, e):
		pass