# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:45:26 2023

@author: Administrator
Use: https://github.com/PolarBean/DeepSlice
to use together with abba 
"""

from DeepSlice import DSModel
import SaveFilesAsJpeg 

def deepslice(folderpath):
 

 # SaveFilesAsJpeg.call_class_to_Save(folderpath, output)
 
  species = 'mouse' #available species are 'mouse' and 'rat'

  Model = DSModel(species)

#here you run the model on your folder
#try with and without ensemble to find the model which best works for you
#if you have section numbers included in the filename as _sXXX specify this :)
  Model.predict(folderpath, ensemble=True, section_numbers=True)    
  
  #If you would like to normalise the angles (you should)
  Model.propagate_angles()                     
#To reorder your sections according to the section numbers 
  Model.enforce_index_order()    
#alternatively if you know the precise spacing (ie; 1, 2, 4, indicates that section 3 has been left out of the series) Then you can use      
#Furthermore if you know the exact section thickness in microns this can be included instead of None
#if your sections are numbered rostral to caudal you will need to specify a negative section_thickness      
  Model.enforce_index_spacing(section_thickness = None)
  

#now we save which will produce a json file which can be placed in the same directory as your images and then opened with QuickNII. 
  Model.save_predictions(folderpath + 'results')                    

def main():
    #folderpath = 'C:/Users/Administrator/AppData/Local/Temp/deepslice3196393059916875717/'
    folderpath = input('What is your folder path with your images? \n')
    #output ='X:/Users/Members/Tali S/aging project/p16 virus/p16 virus brain/p16 young/tif/plate1/ForAutomaticRegistration/your_brain_folder/'
    deepslice(folderpath )


if __name__ == '__main__':
    main()
    
    