#!/usr/bin/env python3
"""Generate HTML files for JD screenshots."""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

COMMON_STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #f5f5f5;
    padding: 40px;
    color: #1a1a1a;
    line-height: 1.7;
  }
  .card {
    background: #fff;
    border-radius: 16px;
    padding: 48px;
    max-width: 680px;
    margin: 0 auto;
    box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  }
  .badge {
    display: inline-block;
    font-size: 12px;
    font-weight: 500;
    padding: 4px 12px;
    border-radius: 20px;
    margin-bottom: 16px;
  }
  .badge-a { background: #e8f4fd; color: #1976d2; }
  .badge-b { background: #fce4ec; color: #c62828; }
  .badge-c { background: #e8f5e9; color: #2e7d32; }
  .title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 6px;
  }
  .meta {
    font-size: 14px;
    color: #888;
    margin-bottom: 28px;
  }
  .meta .salary {
    color: #e65100;
    font-weight: 700;
    font-size: 16px;
  }
  .intro {
    font-size: 15px;
    color: #555;
    margin-bottom: 24px;
    padding: 16px 20px;
    background: #fafafa;
    border-radius: 10px;
    border-left: 3px solid #e65100;
  }
  h3 {
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 12px;
    margin-top: 24px;
    color: #333;
  }
  h3::before {
    content: '';
    display: inline-block;
    width: 4px;
    height: 16px;
    background: #e65100;
    border-radius: 2px;
    margin-right: 8px;
    vertical-align: middle;
  }
  ol, ul {
    padding-left: 20px;
    margin-bottom: 16px;
  }
  li {
    font-size: 14px;
    color: #444;
    margin-bottom: 8px;
    line-height: 1.7;
  }
  .bonus {
    background: #f9f9f9;
    border-radius: 10px;
    padding: 16px 20px;
    margin-top: 20px;
  }
  .bonus h3 { margin-top: 0; }
  .bonus li { color: #666; }
  .footer {
    margin-top: 32px;
    padding-top: 20px;
    border-top: 1px solid #eee;
    font-size: 12px;
    color: #bbb;
    text-align: center;
  }
</style>
"""

# --- Style A: Traditional ---
def style_a_uiux():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-a">风格 A · 传统风格</span>
<div class="title">UI/UX 设计师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">25-40K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<h3>工作职责</h3>
<ol>
<li>负责公司智能健身产品的用户体验设计与 UI 视觉设计，覆盖移动端 APP 及配套界面</li>
<li>深入研究目标用户（以海外健身用户为主），输出用户画像、使用场景分析和交互方案</li>
<li>主导产品从概念到上线的设计全流程，与产品经理、开发工程师紧密协作，确保设计高质量落地</li>
<li>建立和维护产品设计规范与组件库，保证视觉一致性和设计效率</li>
<li>关注海外主流健身 APP 设计趋势，持续优化产品体验</li>
</ol>

<h3>任职要求</h3>
<ol>
<li>本科及以上学历，设计、人机交互、计算机等相关专业</li>
<li>3-5 年用户体验设计经验，主导过至少 1 款上线产品的完整设计</li>
<li>精通 Figma，熟练使用 Sketch、Principle 等设计与原型工具</li>
<li>扎实的 UI 设计功底（排版、色彩、图形设计），理解用户体验设计原则</li>
<li>了解基本的前端开发逻辑，能与开发团队高效沟通</li>
<li>有运动健康类或硬件配套 APP 设计经验者优先</li>
<li>能清晰阐述海外产品和国内产品在设计语言、信息架构、用户习惯上的差异</li>
</ol>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有海外产品设计经验或长期使用海外健身 APP</li>
<li>有带人经验，具备设计团队管理意识</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_a_flutter():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-a">风格 A · 传统风格</span>
<div class="title">Flutter 前端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<h3>工作职责</h3>
<ol>
<li>使用 Flutter 开发公司智能健身设备配套 APP，覆盖 iOS 和 Android 双平台</li>
<li>负责 APP 核心功能的开发、性能优化和迭代维护</li>
<li>与产品经理、UI 设计师、后端工程师协作，保证功能按时高质量交付</li>
<li>参与技术方案评审和代码 Review，维护良好的代码质量和工程规范</li>
<li>参与 APP 与智能硬件设备的数据通信联调</li>
</ol>

<h3>任职要求</h3>
<ol>
<li>本科及以上学历，计算机相关专业</li>
<li>3-5 年移动端开发经验，其中至少 2 年 Flutter 开发经验</li>
<li>熟悉 Dart 语言，熟悉 Flutter 框架及常见状态管理方案（如 Riverpod、Bloc 等）</li>
<li>有 iOS 或 Android 原生开发经验，了解平台特性和上架流程</li>
<li>有良好的代码习惯，注重可读性、可维护性和测试</li>
<li>有较强的学习能力和技术热情</li>
</ol>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有蓝牙（BLE）通信开发经验，熟悉硬件设备连接与数据交互</li>
<li>有运动健康类 APP 开发经验</li>
<li>对健身或运动有真实兴趣</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_a_java():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-a">风格 A · 传统风格</span>
<div class="title">Java 后端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<h3>工作职责</h3>
<ol>
<li>负责公司智能健身设备后端服务的设计与开发，支撑移动端 APP 和设备数据处理</li>
<li>设计合理的系统架构，确保服务的稳定性、可扩展性和高可用性</li>
<li>负责数据模型设计，支持多种运动数据格式的接入和扩展</li>
<li>与前端工程师、产品经理协作，制定接口规范，保证前后端高效联调</li>
<li>编写技术文档，参与 Code Review，维护代码质量</li>
</ol>

<h3>任职要求</h3>
<ol>
<li>本科及以上学历，计算机相关专业</li>
<li>3-5 年 Java 后端开发经验</li>
<li>熟悉 Spring Boot / Spring Cloud 等主流框架</li>
<li>熟悉 MySQL 等关系型数据库的设计与优化，了解 Redis、消息队列等常用中间件</li>
<li>有良好的系统设计和架构思维，能设计出可扩展的数据结构和服务架构</li>
<li>熟悉 RESTful API 设计，有接口规范意识</li>
<li>有良好的代码习惯和文档意识</li>
</ol>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有运动健康类或 IoT 相关后端开发经验</li>
<li>有海外产品后端开发经验（了解 GDPR 等合规要求）</li>
<li>熟悉云服务部署（AWS / GCP 等）</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

# --- Style B: Mission-driven ---
def style_b_uiux():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-b">风格 B · 使命驱动风格</span>
<div class="title">UI/UX 设计师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">25-40K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们正在打造一款面向全球用户的数字训练设备，目标是让力量训练、划船、滑雪等运动体验变得更智能、更有趣。<br><br>
现在，我们需要<strong>第一位设计师</strong>。<br><br>
你不是来"接需求出图"的。你会从零定义这款产品的视觉语言和交互体验，直接影响全球用户打开 APP 的第一感受。随着团队成长，你将有机会组建自己的设计团队。
</div>

<h3>我们希望你是这样的人</h3>
<ul>
<li>你健身、跑步、或者玩任何一种运动——你理解"训练"这件事本身</li>
<li>你日常使用 Strava、Peloton、Apple Fitness+ 或类似产品，对它们的设计有自己的判断</li>
<li>你能说清楚一个面向欧美用户的 APP 和一个面向国内用户的 APP，在设计上到底有什么不同，以及为什么</li>
<li>你想做一款拿得出手的海外产品，而不只是完成一个任务</li>
</ul>

<h3>基本门槛</h3>
<ul>
<li>3-5 年 UI/UX 设计经验，主导过至少 1 款完整产品</li>
<li>精通 Figma</li>
<li>能独立完成从用户研究 → 交互方案 → 视觉设计 → 设计规范的全流程</li>
<li>了解前端开发的基本逻辑，方便和开发高效沟通</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有运动健康类产品设计经验</li>
<li>有海外产品设计经验</li>
<li>有带人经验</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_b_flutter():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-b">风格 B · 使命驱动风格</span>
<div class="title">Flutter 前端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们在做一款面向全球市场的智能训练设备——力量训练、划船、滑雪，一台设备搞定。现在需要<strong>第一位前端工程师</strong>，用 Flutter 从零搭建配套 APP。<br><br>
这不是一个"按 PRD 写页面"的岗位。你将是移动端唯一的工程师，你的技术决策直接决定这款 APP 的架构和体验。
</div>

<h3>我们希望你是这样的人</h3>
<ul>
<li>你自己有健身或运动的习惯，知道一个好的训练 APP 应该是什么样的</li>
<li>你用过 Tempo、Tonal、Peloton 或类似产品的 APP，并且对它们有自己的看法</li>
<li>你想从头搭一个项目，而不是在一个庞大的代码库里修修补补</li>
<li>你在意代码质量，但更在意用户拿到手的体验</li>
</ul>

<h3>基本门槛</h3>
<ul>
<li>3-5 年移动端开发经验，至少 2 年 Flutter</li>
<li>熟悉 Dart，熟悉至少一种状态管理方案</li>
<li>有 iOS 或 Android 原生开发背景，了解平台特性</li>
<li>能独立完成从技术方案设计到开发上线的全流程</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有蓝牙（BLE）设备通信开发经验</li>
<li>有运动健康类产品开发经验</li>
<li>有过从 0 到 1 搭建项目的经历</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_b_java():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-b">风格 B · 使命驱动风格</span>
<div class="title">Java 后端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们在做一款全球化的智能训练设备。力量训练只是起点，划船、滑雪等模式正在路上——设备会产生越来越多种类的运动数据。<br><br>
我们需要一位后端工程师，来设计一个能<strong>"长出来"</strong>的后端架构。不是堆功能，而是搭一套能轻松适配新数据格式、新运动模式的系统。
</div>

<h3>我们希望你是这样的人</h3>
<ul>
<li>比起"写代码快"，你更在意"架构是否合理"</li>
<li>你设计一个数据表或一个接口时，会想"半年后加新功能时，这里会不会成为瓶颈"</li>
<li>你有运动习惯，或者至少对运动数据（心率、力量曲线、训练量）有好奇心</li>
<li>你想参与一款海外产品的后端架构搭建，而不是维护一个已有系统</li>
</ul>

<h3>基本门槛</h3>
<ul>
<li>3-5 年 Java 后端开发经验</li>
<li>熟悉 Spring Boot，有独立设计和开发后端服务的能力</li>
<li>有扎实的数据库设计功底，能设计出可扩展的数据模型</li>
<li>能清晰表达自己的架构思路和技术方案</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有运动健康类或 IoT 数据处理经验</li>
<li>有海外产品经验，了解 GDPR 等数据合规要求</li>
<li>熟悉 AWS / GCP 等云服务</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

# --- Style C: Hybrid ---
def style_c_uiux():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-c">风格 C · 混合风格（推荐）</span>
<div class="title">UI/UX 设计师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">25-40K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们是一家做智能训练设备的公司，产品面向全球市场。你将作为团队第一位设计师，从零搭建产品的用户体验。
</div>

<h3>工作职责</h3>
<ol>
<li>主导产品移动端 APP 的用户体验与视觉设计，服务全球健身用户</li>
<li>深入理解海外用户的训练场景和使用习惯，将洞察转化为设计方案</li>
<li>与产品经理和开发工程师紧密配合，确保设计高质量落地</li>
<li>建立产品设计规范和组件库，为后续团队扩展打好基础</li>
</ol>

<h3>我们看重的</h3>
<ol>
<li>3-5 年 UI/UX 设计经验，主导过至少 1 款完整产品的设计</li>
<li>精通 Figma，有扎实的视觉设计功底</li>
<li>能说清楚海外产品与国内产品在设计上的核心差异——不是背书，而是有自己的思考</li>
<li>对运动和健身有真实的兴趣，是用户、不只是设计师</li>
<li>想参与一款海外产品从 0 到 1 的过程，有主人翁心态</li>
</ol>

<h3>技术要求</h3>
<ul>
<li>精通 Figma，熟练使用常见设计与原型工具</li>
<li>了解前端开发的基本逻辑，能与开发团队高效协作</li>
<li>有运动健康类或硬件配套 APP 设计经验者优先</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有海外产品设计经验</li>
<li>有带人经验，具备设计团队管理意识</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_c_flutter():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-c">风格 C · 混合风格（推荐）</span>
<div class="title">Flutter 前端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们正在打造一款面向全球用户的智能训练设备和配套 APP。你将是团队第一位前端工程师，用 Flutter 构建 iOS 和 Android 双端应用。
</div>

<h3>工作职责</h3>
<ol>
<li>使用 Flutter 开发配套移动端 APP，负责核心功能开发与性能优化</li>
<li>参与 APP 与智能硬件设备的通信联调</li>
<li>与产品、设计、后端紧密协作，快速迭代交付</li>
<li>主导前端技术选型和架构设计，为后续团队扩展奠定基础</li>
</ol>

<h3>我们看重的</h3>
<ol>
<li>3-5 年移动端开发经验，至少 2 年 Flutter 实战</li>
<li>有 iOS 或 Android 原生开发经验，理解双平台差异</li>
<li>对运动或健身有真实兴趣——你是用户，不只是开发者</li>
<li>想做一款面向海外市场的高质量产品，有追求</li>
<li>注重代码质量，能独立做技术决策</li>
</ol>

<h3>技术要求</h3>
<ul>
<li>熟悉 Dart 语言和 Flutter 框架</li>
<li>了解常见状态管理方案（Riverpod、Bloc 等）</li>
<li>了解平台特性和 App Store / Google Play 上架流程</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有蓝牙（BLE）硬件通信开发经验</li>
<li>有运动健康类 APP 开发经验</li>
<li>有从 0 到 1 搭建项目的经历</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

def style_c_java():
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">{COMMON_STYLE}</head><body><div class="card">
<span class="badge badge-c">风格 C · 混合风格（推荐）</span>
<div class="title">Java 后端工程师</div>
<div class="meta">深圳 &nbsp;|&nbsp; <span class="salary">20-35K · 13薪</span> &nbsp;|&nbsp; 3-5年 &nbsp;|&nbsp; 本科及以上</div>

<div class="intro">
我们正在打造一款面向全球的智能训练设备，产品将支持力量训练、划船、滑雪等多种运动模式。你将是团队第一位后端工程师，从零搭建后端服务架构。
</div>

<h3>工作职责</h3>
<ol>
<li>设计和开发后端服务，支撑移动端 APP 与设备数据处理</li>
<li>设计可扩展的数据模型和接口，适配多种运动模式和数据格式</li>
<li>与前端工程师、产品经理协作，保证前后端高效联调</li>
<li>确保系统稳定性和数据安全性，尤其关注海外用户的数据合规</li>
</ol>

<h3>我们看重的</h3>
<ol>
<li>3-5 年 Java 后端开发经验，有独立搭建服务的能力</li>
<li>有良好的架构思维——比起"能跑就行"，你更在意"好不好扩展"</li>
<li>对运动或健身有兴趣，愿意理解业务场景</li>
<li>想从零搭建一个面向海外市场的后端系统，有技术追求</li>
<li>能清晰表达技术方案，乐于协作</li>
</ol>

<h3>技术要求</h3>
<ul>
<li>熟悉 Java、Spring Boot / Spring Cloud</li>
<li>有扎实的数据库设计能力（MySQL 为主），了解 Redis 等常用中间件</li>
<li>熟悉 RESTful API 设计</li>
<li>有良好的代码规范和文档习惯</li>
</ul>

<div class="bonus">
<h3>加分项</h3>
<ul>
<li>有运动健康类或 IoT 后端开发经验</li>
<li>有海外产品经验，了解 GDPR 等数据合规</li>
<li>熟悉 AWS / GCP 等云服务部署</li>
</ul>
</div>
<div class="footer">JD 草稿 · 仅供内部讨论</div>
</div></body></html>"""

# Generate all files
files = {
    "A_UIUX_传统风格.html": style_a_uiux(),
    "A_Flutter_传统风格.html": style_a_flutter(),
    "A_Java_传统风格.html": style_a_java(),
    "B_UIUX_使命驱动.html": style_b_uiux(),
    "B_Flutter_使命驱动.html": style_b_flutter(),
    "B_Java_使命驱动.html": style_b_java(),
    "C_UIUX_混合风格.html": style_c_uiux(),
    "C_Flutter_混合风格.html": style_c_flutter(),
    "C_Java_混合风格.html": style_c_java(),
}

for name, content in files.items():
    path = os.path.join(OUTPUT_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {name}")

print(f"\nTotal: {len(files)} HTML files generated.")
