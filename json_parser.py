import json as json_module

def json_to_html(json, depth=0):
    """
    convert json to html
    json is a list of dicts, each dict is a section
    json starts off with a page title and a subsections list
    {
        "title": "Section Title",
        "content": ["Section Content"],
        "subsections": [
            {
                "title": "Subsection Title",
                "content": ["Subsection Content"],
                "subsections": []
    }
    recursively convert each section to html
    use depth to determine the heading level
    """
    print(depth)
    if depth == 0:
        json = json_module.loads(json)
    if type(json) == dict:
        json = [json]
    html = ""
    for section in json:
        if "title" in section:
            html += f"<h{depth+1}>{section['title']}</h{depth+1}>"
        if "type" not in section or section['type'] == "text":
            for content in section['content']:
                html += f"<p>{content}</p>"
        elif section['type'] == "code":
            for content in section['content']:
                html += f"<pre><code>{content}</code></pre>"
        elif section['type'] == "table":
            # tables are in nested lists in json, assume the first row is the header
            html += "<table>"
            html += "<tr>"
            for cell in section['content'][0]:
                html += f"<th>{cell}</th>"
            html += "</tr>"
            for row in section['content'][1:]:
                html += "<tr>"
                for cell in row:
                    html += f"<td>{cell}</td>"
                html += "</tr>"
            html += "</table>"
        elif section['type'] == "headless-table":
            # tables are in nested lists in json, there is no header
            html += "<table>"
            for row in section['content']:
                html += "<tr>"
                for cell in row:
                    html += f"<td>{cell}</td>"
                html += "</tr>"
            html += "</table>"
        elif section['type'] == "ulist":
            # unordered list, add ul and li tags
            html += "<ul>"
            for item in section['content']:
                html += f"<li>{item}</li>"
            html += "</ul>"
        elif section['type'] == "olist":
            # ordered list, add ol and li tags
            html += "<ol>"
            for item in section['content']:
                html += f"<li>{item}</li>"
            html += "</ol>"
        elif section['type'] == "link":
            # link, add a tag
            html += f"<a href='{section['content'][0]}'>{section['content'][1]}</a>"
        elif section['type'] == "image":
            # content should be an image url in the first element and an alt text in the second
            html += f"<img src='{section['content'][0]}' alt='{section['content'][1]}' />"
        if "subsections" in section and section['subsections']:
            html += json_to_html(section['subsections'], depth=depth+1)
    return html