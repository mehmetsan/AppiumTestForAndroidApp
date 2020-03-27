from appium import webdriver

desired_cap={
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.sand.airmirror",
    "appWaitActivity": "com.sand.airmirror.ui.guide.GuideActivity_",
    "app": "C:\\Users\\MehmetSanisoglu\\Downloads\\airmirror.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

button = driver.find_element_by_id("com.sand.airmirror:id/tvLogin")
button.click()
