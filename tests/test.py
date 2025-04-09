import pytest
from fastapi.testclient import TestClient
from main import app


# 建立測試客戶端
client = TestClient(app)

# ✅ 測試 /project/gen_number/ 正常情境
def test_gen_number_success():
    response = client.get("/project/gen_number/", params={
        "first_char": "A",
        "gender": "M"
    })

    assert response.status_code == 200
    data = response.json()
    assert "result" in data or isinstance(data, dict)
