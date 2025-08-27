"""Bitmap Message through a Multiline String
Displays a text message according to the provided bitmap image.
Gets input as string and present it as a bitmap message reprsenting world map.
Tags: tiny, beginner, artistic"""

import sys

#(!) We can change this multiline string to any image we like:

#There are 68 periods along the top and bottom of this string:


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
....................................................................."""

print('Bitmap Message')
print("Enter the message to display with the bitmap.")
message = input('> ')
if message == '':
    sys.exit()

#Loop over each line in the bitmap:
for line in bitmap.splitlines():
    #Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == " ":
            #Print an empty space since there's a space in the bitmap:
            print(' ', end = '')
        else:
            #print a character from the message:
            print(message[i % len(message)], end = "")
    print()
