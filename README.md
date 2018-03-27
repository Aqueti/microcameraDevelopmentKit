# microcameraPython
Python scripts and notebooks used with the Aqueti microcamera development kit

This repositoryy contains python scripts and Jupyter notebooks used in the course "Computational Photography" at Duke Kunshan University. These scripts run on Aqueti microcamera development boards.

"camera" contains scripts that should be installed on the camera platform. The default user name is ubuntu, the default password is also ubuntu.

"render" contains scripts that run on a remote computer connected via ethernet to the camera. Typically the camera IP address is set manually and the remote computer connects to the camera also via a manually set network interface. The interface works better if password-free login to the camera from the render is setup using ssh key exchange. One must use ssh-copy-id to place the appropriate ssh key on the camera.

"notebooks" contains jupyter-notebooks written in Python3 to explore various camera control functions.

"docs" contains interesting documents. 