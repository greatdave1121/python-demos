import time, sys

indent = 0
indent_increasing = True

while True:
    try:
        print(" "*indent, end="")
        print("*********")
        time.sleep(0.1)

        if indent_increasing:
                indent += 1
                if indent == 20:
                        indent_increasing = False
        
        else:
            indent -= 1
            if indent == 0:
                   indent_increasing = True
    except KeyboardInterrupt:
          sys.exit()






    