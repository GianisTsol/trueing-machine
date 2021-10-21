# Turing machine

A simple turing machine code interpreter.

It was made by abusing yaml and interpreting it as
a language. Cool right?


# Syntax explanation

  ## Functions
   ### Read
    read:
      1:
        # Do stuff if head reads one
      0:
        # Do stuff if head reads zero
   ### Write
    write:
      *value* # 1 or 0
      # Write only takes one argument (1 or 0). Anything else
      # in its context will be ignored.
   ### Move
     move:
      *direction* # right or left
      
   ### IMPORTANT!
    Capitalization matters!!
