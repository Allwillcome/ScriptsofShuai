import requests

def send_message(api_url, message_type, content, source, is_mentioned="0", is_msg_from_self="0"):
    data = {
        "type": message_type,
        "content": content,
        "source": source,
        "isMentioned": is_mentioned,
        "isMsgFromSelf": is_msg_from_self,
    }

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        return response.json()
    return None

# 示例调用
if __name__ == "__main__":
    api_url = "http://0.0.0.0:1219/receive/"
    message_type = "text"
    content = "你好"
    source = '{"room":"","to":{"id":"@f387910fa45","payload":{"alias":"","avatar":""}},"from":{"id":"@6b5111dcc269b6901fbb58","payload":{"city":"Mars","name":"Daniel"}}}'
    response = send_message(api_url, message_type, content, source)
    print(response)