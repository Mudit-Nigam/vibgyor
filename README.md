# vibgyor
Blind/ Partially Blind people can read only by audio books, Braille or with the help of a personal assistant. The scope of this project is to provide technical solution to assist the visually impaired people to access various text resources and making them independent. This enables the visually impaired people to identify the objects and written to the text written on it easily.
                             The program captures the image placed in front of the camera of mobile using droidcam. The image is converted to grayscale image and the number of contours are identified, which helps to determine the shape. Color is identified using KNN,trained on image data set. It uses an automatic document reader for visually impaired people , using pytesseract library. 
                               For shape, piano notes are produced, by which shape can be identified. For color, Guitar chords are produced at 2 levels-basic (basic colors),advanced(basic +extra colors),by which color of the object can be identified . It uses the Optical Character Recognition technology for the conversion of scanned images of printed text or symbols into text or information that can be understood or edited using a computer program. The text is converted into the audio output (Speech) through the use of OCR and Text-to-speech synthesis.

Technologies Used:     
Scripting Language: Python      
Libraries Used: Pytesseract,OpenCV,Numpy,PyGame,Pillow     
Algorithm :	K-Nearest Neighbours     
Third Party apps:	DroidCam    
