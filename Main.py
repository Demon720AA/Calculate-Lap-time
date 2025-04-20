"""main"""
import CalculatorResult
def main():
    '''main'''
    name = input("Name : ")
    nameList = []
    timeList = []
    while name != "":
        time = input("Time : ")
        nameList.append(name)
        timeList.append(time)
        CalculatorResult.check(nameList, timeList)
        name = input("Name : ")
    # print(nameList)
    # print(timeList)
    name_time = CalculatorResult.sort(nameList, timeList)
    print(name_time)
main()
