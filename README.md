# Counter PCB
Counter PCB is a project that sits on a custom designed PCB. The PCB involves a Seeed Xiao ESP32 C6 as it's powerhouse, a 1.3 inch I2C OLED sh1106 display, 4 MX switches, a 5mm round LED and a 1k resistor for it. 
<img width="1025" height="720" alt="image" src="https://github.com/user-attachments/assets/78e27134-b328-4e57-8541-94cb9fadcfa6" />

### Wiring
My project started with learning how to use EasyEDA and PCB designing. The sh1106 OLED I2C display is connected to pin d4 and d5 which hands I2C management in the microcontroller. Each MX switch is connected to its own gpio port, and ground. the LED is connected to  resistor to make sure the power doesn't spike and the LED burn out. At first when I was wiring, I uses actual wires, however when I added more and more components it got slighlty messy so I resorted to net labels.
As I went through the process I made some mistakes and had to do some trouble shooting. When I finished the schematic, I went on to positon the components, the screen at the top, buttons in a arrow shape and the microcontroller and LED 'flanking' them on either side, as you can see in the image below.

### PCB images
<table>
  <tr>
    <td valign="top"><img width="100%" alt="PCB Layout" src="https://github.com/user-attachments/assets/84f7fa62-bbac-49b8-b46f-18ca4e1d45ff" /></td>
    <td valign="top"><img width="100%" alt="3D View" src="https://github.com/user-attachments/assets/1d7c1d7d-aa60-45ae-a731-312a447c9ab4" /></td>
  </tr>
</table>

### Coding
I have also done some basic MicroPython code which show where each GPIO pin is connected to and write some basic text to the screen. I did some software logic which configured the button inputs and used the sh1106 driver to be able to display basic text. I used Micro Pico libary on VSCode.

### BOM
I have also done the pricing for the components and it put it slightly below the budget. However coupons and other discount promotions may lower this more.
<img width="1187" height="960" alt="image" src="https://github.com/user-attachments/assets/7ac4753e-5d9f-48a4-b167-6bff3791e34e" />

(a picture is worth a thousand words)
