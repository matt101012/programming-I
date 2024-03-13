import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(132, 39)
		self._label2.TabIndex = 1
		self._label2.Text = "Pick A Car:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 FireBird",
			"1980 Subaru",
			"1975 Cultas"]))
		self._comboBox1.Location = System.Drawing.Point(161, 19)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(172, 21)
		self._comboBox1.TabIndex = 2
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label1.Location = System.Drawing.Point(12, 65)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(132, 39)
		self._label1.TabIndex = 3
		self._label1.Text = "Miles:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label3.Location = System.Drawing.Point(12, 182)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(132, 39)
		self._label3.TabIndex = 4
		self._label3.Text = "MPG:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label4.Location = System.Drawing.Point(12, 124)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(132, 39)
		self._label4.TabIndex = 5
		self._label4.Text = "Gallons:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label5.Location = System.Drawing.Point(160, 68)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(181, 35)
		self._label5.TabIndex = 6
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label6.Location = System.Drawing.Point(161, 124)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(180, 43)
		self._label6.TabIndex = 7
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._label7.Location = System.Drawing.Point(161, 181)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(180, 39)
		self._label7.TabIndex = 8
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._radioButton1.Location = System.Drawing.Point(12, 229)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(99, 47)
		self._radioButton1.TabIndex = 9
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Calculate"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._radioButton2.Location = System.Drawing.Point(127, 229)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(99, 47)
		self._radioButton2.TabIndex = 10
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Clear"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self._radioButton3.Location = System.Drawing.Point(242, 229)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(99, 47)
		self._radioButton3.TabIndex = 11
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Exit"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(355, 288)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "Prog54a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
			
		
		mpg = miles / float(gallons)
		mpg = round(mpg, 1)
		
		self._label7.Text = str(mpg)