======================================
Mobile Robotics Lab Student
======================================

Installation Steps: 
(ONLY FOR WINDOWS MACHINES. 
Linux and macOS are not currently supported.)
--------------------------------------------------

1. The setup requires Python. If a compatible version is not installed, 
   the user will be prompted to install it from the provided installer 
   (in which case please ensure to check the 'Add python.exe to PATH' option). 

2. Make sure your machine is connected to the internet. 

3. ON YOUR MACHINE RUN/DOUBLE CLICK ON setup.bat LOCATED IN THIS FOLDER.

4. Restart your machine for changes to be saved.

5. Read the software requirements below if you have more questions about the necessary
	downloads to run the content.
	
6. Go to the Welcome Guide in Documents/Quanser directory for guidelines and how to get started.

7. Go through the Quick Start Guide for the configuration you plan on using, i.e., QBot Platform 
   hardware or virtual twin for either Python or Simulink. 

Please contact Quanser customer success team (tech@quanser.com) regarding any questions or concerns with 
the setup process.


Notes:
-----------------------------------

WARNING: DO NOT CONNECT THE INTERNET CABLE DIRECTLY TO THE
	 PROVIDED ROUTER. THIS MAY CAUSE UNEXPECTED BEHAVIOR DUE TO
	 AUTOMATIC ROUTER FIRMWARE UPDATES.
Caution: If an internet connection is not available, the setup
	 process will proceed to finish offline. Python examples
	 might not function properly due to potentially missing
	 or incompatible libraries.

- The setup.bat script was designed to:
   - Install Python if not on your PC
   - Copy the content of src\ onto the local machine under the C:\Users\<USER>\Documents\Quanser directory
   - Define the PYTHONPATH variable on your system which points to custom
     Quanser python libraries within the src\libraries\python folder
   - Install the python dependencies required for users using python.


Software requirements:
-------------------

1. On your Windows development machine (PC or laptop),

    a. To interface to physical hardware, with or without virtual experiments, 
		i. If using MATLAB Simulink:
			- install MATLAB Simulink and QUARC as described in the QUARC Quick Installation Guide 
			(https://download.quanser.com/doc/latest/QUARC_Quick_Installation_Guide.pdf)

		ii. If using Python:
			- the installation of Python 3.11+ will be carried out when running setup.bat
			- if QUARC was not installed (as it's only needed if using MATLAB Simulink), 
				install the Quanser SDK for Windows. (https://github.com/quanser/quanser_sdk_win64)

	b. To interface to ONLY the virtual experiments,
		i. If using MATLAB Simulink, with or without Python:
			- install a version of MATLAB Simulink compatible with the Quanser Interactive Labs MATLAB Add-on  
			(https://www.mathworks.com/matlabcentral/fileexchange/123860-quanser-interactive-labs-for-matlab) 
			- install Quanser Interactive Labs for MATLAB using the Add-on Manager in MATLAB 
			  
		ii. If using ONLY Python:
			- the installation of Python 3.11+ will be carried out when running setup.bat
			- install both Quanser Interactive Labs and the Quanser SDK for Windows as described here  
			  (https://qlabs.quanserdocs.com/en/latest/Get%20Started.html#installation-set-up)



==========================================================================================================
Mobile Robotics Lab Student:
--------------------
src	 	  			: Source folder for files used by the Mobile Robotics Lab.
- user_manuals    	: User manuals related to the QBot Platform.
- quick_start_guides: Standalone Quick Start Guides for the QBot Platform. 
- concept_reviews 	: Consists of background concepts utilized in the provided curriculum.
- libraries	  		: Source location for custom Python/Simulink libraries.
- examples	  		: Consists of IO examples in either Simulink/Python for QBot Platform.
- Mobile_Robotics 	: Consists of the lab content for hardware/digital-twin, in both Simulink & Python
==========================================================================================================

==========================================================================================================
Change Log:
==========================================================================================================

Mobile_Robotics_Student_v1.2 (2024-07-31):
---------------------------------------------
- New Matlab QVL libraries for Quanser Interactive Labs. 
	(Files are updated to use these ones. Files from previous releases will stop working)
	These new libraries will make sure the python and matlab functions for QLabs are consistent. 
- Updated Labs fixing small issues and adding improved instructions.

Mobile_Robotics_Student_v1.0 (2024-03-19):
------------------------------------------
- First release adding lab content for the Play and Task Automation skills progression.
