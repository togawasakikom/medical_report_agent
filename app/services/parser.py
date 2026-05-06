async def parse_report_mock(file_bytes: bytes, filename: str):
    """
    这里写一个解析完成后模拟数据的函数
    之后接入pdfplumber和pandas真的处理数据逻辑
    """

    # 打印日志假装处理文件

    print(f"正在解析：{filename}, 文件大小:{len(file_bytes)}字节")

    # 模拟从 PDF/Excel 中提取出的结构化数据
    mock_data =[
        {
            "name": "白细胞计数", 
            "value": 5.2, 
            "unit": "10^9/L", 
            "reference_range": "3.5-9.5", 
            "status": "正常"
        },
        {
            "name": "空腹血糖", 
            "value": 6.8, 
            "unit": "mmol/L", 
            "reference_range": "3.9-6.1", 
            "status": "偏高"
        },
        {
            "name": "总胆固醇", 
            "value": 6.1, 
            "unit": "mmol/L", 
            "reference_range": "3.1-5.17", 
            "status": "偏高"
        }
    ]
    
    return mock_data