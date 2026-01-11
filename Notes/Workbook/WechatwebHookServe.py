from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recvd_msg', methods=['POST'])
def recvd_msg():
    # 获取请求中的表单数据（按照前面提到的微信机器人发送消息过来的格式来解析）
    msg_type = request.form.get('type')
    content = request.form.get('content')
    source = request.form.get('source')
    is_mentioned = request.form.get('isMentioned')
    is_msg_from_self = request.form.get('isMsgFromSelf')

    # 这里可以添加你自己的消息处理逻辑，比如打印消息内容
    print(f"收到消息类型: {msg_type}，内容: {content}")

    # 简单返回一个表示成功接收的响应，实际应用中可按要求返回更完善的回复消息结构
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1219)