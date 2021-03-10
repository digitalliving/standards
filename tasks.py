from pathlib import Path

from invoke import task
import jinja2

STANDARDS_DIR = [Path("draft") / "DataProducts"]


@task()
def bootstrap_html(ctx):
    """
    Creates corresponding HTML file next to each data product standard
    """
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("utils"))
    for standards_root in STANDARDS_DIR:
        for p in standards_root.glob("**/*.json"):
            template = env.get_template("standard.html.jinja2")
            html_content = template.render(name=p.with_suffix("").name)
            html_file = p.with_suffix(".html")
            html_file.write_text(html_content)
            print(f"{html_file} written")
