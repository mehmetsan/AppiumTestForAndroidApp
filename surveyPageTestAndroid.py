from appium import webdriver
import os

#SIMPLE METHOD TO SEPERATE WORDS IN A LINE
def seperateWords(line):
    listOfWords = []
    word = ""
    for each in line:
        if(each == '+' and each != "\n"):
            listOfWords.append(word)
            word = ""
        else:
            word += each

    listOfWords.append(word.replace('\n','')) #ADD THE LAST WORD
    return listOfWords

desired_cap={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.example.surveypage",
    "appWaitActivity": "com.example.surveypage.MainActivity",
    "app": os.getcwd() + "\\surveyApp.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

#INPUT VARIABLES FROM THE FILE
nameIn = surnameIn = birthDateIn = cityIn = genderIn = occupationIn = ""
testCases = open("testCases.txt","r")

#TEST EACH TEST CASE
for case in testCases:
    fName = driver.find_element_by_id("com.example.surveypage:id/name_text")
    sName = driver.find_element_by_id("com.example.surveypage:id/surname_text")
    bDate = driver.find_element_by_id("com.example.surveypage:id/date_text")
    city = driver.find_element_by_id("com.example.surveypage:id/city_text")
    gender = driver.find_element_by_id("com.example.surveypage:id/gender_spinner")
    occupation = driver.find_element_by_id("com.example.surveypage:id/occ_text")

    values = seperateWords(case)

    problemDefinition = values[0]     #USED IN TESTING ONLY
    nameIn = values[1]
    surnameIn = values[2]
    birthDateIn = values[3]
    cityIn = values[4]
    genderIn = values[5]
    occupationIn = values[6]

    # SEND KEYS
    fName.send_keys(nameIn)
    sName.send_keys(surnameIn)
    bDate.send_keys(birthDateIn)
    city.send_keys(cityIn)
    gender.click()
    driver.implicitly_wait(2)       #WAIT FOR THE GENDERS TO APPEAR
    if(genderIn == "Male"):
        genderSelect = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]")
        genderSelect.click()
    elif(genderIn == "Female"):
        genderSelect = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
        genderSelect.click()
    else:
        genderSelect = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[3]")
        genderSelect.click()
    occupation.send_keys(occupationIn)


    driver.implicitly_wait(5)   #WAIT FOR THE SEND BUTTON TO APPEAR

    try:
        send = driver.find_element_by_id("com.example.surveypage:id/send")
        send.click()
    except:
        occupation.clear()
        gender.click()
        genderSelect = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[1]")
        genderSelect.click()
        city.clear()
        bDate.clear()
        sName.clear()
        fName.clear()


    driver.implicitly_wait(4)   #WAIT FOR THE RESULT TO BE SEEN
