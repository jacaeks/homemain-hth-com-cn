import json


SITE_DATA = {
    "site_name": "华体会体育平台",
    "domain": "https://homemain-hth.com.cn",
    "tags": ["体育", "电竞", "真人娱乐", "彩票"],
    "description": "华体会（HTH）是一家综合性的在线娱乐平台，提供体育赛事投注、电子竞技、真人视讯及彩票游戏等服务。",
    "keywords": ["华体会", "HTH", "体育投注", "电竞竞猜", "真人娱乐", "彩票"]
}


def build_summary(data: dict) -> dict:
    summary = {
        "title": data.get("site_name", "未知站点"),
        "url": data.get("domain", ""),
        "tags": data.get("tags", []),
        "keywords": data.get("keywords", []),
        "description": data.get("description", ""),
    }
    return summary


def format_tags(tags: list) -> str:
    return " | ".join(tags)


def format_keywords(keywords: list) -> str:
    return ", ".join(keywords)


def render_text_summary(summary: dict) -> str:
    lines = []
    lines.append("=" * 48)
    lines.append(f"站点名称：{summary['title']}")
    lines.append(f"网    址：{summary['url']}")
    lines.append(f"标    签：{format_tags(summary['tags'])}")
    lines.append(f"关键词：{format_keywords(summary['keywords'])}")
    lines.append(f"简    介：{summary['description']}")
    lines.append("=" * 48)
    return "\n".join(lines)


def render_html_summary(summary: dict) -> str:
    safe_title = summary["title"]
    safe_url = summary["url"]
    safe_desc = summary["description"]
    safe_tags = format_tags(summary["tags"])
    safe_keywords = format_keywords(summary["keywords"])
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>{safe_title}</title>
<style>
  body {{ font-family: Arial, sans-serif; margin: 2rem; background: #f9f9f9; }}
  .card {{ background: white; border-radius: 12px; padding: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 720px; margin: auto; }}
  h1 {{ color: #333; }}
  .meta {{ color: #555; margin: 0.5rem 0; }}
  .tag {{ display: inline-block; background: #e0f0ff; color: #0055aa; padding: 4px 10px; border-radius: 20px; margin: 4px 6px 4px 0; font-size: 0.85rem; }}
  .kw {{ color: #b34d00; font-weight: 600; }}
  .desc {{ line-height: 1.6; color: #333; }}
</style>
</head>
<body>
<div class="card">
<h1>{safe_title}</h1>
<p class="meta"><strong>网址：</strong><a href="{safe_url}" target="_blank">{safe_url}</a></p>
<p class="meta"><strong>标签：</strong><span class="tag">{safe_tags.replace(" | ", "</span><span class='tag'>")}</span></p>
<p class="meta"><strong>关键词：</strong><span class="kw">{safe_keywords}</span></p>
<p class="desc"><strong>简介：</strong>{safe_desc}</p>
</div>
</body>
</html>"""
    return html


def render_json_summary(summary: dict) -> str:
    return json.dumps(summary, ensure_ascii=False, indent=2)


def main():
    summary = build_summary(SITE_DATA)

    print(">>> 文本摘要")
    print(render_text_summary(summary))
    print()

    print(">>> JSON 摘要")
    print(render_json_summary(summary))
    print()

    html_output = render_html_summary(summary)
    with open("site_summary.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print(">>> HTML 摘要已写入 site_summary.html")


if __name__ == "__main__":
    main()