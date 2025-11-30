---
title: CPU
summary: The arithmetic & logic unit of my CPU.
year: 2025
tags:
    - Electronics
    - Digital Making
    - Soldering
    - Logic
---
# ALU
*2025 - Aged 14*
![An image of my ALU](images/cpu_alu.png)
*An image of my ALU*
## Overview
Doing maths is one of the main purposes of a CPU, and the ALU (Arithmetic and Logic Unit) is the bit that actually does it. As with the rest of my CPU, this is less powerful than most modern ones. It has 4 modes, add, subtract, NOR, and right shift (divide by two, ignore any remainder). I am making it on 2 breadboards: the top one to show the inputs, output, and setting, as well as switching between modes, and the bottom one to actually do the maths. The top breadboard has 26 LEDs on it, and will have 2 8-bit 2:1 multiplexers. The bottom one has 2 quad-XOR gates, 2 4-bit adders and 2 quad-NOR gates. The right shift is simply connecting the inputs to the output in a different place.

## The LEDs
This was a simple part. All I had to do was solder down a whole load of green and blue LEDs, some resistors and some wires. Despite this, I still came across a few issues when prototyping. The current-limiting resistors I used were 470R resistors, which pulled too much current and so the chips to actually use the data sometimes didn't have enough current to know if it was a 1 or a 0. This meant the built-in pull-up resistors took over and the actual data was ignored. I fixed this by using 10kR resistors instead.

## Adding and Subtracting
I used 4 chips for this, 2 adders and 2 XOR chips. Adding 2 numbers is simple: just feed them into the adders (I do know how the adders actually work, but making my own would be too expensive). Subtracting is harder, as you have to negate the second number and then add them together. This is essentially just doing 5 + -3 instead of 5 - 3. In binary, negative numbers are expressed in two's complement, which you convert into by inverting all of the bits and adding 1. I accomplished this by using a single subtract signal (this is actually the least significant bit of the setting as the setting for add is 00, so it won't subtract, subtract is 01 so it will subtract, and the other two don't matter as they won't use the adders anyway). The subtract signal is XORed with all of the data bits for the second number, as any number XOR 0 is itself, and any number XOR 1 is itself inverted. The subtract signal then also goes to the carry in of the first adder, so it will add one. This setup means that the second number will always go through the XOR gates, simplifying the wiring even if it does make the logic more complex.

## NOR Operation
This was a simple bit, as I just connected the inputs of the ALU to the inputs of the NOR gates. I came across no problems, and it was straightforward.

## Right Shift
I haven't done this yet, as it will be very simple. I don't have the multiplexers yet so I have to wait to connect the inputs to one.

## Mode Selection
I haven't actually made this yet, but I have the logic all worked out. It needs 2 8-bit 2:1 multiplexers. The first one chooses between the NOR and right shift operation, and the control bit is the least significant bit of the setting. If it is 0 (in NOR or ADD), then the multiplexers will choose the NOR output and the adders will add. If it is 1 (in RSH or SUB), they will choose the right shift output and the adders will subtract. We now have 2 8-bit numbers, one from the NOR/RSH and one from the adders. The most significant bit of the setting decides this one. If it is 0 (in ADD or SUB), the multiplexers will choose the adders. If it is 1 (in NOR or RSH), they will choose the output from the first multiplexers. The output of these multiplexers will go straight to the output LEDs.

## Challenges
I didn't come across many challenges (yet) when making this. The main one was the weak resistors pulling all of the current so the chips registered a high input, but this was easily fixed. I still have the multiplexers to add though, so I may come across more problems.