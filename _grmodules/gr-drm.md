---
title: gr-drm
author: KIT-CEL
description: Software DRM/DRM+ transmitter
type: Application
repo: https://github.com/kit-cel/gr-drm.git
mirror: http://vanilla.ceat.okstate.edu/cgit/cgit.cgi/gr-drm
layout: gr_module
---

This project features a DRM/DRM+ software transmitter fully integrated into GNU Radio Companion.

You are also free to play around with several robustness modes (RM) and spectrum occupancies (SO, signal bandwidth) ranging from 4.5 to 20 kHz. The corresponding bit rates vary from below 5 kbps to about 55 kbps. A configuration that is widely used is RM B (==1) and 10 kHz bandwidth (SO 3). Among other parameters, the station label and a text message can also be set by simply adapting the correspondant blocks' values.
