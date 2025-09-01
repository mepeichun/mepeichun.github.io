import yaml
from jinja2 import Template
import markdown
import datetime

def generate_publication_html(yaml_data, your_name):
    publications = yaml.safe_load(yaml_data)['publications']
    
    html_blocks = []
    for pub in publications:
        title_html = f"<div class='title'>{pub['title']}</div>"
        
        # Process authors with special formatting for your name
        authors_html = "<div class='authors'>" + ', '.join(
            f"<span class='me'>{a.strip()}</span>" if your_name in a else f"<span class='author'>{a.strip()}</span>"
            for a in pub['authors']
        ) + "</div>"
        
        venue_html = f"<span class='tag'><b>{pub['venue']}</b></span>" if 'venue' in pub else ''
        
        links_html = " / ".join(
            f"<span class='tag'><a href='{link['url']}'>{link['label']}</a></span>" 
            for link in pub.get('links', [])
        )

        block = f"""
        <section class="pub">
            <table width="100%" align="center" border="0">
                <tr>
                    <td width="25%" valign="top">
                        <a class="image"><img src="images/{pub['image']}" width="90%" alt=""></a>
                    </td>
                    <td width="75%" align="center">
                        {title_html}
                        {authors_html}
                        <div>
                            {venue_html} {'/' if venue_html and links_html else ''} {links_html}
                        </div>
                    </td>
                </tr>
            </table>
        </section>
        """
        html_blocks.append(block.strip())
    
    return '\n'.join(html_blocks)

# Read about.md and convert
with open('./data/about.md', 'r', encoding='utf-8') as f:
    about_md = f.read()
about_html = markdown.markdown(about_md)

# Read publication.yaml and convert using function
with open('./data/publication.yaml', 'r', encoding='utf-8') as f:
    publication_yaml = f.read()
publication_html = generate_publication_html(publication_yaml, your_name='Peichun Li')

# Read the HTML template
with open('./data/template.html', 'r', encoding='utf-8') as f:
    template = Template(f.read())

# Define your personal information
context = {
    'name': 'Chengji Wang',
    'github': 'https://github.com/mepeichun',
    'scholar': 'https://scholar.google.com.hk/citations?user=hC0FPWkAAAAJ&hl=en',
    'about_content': about_html,
    'publication_content': publication_html,
    'year': datetime.date.today().year,
}

# Render the final HTML
output_html = template.render(**context)

# Save to output.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output_html)