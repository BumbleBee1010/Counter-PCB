# Counter PCB
Counter PCB is a project that sits on a custom designed PCB. The PCB involves a Seeed Xiao ESP32 C6 as it's powerhouse, a 1.3 inch I2C OLED sh1106 display, 4 MX switches, a 5mm round LED and a 1k resistor for it. I positioned the components, so that the screen at the top, buttons in a arrow shape and the microcontroller and LED/resistor is 'flanking' them on either side.
### My Goal
My goal for the project is for it to act a counter. The two centre MX switches adjacent to each other will be for + and -  and the right hand side MX switch will be for reset and the left hand side MX switch will be used to change the increment of addition/ subtraction. The counting and outputs will all be displayed on the screen.
<img width="1025" height="720" alt="image" src="https://github.com/user-attachments/assets/78e27134-b328-4e57-8541-94cb9fadcfa6" />

### Wiring
My project started with learning how to use EasyEDA and PCB designing. The sh1106 OLED I2C display is connected to pin d4 and d5 which hands I2C management in the microcontroller. Each MX switch is connected to its own gpio port, and ground. the LED is connected to  resistor to make sure the power doesn't spike and the LED burn out. At first when I was wiring, I uses actual wires, however when I added more and more components it got slighlty messy so I resorted to net labels.
As I went through the process I made some mistakes and had to do some trouble shooting. 

### PCB images
<table>
  <tr>
    <td valign="top"><img width="100%" alt="PCB Layout" src="https://github.com/user-attachments/assets/84f7fa62-bbac-49b8-b46f-18ca4e1d45ff" /></td>
    <td valign="top"><img width="850" height="710" alt="image" src="https://github.com/user-attachments/assets/debdc19e-8499-46b1-b24e-9ef2da9c99c4" />

  </td>
  </tr>
</table>

### Coding
I have also done some basic MicroPython code which show where each GPIO pin is connected to and write some basic text to the screen. I did some software logic which configured the button inputs and used the sh1106 driver to be able to display basic text. I used Micro Pico libary on VSCode.

### BOM
I have also done the pricing for the components and it put it slightly below the budget. However coupons and other discount promotions may lower this more.
<img width="1200" height="900" alt="image" src="https://github.com/user-attachments/assets/b62f9759-7daf-4c59-94bf-288b6eaa8abe" />

