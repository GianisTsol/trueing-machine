# Turing machine

A simple turing machine code interpreter.

It was made by abusing yaml and interpreting it as
a language. Cool right?


# Syntax explanation
  ## Blocks
   A block can be used for loops
   or other repetitive work.
   
   You need to have a `main:` at the start of your
   script, thats where execution starts.
   Blocks need no ident (should be placed at the start of a line)
     
   You can move the execution point to another block with the action `goto: *block name*`.
   
   
   See example to understand.
  
  ## Actions
   ### Read
    read:
      1:
        # Do stuff if head reads one
      0:
        # Do stuff if head reads zero
   ### Write
    write: *value* # 1 or 0
      # Write only takes one argument (1 or 0). Anything else
      # in its context will be ignored.
   ### Move
     move: *direction* # right or left
      
   ### IMPORTANT!
    Capitalization matters!!
