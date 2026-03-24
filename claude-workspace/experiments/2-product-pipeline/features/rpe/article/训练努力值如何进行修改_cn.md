我现在需要把 PeakWatch 的训练努力值的科普文章修改下，之前的科普文章链接为：https://doc.peakwatch.co/zh_cn/training-effort.html

修改的原因：是把这个指标升级为了 RPE。不是完全替换修改。

现在这个是叫做自觉耗能和苹果保持一致，对应的文件名也可以改一下吧。到时候前端把之前的科普文章的文件保留，供之前的老用户使用。

相关的 PRD 文档：

RPE 为 Rate of Perceived Exertion的全拼，翻译为主观自觉量表，代表一节课中的努力程度。

- 能够读取苹果健康的 RPE 数值（后续佳明也要考虑此数据）
- 在 PeakWatch 上发起的运动，会自动计算 RPE，此时用户可以修改 RPE，并写入到苹果健康（用户如果没有修改 RPE，就把默认计算的 RPE 写到苹果健康）
  - 包含训练结束后在手表上选择 RPE
- 在训练记录当中可以修改 RPE，修改后的 RPE 同步到苹果健康
  - 需要@杨爽 确认我们能否修改苹果的 RPE
  - 就是苹果健康里面的 RPE 和佳明里面的 RPE 保持实时
- RPE 是训练努力值的升级，适用于所有的训练记录
  - 如果用户没有主动填写 RPE 或者没有来自苹果健康的数据，则模式使用现在的计算逻辑，只是数值四舍五入保留整数
  - 如果用户有主动填写 RPE 或者有来自苹果健康数据，则显示对应的数值
- 对应训练努力值下方的评语要进行修改，贴在本文下方的 RPE 评语当中。
- 训练努力值得的科普文章

![img](/Users/wangshuaibo/Documents/配图/已使用/(null)-3386051.)

场景 1：RPE 数据读取自苹果健康

 1.1：苹果健康返回具体 RPE 数值 → 显示：「来自苹果健康」

 1.2：苹果健康无具体 RPE 数值，但训练努力值＞1 → 显示：「PeakWatch 基于心率数据推算」

场景 2：RPE 数据非来自苹果健康

  2.1：苹果健康无具体 RPE 数值，但训练努力值＞1 → 显示：「PeakWatch 基于心率数据推算」

  2.2：用户已手动调整 RPE 数值 → 显示任何 “来自手动输入”

场景 3: 不同数据源修改（需研发调研，GS都已实现）

​       3.1: 在2.1的情况下，用户通过苹果健康的运动结果页进行修改，PW的结果页也会同步新的苹果健康修改的数据结果

​      3.2: 反之，在3.1的情况下，用户通过PW进行修改，苹果健康的数据会更新为PW修改的数据

​      3.3:用户在PW「清除数据」，在PW显示无数据，在苹果健康内显示「已跳过」



相关解释：

