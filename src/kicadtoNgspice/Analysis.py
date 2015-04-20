
from PyQt4 import QtGui,QtCore
from PyQt4.Qt import QRect
import TrackWidget

class Analysis(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.track_obj= TrackWidget.TrackWidget()
        self.count =0
        self.parameter_cnt=0
        self.ac_entry_var={}
        self.dc_entry_var={}
        self.tran_entry_var={}
        self.ac_parameter={}
        self.dc_parameter={}
        self.tran_parameter= {}
        self.createAnalysisWidget()
       
                 
    def createAnalysisWidget(self):
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.createCheckBox(),0,0)
        self.grid.addWidget(self.createACgroup(),1,0)
        self.grid.addWidget(self.createDCgroup(),2,0)
        self.grid.addWidget(self.createTRANgroup(),3,0)
            
        '''
        self.grid.addWidget(self.createTRANgroup(),3,0)
        self.grid.addWidget(self.createTRANgroup(),4,0)
        self.grid.addWidget(self.createTRANgroup(),5,0)
        self.grid.addWidget(self.createTRANgroup(),6,0)
        self.grid.addWidget(self.createTRANgroup(),7,0)
        self.grid.addWidget(self.createTRANgroup(),8,0)
        self.grid.addWidget(self.createTRANgroup(),9,0)
        self.grid.addWidget(self.createTRANgroup(),10,0)
        self.grid.addWidget(self.createTRANgroup(),11,0)
        self.grid.addWidget(self.createTRANgroup(),12,0)
        self.grid.addWidget(self.createTRANgroup(),13,0)
        self.grid.addWidget(self.createTRANgroup(),14,0)
        self.grid.addWidget(self.createTRANgroup(),15,0)
        self.grid.addWidget(self.createTRANgroup(),16,0)
        self.grid.addWidget(self.createTRANgroup(),17,0)
        self.grid.addWidget(self.createTRANgroup(),18,0)
        self.grid.addWidget(self.createTRANgroup(),19,0)
        self.grid.addWidget(self.createTRANgroup(),20,0)
        '''
        
        self.setLayout(self.grid)
        self.show()
             
    def createCheckBox(self):
        self.checkbox = QtGui.QGroupBox()
        self.checkbox.setTitle("Select Analysis Type")
        self.checkgrid = QtGui.QGridLayout()
        
        self.checkgroupbtn = QtGui.QButtonGroup()
        self.checkAC = QtGui.QCheckBox("AC")
        self.checkDC = QtGui.QCheckBox("DC")
        self.checkTRAN = QtGui.QCheckBox("TRANSIENT")
        self.checkgroupbtn.addButton(self.checkAC)
        self.checkgroupbtn.addButton(self.checkDC)
        self.checkgroupbtn.addButton(self.checkTRAN)
        self.checkgroupbtn.setExclusive(True)
        self.checkAC.setChecked(True)
        self.checkgroupbtn.buttonClicked.connect(self.enableBox)
        
        self.checkgrid.addWidget(self.checkAC,0,0)
        self.checkgrid.addWidget(self.checkDC,0,1)
        self.checkgrid.addWidget(self.checkTRAN,0,2)
        self.checkbox.setLayout(self.checkgrid)

        #CSS
        '''
        self.checkbox.setStyleSheet(" \
        QGroupBox { border: 1px solid gray; border-radius: 9px; margin-top: 0.5em; } \
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; } \
        ")
        '''
              
        return self.checkbox
        #return self.checkgroupbtn
    
    def enableBox(self):
        if self.checkAC.isChecked():
            self.acbox.setDisabled(False)
            self.dcbox.setDisabled(True)
            self.trbox.setDisabled(True)
            self.track_obj.set_CheckBox["ITEMS"]="AC"
        
        elif self.checkDC.isChecked():
            self.dcbox.setDisabled(False)
            self.acbox.setDisabled(True)
            self.trbox.setDisabled(True)
            self.track_obj.set_CheckBox["ITEMS"]="DC"
        
        elif self.checkTRAN.isChecked():
            self.trbox.setDisabled(False)
            self.acbox.setDisabled(True)
            self.dcbox.setDisabled(True)
            self.track_obj.set_CheckBox["ITEMS"]="TRAN"
                 
    def createACgroup(self):
        self.acbox = QtGui.QGroupBox()
        self.acbox.setTitle("AC Analysis")
        self.acgrid = QtGui.QGridLayout()
        self.acbox.setDisabled(False)
        self.track_obj.set_CheckBox["ITEMS"]="AC"
        self.radiobuttongroup= QtGui.QButtonGroup()
        self.Lin = QtGui.QRadioButton("Lin")
        self.Dec = QtGui.QRadioButton("Dec")
        self.Oct = QtGui.QRadioButton("Oct")
        self.radiobuttongroup.addButton(self.Lin)
        self.radiobuttongroup.addButton(self.Dec)
        self.radiobuttongroup.addButton(self.Oct)
        self.radiobuttongroup.setExclusive(True)
        self.Lin.setChecked(True)
        self.track_obj.AC_type["ITEMS"]="lin"
        self.radiobuttongroup.buttonClicked.connect(self.set_ac_type)
        self.acgrid.addWidget(self.Lin,1,1)
        self.acgrid.addWidget(self.Dec,1,2)
        self.acgrid.addWidget(self.Oct,1,3)
        #self.acbox.setDisabled(True)
        self.acbox.setLayout(self.acgrid)
            
        self.scale = QtGui.QLabel("Scale")
        self.start_fre_lable = QtGui.QLabel("Start Frequency")
        self.stop_fre_lable = QtGui.QLabel("Stop Frequency")
        self.no_of_points = QtGui.QLabel("No.of Points")
        self.acgrid.addWidget(self.scale,1,0)
        self.acgrid.addWidget(self.start_fre_lable,2,0)
        self.acgrid.addWidget(self.stop_fre_lable,3,0)
        self.acgrid.addWidget(self.no_of_points,4,0)
        
        self.count=0
        self.ac_entry_var[self.count] = QtGui.QLineEdit()#start
        self.acgrid.addWidget(self.ac_entry_var[self.count],2,1)
        self.ac_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.ac_entry_var[self.count] = QtGui.QLineEdit()#stop
        self.acgrid.addWidget(self.ac_entry_var[self.count],3,1)
        self.ac_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.ac_entry_var[self.count] = QtGui.QLineEdit()#no of pts
        self.acgrid.addWidget(self.ac_entry_var[self.count],4,1)
        self.ac_entry_var[self.count].setMaximumWidth(150)
        
        self.parameter_cnt=0
        self.start_fre_combo = QtGui.QComboBox()
        self.start_fre_combo.addItem("Hz",)
        self.start_fre_combo.addItem("KHz")
        self.start_fre_combo.addItem("MHz")
        self.start_fre_combo.addItem("GHz")
        self.start_fre_combo.addItem("THz")
        self.start_fre_combo.setMaximumWidth(150)
        self.acgrid.addWidget(self.start_fre_combo,2,2)
        self.ac_parameter[self.parameter_cnt]= self.start_fre_combo.currentText()
        self.start_fre_combo.activated[str].connect(self.start_combovalue)
        
        self.parameter_cnt=self.parameter_cnt + 1
        self.stop_fre_combo = QtGui.QComboBox()
        self.stop_fre_combo.addItem("Hz")
        self.stop_fre_combo.addItem("KHz")
        self.stop_fre_combo.addItem("MHz")
        self.stop_fre_combo.addItem("GHz")
        self.stop_fre_combo.addItem("THz")
        self.stop_fre_combo.setMaximumWidth(150)
        self.acgrid.addWidget(self.stop_fre_combo,3,2)
        self.ac_parameter[self.parameter_cnt]= self.stop_fre_combo.currentText()
        self.stop_fre_combo.activated[str].connect(self.stop_combovalue)
        
        self.track_obj.AC_entry_var["ITEMS"]=self.ac_entry_var
        self.track_obj.AC_Parameter["ITEMS"]=self.ac_parameter
        
        #CSS   
        self.acbox.setStyleSheet(" \
        QGroupBox { border: 1px solid gray; border-radius: 9px; margin-top: 0.5em; } \
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; } \
        ") 
        return self.acbox
    
    def start_combovalue(self, text):
        self.ac_parameter[self.parameter_cnt]= str(text)
    
    def stop_combovalue(self, text):
        self.ac_parameter[self.parameter_cnt+1]= str(text)
    
    def set_ac_type(self):
        self.parameter_cnt=0
        if self.Lin.isChecked():
            self.track_obj.AC_type["ITEMS"]="lin"
        elif self.Dec.isChecked():
            self.track_obj.AC_type["ITEMS"]= "dec" 
        elif self.Oct.isChecked():
            self.track_obj.AC_type["ITEMS"]="oct"
        else:
            pass  
        print "AC type is ", self.Lin.isChecked
    
    def createDCgroup(self):
        self.dcbox = QtGui.QGroupBox()
        self.dcbox.setTitle("DC Analysis")
        self.dcgrid = QtGui.QGridLayout()
        
        self.dcbox.setDisabled(True)
        self.dcbox.setLayout(self.dcgrid)
        
        self.source_name= QtGui.QLabel('Enter Source Name',self)
        self.source_name.setMaximumWidth(150)
        self.start= QtGui.QLabel('start', self)
        self.start.setMaximumWidth(150)
        self.increment=QtGui.QLabel('Increment',self)
        self.increment.setMaximumWidth(150)
        self.stop=QtGui.QLabel('stop',self)
        self.stop.setMaximumWidth(150)

        
        self.dcgrid.addWidget(self.source_name,1,0) 
        self.dcgrid.addWidget(self.start,2,0)
        self.dcgrid.addWidget(self.increment,3,0)
        self.dcgrid.addWidget(self.stop,4,0)        
        
        self.count=0
        self.dc_entry_var[self.count] = QtGui.QLineEdit()#source
        self.dcgrid.addWidget(self.dc_entry_var[self.count],1,1)
        self.dc_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.dc_entry_var[self.count] = QtGui.QLineEdit()#start
        self.dcgrid.addWidget(self.dc_entry_var[self.count],2,1)
        self.dc_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.dc_entry_var[self.count] = QtGui.QLineEdit()#increment
        self.dcgrid.addWidget(self.dc_entry_var[self.count],3,1)
        self.dc_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.dc_entry_var[self.count] = QtGui.QLineEdit()#stop
        self.dcgrid.addWidget(self.dc_entry_var[self.count],4,1)
        self.dc_entry_var[self.count].setMaximumWidth(150)

        self.parameter_cnt=0
        self.start_combo=QtGui.QComboBox(self)
        self.start_combo.setMaximumWidth(150)
        self.start_combo.addItem('volts or Amperes')
        self.start_combo.addItem('mV or mA')
        self.start_combo.addItem('uV or uA')
        self.start_combo.addItem("nV or nA")
        self.start_combo.addItem("pV or pA")
        self.dcgrid.addWidget(self.start_combo,2,2)
        self.dc_parameter[self.parameter_cnt]= self.start_combo.currentText()
        self.start_combo.activated[str].connect(self.start_changecombo)
        self.parameter_cnt= self.parameter_cnt+1
        
        self.increment_combo=QtGui.QComboBox(self)
        self.increment_combo.setMaximumWidth(150)
        self.increment_combo.addItem("volts or Amperes")
        self.increment_combo.addItem("mV or mA")
        self.increment_combo.addItem("uV or uA")
        self.increment_combo.addItem("nV or nA")
        self.increment_combo.addItem("pV or pA")
        self.dcgrid.addWidget(self.increment_combo,3,2)
        self.dc_parameter[self.parameter_cnt]= str(self.increment_combo.currentText())
        self.increment_combo.activated[str].connect(self.increment_changecombo)
        self.parameter_cnt= self.parameter_cnt+1
        
        self.stop_combo=QtGui.QComboBox(self)
        self.stop_combo.setMaximumWidth(150)
        self.stop_combo.addItem("volts or Amperes")
        self.stop_combo.addItem("mV or mA")
        self.stop_combo.addItem("uV or uA")
        self.stop_combo.addItem("nV or nA")
        self.stop_combo.addItem("pV or pA")  
        self.dcgrid.addWidget(self.stop_combo,4,2)
        self.stop_combo.activated[str].connect(self.stop_changecombo)
        self.dc_parameter[self.parameter_cnt]= str(self.stop_combo.currentText())
        self.parameter_cnt= self.parameter_cnt+1
        
        self.check=QtGui.QCheckBox('Operating Point Analysis',self)
        if(self.check.isChecked()):
            self.flagcheck = 1
            
        else:
            self.flagcheck= 2
        self.dcgrid.addWidget(self.check,5,1,5,2)
        self.track_obj.DC_entry_var["ITEMS"]=self.dc_entry_var
        self.track_obj.DC_Parameter["ITEMS"]=self.dc_parameter
        
        #CSS
        self.dcbox.setStyleSheet(" \
        QGroupBox { border: 1px solid gray; border-radius: 9px; margin-top: 0.5em; } \
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; } \
        ")
              
        
        return self.dcbox
    
    def start_changecombo(self,text):
        self.parameter_cnt=0
        self.dc_parameter[self.parameter_cnt]=text
    
    def increment_changecombo(self,text):
        self.dc_parameter[self.parameter_cnt+1]=text
        
    def stop_changecombo(self,text):
        self.dc_parameter[self.parameter_cnt+2]=text
    
    def createTRANgroup(self):
        self.trbox = QtGui.QGroupBox()
        self.trbox.setTitle("Transient Analysis")
        self.trgrid = QtGui.QGridLayout()
        
        self.trbox.setDisabled(True)
        self.trbox.setLayout(self.trgrid)
        
        self.start = QtGui.QLabel("start Time")
        self.step = QtGui.QLabel("Step Time")
        self.stop = QtGui.QLabel("stop Time")
        self.trgrid.addWidget(self.start,1,0)
        self.trgrid.addWidget(self.step,2,0)
        self.trgrid.addWidget(self.stop,3,0)
        self.count=0
        
        self.tran_entry_var[self.count] = QtGui.QLineEdit()
        self.trgrid.addWidget(self.tran_entry_var[self.count],1,1)
        self.tran_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.tran_entry_var[self.count] = QtGui.QLineEdit()
        self.trgrid.addWidget(self.tran_entry_var[self.count],2,1)
        self.tran_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        self.tran_entry_var[self.count] = QtGui.QLineEdit()
        self.trgrid.addWidget(self.tran_entry_var[self.count],3,1)
        self.tran_entry_var[self.count].setMaximumWidth(150)
        self.count= self.count+1
        
        self.parameter_cnt=0
        self.start_combobox = QtGui.QComboBox()
        self.start_combobox.addItem("Sec")
        self.start_combobox.addItem("ms")
        self.start_combobox.addItem("us")
        self.start_combobox.addItem("ns")
        self.start_combobox.addItem("ps")
        self.trgrid.addWidget(self.start_combobox,1,3)
        self.tran_parameter[self.parameter_cnt]=self.start_combobox.currentText()
        self.start_combobox.activated[str].connect(self.start_combo_change)
        self.parameter_cnt= self.parameter_cnt+1
        
        self.step_combobox = QtGui.QComboBox()
        self.step_combobox.addItem("Sec")
        self.step_combobox.addItem("ms")
        self.step_combobox.addItem("us")
        self.step_combobox.addItem("ns")
        self.step_combobox.addItem("ps")
        self.trgrid.addWidget(self.step_combobox,2,3)
        self.tran_parameter[self.parameter_cnt]=self.step_combobox.currentText()
        self.step_combobox.activated[str].connect(self.step_combo_change)
        self.parameter_cnt= self.parameter_cnt+1
        
        self.stop_combobox = QtGui.QComboBox()
        self.stop_combobox.addItem("Sec")
        self.stop_combobox.addItem("ms")
        self.stop_combobox.addItem("us")
        self.stop_combobox.addItem("ns")
        self.stop_combobox.addItem("ps")
        self.trgrid.addWidget(self.stop_combobox,3,3)
        self.tran_parameter[self.parameter_cnt]=self.stop_combobox.currentText()
        self.stop_combobox.activated[str].connect(self.stop_combo_change)
        self.parameter_cnt= self.parameter_cnt+1
        
        self.track_obj.TRAN_entry_var["ITEMS"]=self.tran_entry_var
        self.track_obj.TRAN_Parameter["ITEMS"]=self.tran_parameter
    
        #CSS
        self.trbox.setStyleSheet(" \
        QGroupBox { border: 1px solid gray; border-radius: 9px; margin-top: 0.5em; } \
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px; } \
        ")
              
        
        return self.trbox    
    
    def start_combo_change(self,text):
        self.parameter_cnt=0
        self.tran_parameter[self.parameter_cnt]=text
        
    def step_combo_change(self,text):
        self.tran_parameter[self.parameter_cnt+1]=text
        
    def stop_combo_change(self,text):
        self.tran_parameter[self.parameter_cnt+2]=text