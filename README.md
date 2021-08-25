Publication: New mouse models for high resolution and live imaging of planar cell polarity proteins in vivo.

## CellViewer for 2D Segmentation of Images (Latest Release 2.0)

Documentation on running the 2D cell segmentation tool, CellViewer. 

### Download and Install

URL: ```smb://lowrie.princeton.edu/molbio3/labs/devenportlab/DDLab_Members_Current/Abhishek/CellViewer```

1.	Download and unzip the files above based on the operating system of preference. 

2.  Let us assume that the unzipped path on the filesystem is PATH. This is the install path. 

### Data Processing 

1. Convert the image from the microscope into a single channel 8-bit greyscale image in TIF or PNG format using Fiji. 

2. This program works with only one of the frames of the z-stack. Please pick the one that is of interest. 

### How to Run  

Prerequisites: MATLAB > 2019b

Running a single image segmentation to pick the best Model and post-processing parameters: 

1.  On MAC OSX grant permission for the app to run. To grant permissions launch the ```Terminal``` app from Launchpad and execute the following commands:
    ```
    cd PATH
	chmod a+x test_single.exe
    ```

2.  Double click and run ```CellViewer_App.mlapp```.

3.	In the selector text box below the whole “Batch Processing Panel” click the button “Browse Image”. It will open a file selection dialogue box. 

4.	Select the image of choice and select the “Model” from the dropdown menu on the right panel. Here for IFE images please select the only IFE model available.

5.	Click the button “Single Segment” to start segmentation. The “Process Log” will show when the segmentation is complete. 

6.	Adjust other input parameters such as “Local Threshold Window”, “Border Size”. Click “Update” to see the changes in the mask. 


After the first single image segmentation to fix the parameters, perform a batch processing:  

1.	Click on the “Browse Dir” button in the “Batch Processing Panel”. It will open a file selection dialogue box . Select a folder that contains TIF images. It won’t show the files.

2.	Click on “Batch Segment” to start the segmentation using the parameters in the “Input Parameters” in the right hand side panel. 

3.	The “Process Log” will show when the segmentation is complete. 

All the output is stored in a format compatible with Tissue Analyzer and can be opened in TA for further analysis. 

