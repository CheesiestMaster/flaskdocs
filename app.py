from flask import Flask, templating
import docs.config as config
import markdown
import os
import json as json_module

app = Flask(__name__, static_folder='static', template_folder='templates')

def md_to_html(md):
    # convert markdown to html
    # preserve newlines
    md = md.replace('\n', '  \n')
    # convert to html preserving tables
    html = markdown.markdown(md, extensions=['tables', 'fenced_code'])
    return html

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
        html += f"<h{depth+1}>{section['title']}</h{depth+1}>"
        for content in section['content']:
            html += f"<p>{content}</p>"
        if "subsections" in section and section['subsections']:
            html += json_to_html(section['subsections'], depth=depth+1)
    return html
    

def get_docs(path):
    # find a docs file, if type is md, convert to html and return
    if path.endswith('.md'):
        print("md")
        with open(path, 'r') as f:
            return md_to_html(f.read())
    elif path.endswith('.html') or path.endswith('.txt'):
        print("html or txt")
        with open(path, 'r') as f:
            return f.read()
    elif path.endswith('.json'):
        print("json")
        with open(path, 'r') as f:
            return json_to_html(f.read())
    else:
        # check if a file exists with any of the extensions and recurse
        print("recurse")
        for ext in ['.md', '.html', ".txt", ".json"]:
            if os.path.exists(path + ext) and get_docs(path + ext):
                return get_docs(path + ext)


@app.route('/')
def index():
    # feed return through template to add header and footer, title is DOCS
    # template file is templates/template.html
    return templating.render_template('template.html', title='DOCS', body=get_docs("docs/index"))
    

@app.route('/<path:path>')
def docs(path):
    # title for page is the last part of the path, case converted to title case
    return templating.render_template('template.html', title=path.split('/')[-1].replace('-', ' ').title(), body=get_docs("docs/" + path))

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    # if the app is run directly, run it in debug mode
    app.run(debug=True, port=config.PORT, host=config.HOST)
else:
    # if the app is run indirectly, run it in production mode in a thread
    import threading
    threading.Thread(target=app.run, kwargs={'port': config.PORT, 'host': config.HOST}).start()