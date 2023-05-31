from tool_function import get_day_str , check_folder
import tempfile
import zipfile
import os
import shutil
from fastapi import FastAPI, UploadFile, File, Response
app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    foldername = "./outfolder/{}".format(get_day_str())
    check_folder(foldername)
    filename = "{}/{}".format(foldername,file.filename)
    with open(filename,"wb") as f:
        f.write(contents)
    return {"filename": file.filename}

@app.get("/download")
async def download_folder(folder_name: str, response: Response):
    temp_zip_path = f"outzip/{folder_name}.zip"
    with zipfile.ZipFile(temp_zip_path, "w") as temp_zip:
        shutil.make_archive(f"outzip/{folder_name}", "zip", f"outfolder/{folder_name}")

    response.headers["Content-Disposition"] = f"attachment; filename={folder_name}.zip"
    response.headers["Content-Type"] = "application/octet-stream"

    with open(temp_zip_path, "rb") as temp_zip:
        response.body = temp_zip.read()

    # Xóa tệp tạm thời sau khi tải xuống hoàn tất
    # os.remove(temp_zip_path)
    response.status_code = 200
    return response