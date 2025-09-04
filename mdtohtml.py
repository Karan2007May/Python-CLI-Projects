import markdown

def convert_md_to_html():
    md_text = """# Hello World
This is a markdown file!"""
    html = markdown.markdown(md_text)
    print(html)

convert_md_to_html()
