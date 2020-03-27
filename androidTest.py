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

driver.implicitly_wait(2)

email = driver.find_element_by_id("com.sand.airmirror:id/etAccount")
email = email.find_element_by_class_name("android.widget.EditText")
email.send_keys(("trabzonpower@gmail.com"))

password = driver.find_element_by_id("com.sand.airmirror:id/etPwd")
password = password.find_element_by_class_name("android.widget.EditText")
password.send_keys("northern61")

btn = driver.find_element_by_id("com.sand.airmirror:id/btnLogin")
btn.click()

driver.implicitly_wait(4)


popUp = driver.find_element_by_id("com.sand.airmirror:id/tvCancel")
popUp.click()
