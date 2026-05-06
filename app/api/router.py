from fastapi import APIRouter, UploadFile, File

from app.schemas.report import Report_Response, Indicator
from app.services.parser import parse_report_mock


router = APIRouter()

@router.post("/upload", response_model = Report_Response, summary="上传并解析体检报告")
async def uploda_report(file: UploadFile = File(...)):
    """
    接收用户文件
    """

    content = await file.read()

    extracted_data = await parse_report_mock(content, file.filename)

    indicators = [Indicator(**item) for item in extracted_data]

    return Report_Response(
        file_name = file.filename,
        message="文件上传解析成功",
        indicators = indicators 
    )