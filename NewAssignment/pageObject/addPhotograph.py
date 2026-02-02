import page


class AddPhotograph:

    def __init__(self, page):
        self.page = page


    def addPhotograph(self):
       uploadImg=self.page.locator("input[type='file']")
       uploadImg.set_input_files("data/testImage.jpg")
       self.page.get_by_role("button",name="Save").click()
