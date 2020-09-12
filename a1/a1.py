import sys

# Read and parse .txt file
with open(sys.argv[1]) as text:
    lines = text.readlines()

# Create reference dictionary to count duplicates
dupDict = {}

# Check for and count repeated hex values in parsed file
for val in lines:
    strippedVal = val.lstrip("0").rstrip("\n")

    # Create base string if stripped down to an empty string
    if strippedVal == "":
        strippedVal = "0"

    hexVal = int(strippedVal, 16)

    if hexVal in dupDict:
        dupDict[hexVal] += 1
    else:
        dupDict[hexVal] = 1

# Print sorted duplicates and their count
for key in sorted(dupDict):
    if dupDict[key] > 1:
        hexKey = "%x" % key
        print(hexKey + " " + str(dupDict[key]))
