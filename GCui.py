#region---------  GCShort v1.0a-------------------
#---------------  Gurkan Corumlu  --------------------
#---------------  Setup Maya:     --------------------
# from imp import reload
# import GCui
# reload(GCui)
# GCui.UIWindows().Show()
#-----------------------------------------------------
#-----------------------------------------------------
#endregion--------------------------------------------
#region library
from maya import cmds
import time
import random
import maya.mel as mel
import os
#endregion
class UIWindows(object):
    def Show(self):

        #region ---  Windows
        if cmds.window('GCWin', exists=True):
            cmds.deleteUI('GCWin')
        # Create the window
        window = cmds.window('GCWin', title='GC Script v0.0.1', s=True, width=300, height=300)
        column = cmds.columnLayout(adjustableColumn=True)
        #endregion
        
        #region Selected Type
        
        selected_frame = cmds.frameLayout(cl=True,collapsable=False, label='Selected Type')
        selrowplane = cmds.rowLayout(numberOfColumns=8, columnWidth2=(300, 50))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_envBall.png', label='All', command= lambda *args:self.SelectMode(0))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_nurbsCurve.png', label='Curve', command= lambda *args:self.SelectMode(1))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_polyCube.png', label='Poly' , command= lambda *args:self.SelectMode(2))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_joint.png', label='Joint' , command= lambda *args:self.SelectMode(3))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_ikSplineSolver.png', label='Cur&Jo' , command= lambda *args:self.SelectMode(4))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='out_lattice.png', label='Defor' , command= lambda *args:self.SelectMode(5))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='HIKCharacterToolFullBody.png', label='Help' , command= lambda *args:self.SelectMode(6))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='positionAlongCurve.png', label='De&cur' , command= lambda *args:self.SelectMode(7))

        cmds.setParent('..')
        row1 = cmds.rowLayout(numberOfColumns=8, columnWidth2=(150, 50))
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='menuIconModify.png', label='Freeze', command=cmds.FreezeTransformations)
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='menuIconModify.png', label='Reset',  command=cmds.ResetTransformations)
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='menuIconModify.png', label='Center',  command=cmds.CenterPivot)
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='locator.png', label='Group', command=cmds.Group)
        cmds.iconTextButton(h=50, w=40, style='iconAndTextVertical', image1='greasePencilPencil.png', label='Separat', command= lambda *args:self.AllMelCommand("addShelfSeparator();"))
        cmds.setParent('..')
        cmds.setParent(column)
        #endregion
        
        #region ---- Special Settings Add a collapsible frame for display options
        display_frame = cmds.frameLayout(cl=True,collapsable=True, label='Special Settings')
        cmds.columnLayout()
        row = cmds.rowLayout(numberOfColumns=2)
        cmds.text(h=20, w=150, l='Change All Material to:')
        self.shaderName = cmds.textField(h=20, w=100, tx='lambert')
        cmds.setParent('..')
        
        row = cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        cmds.button(h=40, w=100, bgc=(0.1, 0.2, 0.3), label='Is Name Avaible', command = self.is_name_available)
        cmds.button(h=40, w=100, bgc=(0.1, 0, 0.3), label='Clear Name Space', command= self.GcRemoveAllNamespaces)
        cmds.button(h=40, w=100, bgc=(0.1, 0.2, 0.3), label='Set Shader Type', command= self.ChangeAllMaterialType)
        cmds.setParent('..')
        cmds.scrollField(w=300,h=50, editable=False, wordWrap=True, text='*Unlock All model type of all children in hierarchy' )
        rowlock = cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        self.lockCheck = cmds.checkBox(align="center",w=100,l="Lock")
        cmds.button(h=40, w=100, bgc=(0.1, 0.2, 0.3), label='Lock Change', command= self.AllLockCahnge)
        cmds.button(h=40, w=100, bgc=(0.1, 0.2, 0.3), label='Delete All UV', command= self.CopyAndDeleteUV)
        cmds.setParent('..')
        cmds.setParent('..')
        cmds.setParent('..')
        #endregion ----

        #region Model Mix
        cmds.frameLayout(cl=True,collapsable=True, label='Selected Mix Up')
        cmds.scrollField(w=300,h=70, editable=False, wordWrap=True, text='*Select the objects to distribute. \n*It will be distributed according to the following values.' )
        min_value = 0
        max_value = 360
        cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        cmds.text(align='center' ,h=20, w=100,label="test")
        cmds.text(align='center', h=20, w=50,label="Min")
        cmds.text(align='center', h=20, w=50,label="Max")
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        cmds.text(w=100, label="Translate X: ")
        self.crashminX = cmds.floatField()
        self.crashmaxX = cmds.floatField()
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        cmds.text(w=100, label="Translate Y: ")
        self.crashminY = cmds.floatField()
        self.crashmaxY = cmds.floatField()
        cmds.setParent('..')
        cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        cmds.text(w=100, label="Translate X: ")
        self.crashminZ = cmds.floatField()
        self.crashmaxZ = cmds.floatField()
        cmds.setParent('..')
        # Slider oluştur
        cmds.columnLayout(columnWidth=100, co= ('left', -100))
        self.crashRotX = cmds.floatSliderGrp(label="Rot X:", field=True, minValue=min_value, maxValue=max_value, value=0)
        self.crashRotY = cmds.floatSliderGrp(label="Rot Y:", field=True, minValue=min_value, maxValue=max_value, value=0)
        self.crashRotZ = cmds.floatSliderGrp(label="Rot Z:", field=True, minValue=min_value, maxValue=max_value, value=0)
        cmds.setParent('..')
        cmds.button(label = "Mix Up", bgc=(0.1,0.2,0.3),w=100, h=40, command = self.randomize_transformations)
        cmds.setParent('..')

        #endregion
 


        #region ---- Walk Plane
        Walk_frame = cmds.frameLayout(cl=True,collapsable=True, label='Walk / Run Plane')
        cmds.scrollField(h=60, editable=False, wordWrap=True, text='*Creates a walking plane is creating for walk/run animation\n*Select X or Z way' )
        rowplane = cmds.rowLayout(numberOfColumns=4, columnWidth2=(300, 50))
        cmds.text(w=75, label="Speed :")
        self.planeSpeed= cmds.floatField(w=75,v=1,step=.01,max=15, pre=True, cc=self.PlaneSpeedChange)
        self.planeRadio = cmds.radioButtonGrp (numberOfRadioButtons=2, labelArray2=['X Way', 'Z Way'], select = 2)
        cmds.setParent('..')
        cmds.button(h=40, w=300, bgc=(0.1, 0.8, 0.3), label='Create Plane', command=self.CreatePlane)
        cmds.button(h=40, w=300, bgc=(0.4, 0.2, 0.2), label='Delete Plane', command=self.DeletePlane)
        cmds.setParent('..')
        #endregion



        #region ---- Add a collapsible frame for time options
        time_frame = cmds.frameLayout(cl=True,collapsable=True, label='TimeSlider Key Copy/Paste')
        row2 = cmds.rowLayout(numberOfColumns=3, columnWidth2=(300, 50))
        #?button( label=name, command = lambda *args: buttonPressed(name) )
        cmds.button(h=30, w=100, bgc=(0, 0.2, 0), label='Copy Key', command = self.copyKeyFnc)
        cmds.button(h=30, w=100, bgc=(0, 0.2, 0), label='Paste Key', command = self.pasteKeyFnc)
        cmds.button(h=30, w=100, bgc=(0, 0.2, 0.2), label='Delete Key', command = self.deleteKeyFnc)
        cmds.setParent(column)
        cmds.setParent(column)
        cmds.setParent(column)
        #endregion ----
        
        #region ---- Bake Animation____________________________________________________________
        anim_frame = cmds.frameLayout(cl=True,collapsable=True, label='Bake Animation')
        #rowLayout -cal 1 "right" -numberOfColumns 2 -columnWidth2 100 30;
        row3 = cmds.rowLayout(numberOfColumns=2)
        cmds.text(w=100, h=30, label='Start Key: ')
        self.timeStart =  cmds.intField(w=100, h=30, bgc=(0.5, 0.7, 0.5), min=0)
        cmds.setParent('..')
        row4 = cmds.rowLayout(numberOfColumns=2)
        cmds.text(w=100, h=30, label='End Key: ')
        self.timeEnd =  cmds.intField(w=100, h=30, bgc=(0.5, 0.7, 0.5), min=0, v=100)
        cmds.setParent('..')
        cmds.button(h=40, w=300, bgc=(0.5, 0.7, 0.7),  label='BAKE', command= self.BakeAnimationStart)	
        cmds.setParent('..')
        #endregion ----

        #region ---- AnimSHAKE__________________________________________________________________________
        anim_frame = cmds.frameLayout(cl=True,collapsable=True, label='GC Anim Shake')
        cmds.scrollField( editable=False, wordWrap=True, text='Select the start and end for animation shake. \nEnter a Shake value for transform or rotate. \nValues left at "0" will not work.' )
        rowShake1 = cmds.rowLayout(numberOfColumns=4)
        cmds.text(w=110, h=30, label='AnimShake Start: ', align='right')
        self.timeStartShake =  cmds.intField(w=40, h=30, bgc=(0.5, 0.7, 0.5), min=0)
        cmds.text(w=110, h=30, label='AnimShake End: ', align='right')
        self.timeEndShake =  cmds.intField(w=40, h=30, bgc=(0.5, 0.7, 0.5), min=0, v=100)
        cmds.setParent('..')
        cmds.columnLayout(columnWidth=100, co= ('left', -40))
        self.ofTX = cmds.floatSliderGrp(label='Offset Translate X', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
        self.ofTY = cmds.floatSliderGrp(label='Offset Translate Y', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
        self.ofTZ = cmds.floatSliderGrp(label='Offset Translate Z', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )

        self.ofRX = cmds.floatSliderGrp(label='Offset Rotate X', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
        self.ofRY = cmds.floatSliderGrp(label='Offset Rotate Y', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
        self.ofRZ = cmds.floatSliderGrp(label='Offset Rotate Z', field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-100.0, fieldMaxValue=100.0, value=0 )
        cmds.setParent('..')
        
        cmds.button(h=40, w=150, bgc=(0.2, 0.1, 0.2), label='GC Shake Animation', command=self.ShakeFnkCalc)
        cmds.setParent('..')
        #endregion ----

        #region ---- GCAnimScale__________________________________  
        anim_frame = cmds.frameLayout(cl=True, collapsable=True, label='Anim Scale')
        
        cmds.columnLayout(columnWidth=250, co= ('left', 70))
        
        self.selROOT = cmds.textField(bgc=(0.2,0.2,0.2),tx='No Root Selected!',h=50, w=220, en=False )
        cmds.button(label='Select ROOT', width=220, align='center', command= self.SelectRootBoneFnk)
        cmds.setParent('..')

        cmds.columnLayout(columnWidth=250, co= ('left', -40))
        self.rootSCALE = cmds.floatSliderGrp(label='Offset Scale', field=True, minValue=-100, maxValue=100, fieldMinValue=-100, fieldMaxValue=100, value=1, cc= self.AllBonesScaleFnk)
        cmds.setParent('..')

        cmds.button(h=40, w=150, bgc=(0.5, 0.6, 0), label='GC Anim Scale', command= self.AnimScaleCalcMake)
        cmds.setParent('..')
        
        #endregion ----
       
        #region ---- Conver Skeletal mesh__________________________________  
        anim_frame = cmds.frameLayout(cl=True, collapsable=True, label='Convert Skeletal Mesh')
        cmds.scrollField(h=55, editable=False, wordWrap=True, text='*Select the animated mesh/meshes. \n*Skinning should not be an object.\n*Bake in timeslider')
        cmds.button(h=40, w=150, bgc=(0.8, 0.8, 0.8), label='Convert / Skeletal Mesh', command= self.BakeModelToJoint)
        cmds.setParent('..')
        #endregion  ---

        #region ---- Developer Information_______________________________
        anim_frame = cmds.frameLayout(cl=True,collapsable=True, label='Developer Information')
        cmds.scrollField(h=150, editable=False, wordWrap=True, text='This GC Script was prepared in 2020. \nI combined minis and basic shortcuts.\n\n\n\nDevelopment: Gurkan CORUMLU\nYear:2020\nversion: 0.0.1' )
        cmds.setParent('..')
        cmds.showWindow('GCWin')
        #endregion
        cmds.showWindow('GCWin')
    
    #region All FUNCTION
    def AllMelCommand(self, *args, strCommand=""):
        mel.eval(strCommand)
    def randomize_transformations(self,*args):
        min_translation = [cmds.floatField(self.crashminX, query=True, value=True),
                           cmds.floatField(self.crashminY, query=True, value=True),
                           cmds.floatField(self.crashminZ, query=True, value=True)]
        
        max_translation = [cmds.floatField(self.crashmaxX, query=True, value=True),
                           cmds.floatField(self.crashmaxY, query=True, value=True),
                           cmds.floatField(self.crashmaxZ, query=True, value=True)]
        max_rotation = [cmds.floatSliderGrp(self.crashRotX, query=True, value=True),
                        cmds.floatSliderGrp(self.crashRotY, query=True, value=True),
                        cmds.floatSliderGrp(self.crashRotZ, query=True, value=True)]
        # Seçili nesneleri al
        selected_objects = cmds.ls(selection=True)

        if not selected_objects:
            cmds.warning("Nesne seçilmedi!")
            return

        # Her seçili nesne için
        for obj in selected_objects:
            # Rastgele konumlandırma
            random_position = [random.uniform(min_translation[0], max_translation[0]),
                            random.uniform(min_translation[1], max_translation[1]),
                            random.uniform(min_translation[2], max_translation[2])]
            # Rastgele döndürme
            random_rotation = [random.uniform(0, max_rotation[0]),
                            random.uniform(0, max_rotation[1]),
                            random.uniform(0, max_rotation[2])]
            # Transformları ayarla
            cmds.xform(obj, translation=random_position, rotation=random_rotation)

    def SelectMode(self,v):
        cmds.selectMode(object=True)
        if(v==0):
            cmds.selectType( allObjects=True, allComponents=False )
        elif(v==1):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(c=True,allComponents=False ) 
        elif(v==2):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(polymesh=True,allComponents=False ) 
        elif(v==3):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(joint=True, allComponents=False ) 
        elif(v==4):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(joint=True,c=True, allComponents=False ) 
        elif(v==5):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(la=True, cl=True, allComponents=False ) 
        elif(v==6):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(locator=True, allComponents=False ) 
        elif(v==7):
           cmds.selectType( allObjects=False, allComponents=False )
           cmds.selectType(la=True, cl=True, c=True, allComponents=False )  


    #_________Modeling bake to joint anim________________
    def BakeModelToJoint(self,*args):
        #list
        jointList = []	#creating joint list
        jointCons = []	#for animbake constraint list
        selected = cmds.ls(selection=True)# All animation Selected objects        
        
        if not selected:
            cmds.warning("No select object")
            return
        
        #progress bar start
        prgoressWindow = cmds.window()
        cmds.columnLayout()
        progressbar = cmds.progressBar(maxValue=6, width=300)
        cmds.showWindow( prgoressWindow )
        cmds.waitCursor(state=True)   
        #__________________


        cmds.select(cl=True)
        rootJoint = cmds.joint(name= "RootJointTransform")#Create Root Joint
        cmds.select(cl=True)
        cmds.progressBar(progressbar, edit=True, step=1)
        #attached constraint with joint and obje..
        for obj in selected:
            pos = cmds.xform(obj, q=True, ws=True, t=True)
            joi = cmds.joint(position=pos, name="Anim_joint_"+obj)
            jointList.append(joi)
            cmds.parent(joi, rootJoint)
            cons = cmds.parentConstraint(obj, joi)
            jointCons.append(cons)
        cmds.progressBar(progressbar, edit=True, step=1)    


        #Bake Anim to Joint
        minTimeValue = cmds.playbackOptions(q=True, min=True)# timeslider min
        maxTimeValue = cmds.playbackOptions(q=True, max=True)# timeslider max
        cmds.progressBar(progressbar, edit=True, step=1)
        cmds.select(rootJoint)
        cmds.ls(selection=True)
        cmds.select(hi=True)
        slc =cmds.ls(selection=True)
        cmds.bakeResults(slc, t=(minTimeValue, maxTimeValue), simulation=True)
        cmds.progressBar(progressbar, edit=True, step=1)

        
        # All Constraint deleted
        for cons in jointCons:
            cmds.delete(cons)
        cmds.progressBar(progressbar, edit=True, step=1)

        #All model smoth bind
        for obj in selected:
            cmds.cutKey(obj, t=(0,maxTimeValue))#important here.. if the animation not deleted it will not work incorrectly
            jointName = "Anim_joint_"+obj
            cmds.skinCluster(obj, jointName, toSelectedBones=True, bindMethod=0, skinMethod=0)
        cmds.progressBar(progressbar, edit=True, step=1)
        cmds.waitCursor(state=False)
        cmds.deleteUI(prgoressWindow)

    #selecct root bone_________________________________________________________

    def SelectRootBoneFnk(self, *args):
        selection = cmds.ls(selection=True)
        if not selection:
            cmds.warning("No select object")
            return
        cmds.textField(self.selROOT, edit=True, text=selection[0])
    
    def AllBonesScaleFnk(self, *args):
        sec = cmds.textField(self.selROOT, query=True, text=True)
        try:
            cmds.select(sec)
        except:
            cmds.warning("There is no object name in this name.")
            return

        #cmds.select(hi=True)
        x = cmds.floatSliderGrp(self.rootSCALE, query=True, value=True)
        cmds.scale(x, x, x)
        cmds.select(cl=True)
    
    def AnimScaleCalcMake(self, *args):
        min_time = cmds.playbackOptions(q=True, minTime=True)
        max_time = cmds.playbackOptions(q=True, maxTime=True)
        cmds.select(clear=True)
        sec = cmds.textField(self.selROOT, q=True, text=True)
        try:
            cmds.select(sec)
            cmds.warning("\nSelect model:  "+ sec)
        except:
            cmds.warning("There is no object name in this name.")
            return
        cmds.select(hi=True)
        obj = cmds.ls(sl=True)
        cmds.warning(obj[1])
        x = cmds.floatSliderGrp(self.rootSCALE, query=True, value=True)
        for i in range(int(min_time), int(max_time) + 1):
            cmds.currentTime(i)
            cmds.warning(i)
            for item in obj:
                xboy = cmds.getAttr(item + ".translateX")
                yboy = cmds.getAttr(item + ".translateY")
                zboy = cmds.getAttr(item + ".translateZ")
                cmds.setAttr(item + ".translateX", xboy * x)
                cmds.setAttr(item + ".translateY", yboy * x)
                cmds.setAttr(item + ".translateZ", zboy * x)
                # cmds.move(x, x, x, r=True)
                cmds.scale(1, 1, 1)
            cmds.setKeyframe()

    #____SHAKE CALC____________________________________

    def ShakeFnkCalc(self, *args):
        minTime = cmds.intField(self.timeStartShake, query=True, value=True) # start time slider
        maxTime = cmds.intField(self.timeEndShake  , query=True, value=True) # start time slider
        difKey = maxTime-minTime
        if difKey < 2:
            cmds.warning("Time problem.. Check Start Key value and Max Key Value")
            return
        selectedOBJ = cmds.ls(sl=True)[0]
        if not selectedOBJ:
            cmds.warning("No select object")
            return
        tx = cmds.floatSliderGrp(self.ofTX, q=True, value=True)
        ty = cmds.floatSliderGrp(self.ofTY, q=True, value=True)
        tz = cmds.floatSliderGrp(self.ofTZ, q=True, value=True)

        rx = cmds.floatSliderGrp(self.ofRX, q=True, value=True)
        ry = cmds.floatSliderGrp(self.ofRY, q=True, value=True)
        rz = cmds.floatSliderGrp(self.ofRZ, q=True, value=True)

        if tx==0 and ty==0 and tz==0 and rx==0 and ry==0 and rz==0:
            cmds.warning("All offset value 0")
            return
            
        xTboy = cmds.getAttr(selectedOBJ + '.translateX')
        yTboy = cmds.getAttr(selectedOBJ + ".translateY")
        zTboy = cmds.getAttr(selectedOBJ + ".translateZ")
        xRboy = cmds.getAttr(selectedOBJ + ".translateX")
        yRboy = cmds.getAttr(selectedOBJ + ".translateY")
        zRboy = cmds.getAttr(selectedOBJ + ".translateZ")

        #-----progreess barr---------
        prgoressWindow = cmds.window()
        cmds.columnLayout()
        progressbar = cmds.progressBar(maxValue=difKey, width=300)
        cmds.showWindow( prgoressWindow )
        cmds.waitCursor(state=True)  

        for i in range(int(minTime), int(maxTime)+1):
            cmds.progressBar(progressbar, edit=True, step=1)
            cmds.currentTime(i)
            print("say: ")
            if (tx!=0):
                xboy = xTboy + random.uniform(0,tx)
                cmds.setAttr(selectedOBJ + ".translateX", xboy)
            if (ty!=0):
                yboy = yTboy+random.uniform(0,ty)
                cmds.setAttr(selectedOBJ + ".translateY", yboy)
            if (tz!=0):
                zboy = zTboy+random.uniform(0,tz)
                cmds.setAttr(selectedOBJ + ".translateZ", zboy)
            if (rx!=0):
                xRboy = xTboy + random.uniform(0,rx)
                cmds.setAttr(selectedOBJ + ".rotateX", xRboy)
            if (ry!=0):
                yRboy = yTboy+random.uniform(0,ry)
                cmds.setAttr(selectedOBJ + ".rotateY", yRboy)
            if (rz!=0):
                zRboy = zTboy+random.uniform(0,rz)
                cmds.setAttr(selectedOBJ + ".rotateZ", zRboy)
            cmds.setKeyframe()
        cmds.waitCursor(state=False)    
        cmds.deleteUI(prgoressWindow)
    #BakeAnimation__________________________________________________________________________________________	
    def BakeAnimationStart(self, *args):
        selection = cmds.ls(selection=True)
        minTimeValue = cmds.intField(self.timeStart, query=True, value=True)
        maxTimeValue = cmds.intField(self.timeEnd, query=True, value=True)
        maxValue = maxTimeValue - minTimeValue
        if maxValue < 1:
            cmds.warning("Time problem.. Check Start Key value and Max Key Value")
            return
        if not selection:
            cmds.warning("No select object")
            return

        cmds.waitCursor(state=True)   
        current_time = minTimeValue  	
        cmds.bakeSimulation( selection, t=(minTimeValue,maxTimeValue)) #bake simulation
        cmds.waitCursor(state=False)
    
    #________________________________________________________________________________________
    #Copy Key
    def copyKeyFnc(self, *args):
        print('Copying animation keys...')
        keyA = cmds.currentTime(q=True)
        cmds.copyKey(time = (keyA, keyA))
    #paste key
    def pasteKeyFnc(self, *args):
        print('Pasting animation keys...')
        keyA = cmds.currentTime(q=True)
        cmds.pasteKey(time = (keyA, keyA))
    #delete key
    def deleteKeyFnc(self, *args):
        print('Pasting animation keys...')
        keyA = cmds.currentTime(q=True)
        cmds.cutKey(time = (keyA, keyA))        
    #______Walk Plane______________________________________________________________________
    def CreatePlane(self, *args):
        speed = cmds.floatField(self.planeSpeed, q=True, value=True)
        select = cmds.radioButtonGrp(self.planeRadio, q=True, sl=True)# 1 = X  --- 2 = Z //default 2 
        cmds.warning(select)
        if(select==2):
            pPlane = cmds.polyPlane(w= 600,  h= 1200, name = 'WalkRunPlane')
        else:
            pPlane = cmds.polyPlane(w= 1200,  h= 600, name = 'WalkRunPlane')

        selectObj = cmds.ls(sl=True)
        walkRunLayer = cmds.createDisplayLayer(name="AnimPlane", number=1, nr=True)
       
        #shader create
        shader = cmds.shadingNode("blinn", asShader=True, name="WalkRunGridMaterial")
        sg = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=shader + "GridSG")
        #grid create
        texture = cmds.shadingNode("place2dTexture", asUtility=True, name="WalkRunGridMaterialGridTexture")
        grid = cmds.shadingNode("grid", asTexture=True, name="Grid")
        #connect shader and grid texture
        cmds.connectAttr(texture + ".outUV", grid + ".uvCoord")
        cmds.connectAttr(texture + ".outUvFilterSize", grid + ".uvFilterSize")
        cmds.connectAttr(grid + ".outColor", shader + ".color")
        cmds.connectAttr(shader + ".outColor", sg + ".surfaceShader")
        #set greid UV
        
        if(select==2):
            cmds.setAttr(texture + ".repeatU", 20)
            cmds.setAttr(texture + ".repeatV", 40)
            cmds.expression(s = texture + '.offsetV=-time*'+ str(speed), n="WalkRunGridExpresion")
        else:
            cmds.setAttr(texture + ".repeatU", 40)
            cmds.setAttr(texture + ".repeatV", 20)
            cmds.expression(s = texture + '.offsetU=time*'+ str(speed), n="WalkRunGridExpresion")
        #connect to mesh shader
        cmds.sets(pPlane, e=1, forceElement=sg)
        cmds.select(clear=True)
    def DeletePlane(self, *args):
        cmds.delete("WalkRunPlane")
        cmds.delete("AnimPlane")
        cmds.delete("WalkRunGridMaterial")
        cmds.delete("WalkRunGridMaterialGridTexture")
        cmds.delete("WalkRunGridMaterialGridSG")
    def PlaneSpeedChange(self, *args):
        speed = cmds.floatField(self.planeSpeed, q=True, value=True)
        select = cmds.radioButtonGrp(self.planeRadio, q=True, sl=True)# 1 = X  --- 2 = Z //default 2 
        cmds.warning(select)
        
        try:
            cmds.delete("WalkRunGridExpresion")
            if(select==2):
                cmds.expression(s = 'WalkRunGridMaterialGridTexture.offsetV=-time*'+ str(speed), n="WalkRunGridExpresion")
            else:
                cmds.expression(s = 'WalkRunGridMaterialGridTexture.offsetU=time*'+ str(speed), n="WalkRunGridExpresion")

        except:
            cmds.warning("Time problem.. not found expresion")
    #______ISNameAvable______________________________________________________________________
    def is_name_available(self, *args):
        selected = cmds.ls(sl=True)
        if not selected:
            cmds.warning("No selected object")
            return
        avaibleBool = True
        oldSelect = selected[0]
        if len(selected) >0:
            selected.sort(key=len, reverse=True)
        for obj in selected:
            shortName = obj.split("|")[-1]
            if oldSelect == shortName:
                avaibleBool = False
        if avaibleBool == True:
            cmds.warning("{} name is not avaible".format(oldSelect))
        else:
            print("Object name is avaible")
    #All Material Change_______________________________________________________________________	
    def ChangeAllMaterialType(self, *args):
        all_materials = cmds.ls(materials=True)
        for material in all_materials:
            try:
                material_type = cmds.nodeType(material)
                shName = cmds.textField(self.shaderName, query=True, tx=True)
                if material_type != shName:
                    lambert_material = cmds.shadingNode(shName, asShader=True, name=material + "_lambert")
                    connections = cmds.listConnections(material, source=True, destination=False, connections=True)
                    if connections:
                        for src, dest in connections:
                            cmds.connectAttr(src, lambert_material + "." + dest.split(".")[-1])
                    cmds.delete(material)
            except Exception:
                cmds.warning("no change this material :  " + material)
    #Progress Bar NextFrame____________________________________________________
    def AllLockCahnge(self, *args):
        cmds.ls(selection=True)
        cmds.select(hi=True)
        selectAll =cmds.ls(selection=True)
        if not selectAll:
            cmds.warning("No select object")
            return
        lockType = cmds.checkBox(self.lockCheck, query=True, v=True)
        lockInt =  int(lockType == True)
        for obj in selectAll:
            if cmds.lockNode(obj,q=1,l=1) != lockInt:
                cmds.lockNode(obj,l=lockInt)
                cmds.warning('%s change.'%obj)
            else:
                cmds.warning( '%s No Change.'%obj)
    #All UV Copy and Delete____________
    def CopyAndDeleteUV(self, *args):
        selected_objects = cmds.ls(selection=True)
        for obj in selected_objects:
            cmds.select(obj)
            uv_sets = cmds.polyUVSet(obj, query=True, allUVSets=True)
            #region progress bar start
            prgoressWindow = cmds.window(title="UV Calculation..")
            cmds.columnLayout()
            progressbar = cmds.progressBar(maxValue=6, width=300)
            cmds.showWindow( prgoressWindow )
            cmds.waitCursor(state=True)   
            #endregion
            cmds.progressBar(progressbar, edit=True, max=len(uv_sets))
            for uv_set in uv_sets:
                cmds.progressBar(progressbar, edit=True, step=1)
                if uv_set!= 'map1':
                    cmds.polyUVSet(obj, currentUVSet=True, uvSet=uv_set)
                    cmds.select(obj)
                    cmds.SelectUVMask()
                    cmds.SelectAll()
                    try:
                        cmds.polyCopyUV(uvi=uv_set, uvSetName='map1')
                    except Exception:
                        cmds.warning("no selected vertex and copy")
                    cmds.polyUVSet(obj, delete=True, uvSet=uv_set)
            cmds.deleteUI(prgoressWindow)
            cmds.waitCursor(state=False)
    #All name deleted________________________________________________________________________
    def get_all_namespaces(self, iter_nsp=[":"]):
        for nsp in iter_nsp:
            yield nsp
            all_nested_nsp = cmds.namespaceInfo(nsp, listOnlyNamespaces=True) or []
            for nested_nsp in self.get_all_namespaces(iter_nsp=all_nested_nsp):
                yield nested_nsp

    def GcRemoveAllNamespaces(self, *args):
        default_namespaces = [":", "UI", "shared"]
        scene_namespaces = list(self.get_all_namespaces())
        for nsp in reversed(scene_namespaces):
            if nsp in default_namespaces:
                continue   
            try:
                cmds.namespace(removeNamespace=nsp, mergeNamespaceWithRoot=True)
            except:
                cmds.warning("No deleted")
    #endregion
