#---------------------------------------------------------------------------------------------------------#
"""                                             GUITAR INSTRUMENT                                        """
#---------------------------------------------------------------------------------------------------------#
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import lfilter

#-----------------------------------------Basic constant -----------------------------------------------
FS       = 44100
A        = 110 
E_OFFEST  = -5  
D_OFFEST  = 5
G_OFFEST  = 10
B_OFFEST  = 14
E2_OFFEST = 19

#------------------------------------------------------------------------------------
Freq= np.linspace(1/FS, 1000, 2**12)
input=np.zeros((FS*4, 1))
#----------------------------- zero list func ----------------------------
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
#-----------------------------create note ---------------------------------
def CreateNote(string,Delay):
    Numerator = signal.firls(43, [0 ,1/Delay, 2/Delay ,1], [0 ,0 ,1, 1] )
    list =zerolistmaker(int(Delay))
    list   = [1]+list+ [-0.5 ,-0.5]
    Denominator =np.array(list)

    zi = np.random.rand(max(len(Denominator ),len(Numerator))-1,1)

    note,z0 = lfilter(Numerator,Denominator , input,axis=-2,  zi=zi)
    note = note-np.mean(note)
    note = note/max(abs(note))
    sd.play(note ,FS)
    sd.wait()

#------------------------------------------create a fret string ----------------------------------
def CreateFretNote(string,fret):
    delay = np.round(FS/(string*2**(fret/12)))
    CreateNote(string,delay)
#-------------------------------------------create open string note -------------------------------
def createopenNote(string):
    Delay= np.round(FS/string)
    CreateNote(string,Delay)

#------------------------------------------create chord ----------------------------------------
def CreateChord(fret):
    delay =[np.round(FS/(A*2**((fret[0]+E_OFFEST)/12))),np.round(FS/(A*2**(fret[1]/12))),np.round(FS/(A*2**((fret[2]+D_OFFEST)/12))), np.round(FS/(A*2**((fret[3]+G_OFFEST)/12))),np.round(FS/(A*2**((fret[4]+B_OFFEST)/12))),np.round(FS/(A*2**((fret[5]+E2_OFFEST)/12)))]
    note = np.zeros((len(input),len(delay)))
    indx=0
    Denominatorarray=[]
    Numeratorarray=[]
    notearray=[]
    while indx<len(delay):
        Denominator = signal.firls(43, [0 ,1/delay[indx] ,2/delay[indx], 1], [0, 0 ,1 ,1])
        Numerator = [1] +zerolistmaker(int(delay[indx])) +[-0.5 ,-0.5]
        Numerator=np.asarray(Numerator)
        Denominatorarray.append(Denominator)
        Numeratorarray.append(Numerator)
        zi =np.random.rand(max(len(Denominatorarray[indx]),len(Numeratorarray[indx]))-1,1)
        note,zo = lfilter(Denominatorarray[indx], Numeratorarray[indx],input,axis=-2, zi=zi)
        note = note-np.mean(note)
        notearray.append(note)
        indx+=1

    notearray=np.asarray(notearray)    
    combinedNote = sum(notearray,2)
    combinedNote = combinedNote/max(abs(combinedNote))
    sd.play(combinedNote, FS)
    sd.wait()









#*******************************************************************************************************#
'''                                         PIANO INSTRUMENT                                          '''
#********************************************************************************************************#



def piano_key(  string ):
    duration=3
    each_sample_number = np.arange(duration * FS)
    waveform = np.sin(2 * np.pi * each_sample_number * string/FS )*np.exp(-0.0004*2*np.pi*string*each_sample_number/(FS/5))
    sd.play(waveform,FS)
    sd.wait()







#------------------------------------------------------------------------------------------------#
"""                                           THE END                                           """
#------------------------------------------------------------------------------------------------#