| **无数据** | **无数据**   | 请填写本次训练的主观感受强度         | **No Data**           |                                                     | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=NTAzNDRhN2Q1OTg0YTc4NDkwZDJhZjcwNWU2ZmM2ZDRfYWMxcnJLSlFiSlVBbURkS2F0WElreXM1dHZJT05haUdfVG9rZW46QVNjM2I5VXdSbzJUczh4aGhhY2NjbUF2bnNjXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| ---------- | ------------ | ------------------------------------ | --------------------- | --------------------------------------------------- | ------------------------------------------------------------ |
| **1**      | **毫不费力** | 几乎无感，如进行呼吸训练。           | **Almost Effortless** | Barely noticeable, like breathing exercise.         | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmQ4YmY5OWQwZDU1NzM0NjQ4NDU1YTE4N2M3MTA3NzFfNm9sWnA4RlYzM1psM0lKVHFpb2VyN1MyT0dURklYSkZfVG9rZW46TW1HaWJJMGJDb1JTS3V4Wk9ZWmNNZnU2bmFlXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **2**      | **极轻强度** | 身体轻微活动，呼吸保持自然常态。     | **Extremely Light**   | Moving casually with natural, easy breathing.       | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=NGRiNmZiMzkyNTNmOGRlMTRiYzc0MTFlYjJjZTJlYzJfU0JBSHl6ZXFCeHRtR3lSbWhmTmNwTHlLaTF5MWExYlRfVG9rZW46RlRwaGJ4VG56b0Zobnd4cXFJeWNkMWdJbnVoXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **3**      | **较低强度** | 感到活动感，能轻松交谈且毫无压力。   | **Very Light**        | Feeling active, chatting away with zero stress.     | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=MmNhOWVlZDYyNWU1OGQ0Y2E5MWNlNTViYjQ5MDBlMmFfcWJ2T2psbVFxSWFYVHNkejdtbUpwMjFwRnB0RzJvYk5fVG9rZW46Q0NJbmJjSlBDb1NnUk54WXBkVmNuekJKbm9kXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **4**      | **低强度**   | 热身强度，身体微发热，呼吸节奏平稳。 | **Light**             | Warm-up pace, body warming up with steady breath.   | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2VhNDVhNGU1Y2M5MWU3Nzg4MmZhYzNiYjMxN2E1MjJfSjNoem15Z0IzakVORWpvQVV0Z2pOall0aGdVNmgySG5fVG9rZW46S3pudWIxcUEwb2JzcFV4NlN5OWN4Z1Rlbk5nXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **5**      | **中等强度** | 运动感明显，呼吸加速但仍能连贯说话。 | **Moderate**          | Clear effort, breathing faster but speech is fluid. | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTFmOWM0MTYxNmJiMzVlMGFjNDMwYjI1ODdiY2Q2YjJfNGZQM1RqOEhlbjRLMXB6ZUZnTjJSWnNpc3JCcFE3VEhfVG9rZW46V3pXVmJxTUphb3pLNGp4d2VoN2MxYlRpbk5oXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **6**      | **稍感疲劳** | 开始流汗，说话变得断断续续。         | **Tiring**            | Starting to sweat, conversation becomes broken.     | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=NzEyOTIxMWI5MGU0MjkwNWY5ZmQ2MmI4NzFjZGMyOWFfYWl3TTVxQ1NLd1ZsOWRZN3FkdVAyMjR3UDFOTDRqYTVfVG9rZW46RDhhQWJCY0Zjb25Mekh4SjBGTmNvbEFXbmpkXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **7**      | **颇具挑战** | 呼吸深沉，能简短交流但无法唱歌。     | **Challenging**       | Deep breathing, short phrases only, no singing.     | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQ3OTlmNjkxNzgzYTFjODA0NTAzZTU0Y2U1YWU5N2FfUWpmbkNQaHJVOFZGOGFRdzhmaGlxMmxlMWtiVGlURlVfVG9rZW46SDhSdGJWSHQ1b05wREp4V0xISmMxZ1Q3bnlnXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **8**      | **高强训练** | 感到吃力，难以开口说话，专注呼吸。   | **Hard**              | Strenuous work, hard to talk, focus on breathing.   | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=MDUzNjZiNWNkMmJhNmFkOTI2MDk2Y2FkZDNlODIwMTdfWjFta051b0tHZXF4aWVBM3AwdVVOZXNGZnp1VUlNV05fVG9rZW46TFhNeWJBczVCb25NSWx4ZnlvRWN2OVNxbjRiXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **9**      | **极其艰苦** | 接近极限，呼吸急促，无法言语交流。   | **Very Hard**         | Pushing your limits, gasping, unable to speak.      | ![img](https://brjrn9letm.feishu.cn/space/api/box/stream/download/asynccode/?code=M2I0ODAxZmI5OTkyZWZkZjdiNzY1Zjc1MTdjMGQ5MWZfVHRHanJ2Y3dOSjRESzRaYWhsMjZ5N2hQajVvMUlSOGpfVG9rZW46SFdBSmJwYzhZb3hKTll4OWRleGNZWEpCbnliXzE3NzMzODYwNjM6MTc3MzM4OTY2M19WNA) |
| **10**     | **极限强度** | 筋疲力尽，完全透支，无法再坚持。     | **Extremely Hard**    | Maximum exertion, fully spent and maxed out.        | ![img](/Users/wangshuaibo/Documents/配图/已使用/(null)-20260313151430070.(null)) |