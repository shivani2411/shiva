putshi = input()
print(''.join([ putshi[x:x+2][::-1] for x in range(0, len(putshi), 2) ]))
