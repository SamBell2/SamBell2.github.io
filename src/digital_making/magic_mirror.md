---
title: Magic Mirror
summary: A magic mirror
year: 2023
tags:
    - Digital Making
    - 3D Printed
    - Raspberry Pi
    - Graphical Interfaces
---
# Magic Mirror
*2023-2025 - Aged 12-14*
![An image of my magic mirror](images/magicmirror.png)
## Overview
A magic mirror is a mirror that has text and possibly images displayed on it. They typically work with a 2-way mirror where you can see through it as well as the reflection, and then just placing a screen behind it. I got the inspiration to make one from the [MagPi issue #93](https://magazine.raspberrypi.com/issues/93){target="_blank" rel="noopener"}, where they finished a guide on creating your own. This project involved learning a new programming language, 3D CAD, API calls and Linux setup.
***
## Electronics
I chose a Raspberry Pi here because it made it simple to run a display, had a full Linux OS and I already knew how to use them. I got a Raspberry Pi Touch Display which was very much overkill as once the project's completed, you are never going to touch it (it'll be behind a mirror), but I already had one so decided to use it. I then just got a Raspberry Pi 3, connected it to the screen, and moved on to software.
***
## Software
First, I got the [MagicMirror²](https://magicmirror.builders/){target="_blank" rel="noopener"} software installed and set up. By default, it had a few useful modules installed, such as the time and the weather, but I also decided to change most of them. I removed the 'compliment' module, because the screen I used was too small, and then found a few other ones online that I liked. Once I had finished customising the display, the modules I had were:  

* [Clock](https://docs.magicmirror.builders/modules/clock.html){target="_blank" rel="noopener"}
* [Weather](https://docs.magicmirror.builders/modules/weather.html){target="_blank" rel="noopener"}
* [News Feed](https://docs.magicmirror.builders/modules/newsfeed.html){target="_blank" rel="noopener"}
* [Facts](https://github.com/alanshen111/MMM-Facts){target="_blank" rel="noopener"}
* [Weather Effects](https://github.com/cgillinger/MMM-WeatherEffects){target="_blank" rel="noopener"}
* [Advent Calendar](https://github.com/Jopyth/MMM-Advent){target="_blank" rel="noopener"}

I left it at this stage for a few months, then I decided to go a step further. I learnt how to program in JavaScript, then discovered how to use the MagicMirror² API to create my own modules. The first one I made gave you a random Pokemon each day, similar to [this one](https://github.com/NolanKingdon/MMM-DailyPokemon){target="_blank" rel="noopener"} but with less information. I made a few more small ones, but I haven't yet made a big one as the case problems put me off this project.
***
## Case
Surprisingly, this was the bit that took the longest. I measured the precise dimensions of the glass and the screen, and designed a case that would fit it perfectly. I then 3D printed it, which took almost 24 hours to complete, but when I tested it, it didn't fit! I had designed it to fit the mirror so neatly that the printer squishing the plastic as it moved made it too narrow! This put me off 3D printing far more than it should, and I just put the mirror in a shoebox and forgot about it for a year. Recently (late 2025), I rediscovered it and made a new case for it using a simple trick I learnt when making my [Light Fantastic](light_fantastic.md), where you increase the capacity of the case by a few mm in each direction. I printed it again (in 2 parts as the first one failed near the end) and it worked really well.
***
## Challenges
The most challenging part was making the case, as when I first designed it, I forgot to account for the printer's tolerance, so the mirror simply would not fit. At first, I wasn't sure why this happened, but I eventually measured the dimensions of the inside of the case and found that they were about a millimeter too small. In addition, creating my own modules for the mirror meant that I had to learn a whole new language first, as I had only touched JavaScript a few times before, and now I needed to learn DOM modelling, external API access, timeouts, status codes and a whole load more.
***
## What I Learned
* How two-way mirrors work in display projects
* Setting up and configuring Linux-based systems
* Customising and extending existing open-source software
* Writing JavaScript modules using an existing API
* Designing 3D-printed parts with appropriate tolerances
* Learning from failed designs and improving them through iteration