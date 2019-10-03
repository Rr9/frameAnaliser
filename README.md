# frameAnaliser
Go though frame by frame of a video and analyze brightness values of each frame and print them to a file.

I basically made this really quickly to see if the brightnes of the frames in the movie Perfect Blue went down as the movie progressed. 
Turns out the overall values goes down but its not linear.

1. Turn every frame to greyscale 
2. Average all pixel values in the frame
3. Output all values to file 
4. TODO: Graph the values with numpy
