This was an attempt at programmatically transplanting code between the 68k
MainCode parts of different Macintosh ROMs. The idea was to help clarify the
important features of the NewWorld images that refuse to boot my Mac mini.

It works only for GoNative (the ROM Code Fragment Manager), although there is
some reusable supporting code. This is likely a dead end, but I thought I'd
share some insights that I have gained into the ROM-patching problem.

Matching the commonly called and rarely changed ROM glue code (GetHandleSize
etc) is easy, but other functions are very hard. I considered using a known-good
ROM disassembly and generating regular expressions that would match only the
major opcodes of a given function.

Closely coupled functions can have subtle but catastrophic incompatibility at
the binary level, e.g. in struct layouts.

You need to decide whether to patch a function's callers or place a BRA.L in the
function itself. Then, you need to decide where and how control will return to
the original ROM.
