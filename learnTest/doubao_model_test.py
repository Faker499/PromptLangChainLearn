# 导入依赖库
import requests
import json
import certifi
from urllib3.exceptions import InsecureRequestWarning

# 禁用调试阶段的SSL不安全请求警告，生产环境建议移除
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# ===================== 必填配置：替换为自己的信息 =====================
# 火山方舟 API-KEY
ARK_API_KEY = "30a5b927-bd88-4856-b55b-f053308b1852"
# 火山方舟 推理接入点ID（ep-开头，不是doubao-lite）
MODEL_EP_ID = "ep-20260327113106-tntgm"
# 火山方舟官方统一请求地址
API_URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
# =====================================================================

# 请求头配置
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {ARK_API_KEY}"
}

# 请求体：严格遵循火山方舟参数规范
data = {
    # 核心：填写ep-开头的接入点ID，严禁写doubao-lite
    "model": MODEL_EP_ID,
    "messages": [
        {"role": "user", "content": "你好，请简单介绍一下自己"}
    ],
    # 温度参数，0-1，值越小回答越精准稳定
    "temperature": 0.7,
    # 最大响应长度，可按需调整
    "max_tokens": 2000
}

# 发起请求，适配SSL与超时
try:
    response = requests.post(
        url=API_URL,
        headers=headers,
        data=json.dumps(data, ensure_ascii=False),
        timeout=60,
        # 调试用verify=False，生产环境建议改为 verify=certifi.where()
        verify=False
    )
    result = response.json()

    # 正常返回解析
    if response.status_code == 200 and result.get("choices"):
        answer = result["choices"][0]["message"]["content"]
        print("=" * 50)
        print("火山方舟模型回复：")
        print("=" * 50)
        print(answer.strip())
    else:
        print("=" * 50)
        print("调用失败，错误详情：")
        print("=" * 50)
        print(json.dumps(result, ensure_ascii=False, indent=2))

except Exception as e:
    print(f"请求异常：{str(e)}")
