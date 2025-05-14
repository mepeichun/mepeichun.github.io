# Extremely Simple HomePage


This project generates an HTML webpage showcasing a person's publications and personal information, by converting a Markdown file and a YAML file into HTML. It uses a Jinja2 template to structure the final page, which is saved as `index.html`.

See the page [here](https://mepeichun.github.io/) 

## Prerequisites

Before running the script, ensure that you have the following Python libraries installed:

```bash
pip install pyyaml jinja2 markdown
```

## Project Structure

The following files and directories are required for this script to work:

- `data/about.md`: Markdown file containing the "about" information to be converted into HTML.
- `data/publication.yaml`: YAML file containing a list of publications.
- `data/template.html`: Jinja2 HTML template used to render the final page.
- `images/`: Directory containing images for the publications.

The script expects the following format for the YAML and Markdown files:

### Sample `publication.yaml`:

```yaml
publications:
  - title: "Sample Paper"
    authors: ["Author Two", "Author Two"]
    venue: "Some Conference"
    image: "sample_image.jpg"
    links:
      - label: "Code"
        url: "https://link1.com"
      - label: "Paper"
        url: "https://link2.com"
```