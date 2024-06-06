import os
from markdown_utils import extract_title
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as md_file:
        markdown_content = md_file.read()

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()


    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_content = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as dest_file:
        dest_file.write(final_content)
