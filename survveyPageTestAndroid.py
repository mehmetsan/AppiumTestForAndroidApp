from appium import webdriver

desired_cap={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "",
    "appWaitActivity": "",
    "app": "C:\\Users\\MehmetSanisoglu\\Downloads\\SITE.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

#INPUT VARIABLES FROM THE FILE
nameIn = surnameIn = birthDateIn = cityIn = genderIn = occupationIn = ""

#SIMPLE METHOD TO SEPERATE WORDS IN A LINE
def seperateWords(line):
    listOfWords = []
    word = ""
    for each in line:
        if(each == '/' and each != "\n"):
            listOfWords.append(word)
            word = ""
        else:
            word += each

    listOfWords.append(word.replace('\n','')) #ADD THE LAST WORD
    return listOfWords

testCases = open("testCases.txt","r")

#TEST EACH TEST CASE
for case in testCases:
    values = seperateWords(case)

    problem = values[0]
    nameIn = values[1]
    surnameIn = values[2]
    birthDateIn = values[3]
    cityIn = values[4]
    genderIn = values[5]
    occupationIn = values[6]


    # SEND KEYS
    fName = driver.find_element_by_id()
    fname.send_keys(nameIn)

    sName = driver.find_element_by_id()
    sName.send_keys(surnameIn)

    bDate = driver.find_element_by_id()
    bDate.send_keys(birthDateIn)

    city = driver.find_element_by_id()
    city.send_keys(cityIn)

    gender = driver.find_element_by_id()
    gender.send_keys(genderIn)

    occupation = driver.find_element_by_id()
    occupation.send_keys(occupationIn)


    driver.implicitly_wait(3)   #WAIT FOR THE SEND BUTTON TO APPEAR

    send = driver.find_element_by_id()
    send.click()
