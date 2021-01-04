def yearList(numFile):
    dataFile = open(numFile, "r")
    numbers = []
    remaining = []
    with dataFile: 
        for line in dataFile:
            line = line.strip('\n')
            numbers.append(line)
#1
    for number in numbers:
        number = int(number)
        num = 2020-number
        num = str(num)
        if num in numbers:
            print num
#2
     for number in numbers:
        for num in numbers:
            sum2 = int(number)+int(num)
            if sum2 < 2020:
                for n in numbers:
                    if (sum2+int(n))==2020:
                        print(int(n)*int(num)*int(number))
                        # print(num)
                        # print(number)
        

yearList("C:/Users/Dhyuti/Documents/CY300/input.txt")