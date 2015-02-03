---
title: gr-dvbt
author: Bogdan
description: DVB-T encoder/decoder (ETSI 300 744)
type: Blocks
repo: https://github.com/BogdanDIA/gr-dvbt.git
mirror: http://vanilla.ceat.okstate.edu/cgit/cgit.cgi/gr-dvbt
layout: gr_module
---

The baseband samples can be sent to USRP N210 on TX and received with another USRP N210 on RX. The decoder/encoder consumes a lot of processing power and therefore the realtime functionality will depend on the available computing power. On my computer - i7 Sandybridge 2600K - it is possible to send and receive in realtime the stream.

The encoder/decoder currently works with gnuradio 3.7.2.x and 3.6 (if taken from Gnuradio_v_3_6 tag) but it is not dependent heavily on it. There is also a list of todo tasks in TODO.txt.

The dvb-t module requires SSE2 SIMD instructions available in the processor. If the SSE2 is not available then illegal instruction will be seen at runtime. 
