successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Sent")
        break
else:
    print("Not Sent")

print("Done")
