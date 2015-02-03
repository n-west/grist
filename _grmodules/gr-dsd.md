---
title: gr-dsd
author: argilo
description: Digital Speech Decoder (DSD) blocks
type: Blocks
repo: https://github.com/argilo/gr-dsd.git
mirror: http://vanilla.ceat.okstate.edu/cgit/cgit.cgi/gr-dsd
layout: gr_module
---

The block expects 48000 samples per second input, and outputs sound at
8000 samples per second.  The input should be FM-demodulated (for
example, with GNU Radio's Quadrature Demod block) and should be between
-1 and 1 while receiving digital signals.  (A quadrature demod gain of
1.6 works well for me for EDACS Provoice.)  The input signal should
also be free of DC bias, so make sure you are tuned accurately, or
filter out DC.

To save CPU cycles, the block detects when the input is zero and avoids
sending it through DSD.  Thus it helps to put a squelch block before
gr-dsd, especially if you're using many copies of gr-dsd in parallel.
