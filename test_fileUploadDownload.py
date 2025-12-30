import os
import time
from playwright.sync_api import Page, expect


def test_fileUploadDownload(page:Page):
    page.goto("https://demoqa.com/upload-download")
    file_path= "C:/Users/Daffolap-763/Downloads/test.pdf"
    page.set_input_files("#uploadFile", file_path)
    expect(page.get_by_text("test.pdf")).to_be_visible()


    with page.expect_download() as download_info:
        page.locator("#downloadButton").click()

    download = download_info.value
    download_path= "downloads/test.pdf"
    download.save_as(download_path)

    assert os.path.exists(download_path)
    time.sleep(3)

