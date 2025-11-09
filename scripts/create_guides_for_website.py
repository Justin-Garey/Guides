import os
import re
import json

def find_markdown_files(root_dir):
    markdown_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_markdown_links(file_path):
    links = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Match markdown links [text](path.md)
        pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
        matches = re.findall(pattern, content)
        for _, link in matches:
            # Remove anchors
            link = link.split('#')[0]
            if link:
                links.add(link)
    return links

def resolve_link_path(source_file, link, repo_root):
    source_dir = os.path.dirname(source_file)
    if link.startswith('/'):
        # Absolute path from repo root
        return os.path.normpath(os.path.join(repo_root, link.lstrip('/')))
    else:
        # Relative path
        return os.path.normpath(os.path.join(source_dir, link))
    
def create_json_list_of_links(links, output_dir):
    output_file = os.path.join(output_dir, 'guides_links.json')
    with open(output_file, 'w') as f:
        json.dump(links, f)

def main():
    # Get repository root (parent of scripts directory)
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Find all markdown files
    all_markdown_files = find_markdown_files(repo_root)
    
    # Track files to copy
    files_to_copy = set()
    
    # Include README.md
    readme_path = os.path.join(repo_root, 'README.md')
    if os.path.exists(readme_path):
        files_to_copy.add(readme_path)
    
    # Extract links from all markdown files
    for md_file in all_markdown_files:
        links = extract_markdown_links(md_file)
        for link in links:
            resolved_path = resolve_link_path(md_file, link, repo_root)
            if os.path.exists(resolved_path):
                files_to_copy.add(resolved_path)
    
    # Create temp directory
    temp_dir = os.path.join(repo_root, 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    links_for_json = []
    
    # Copy files and update links
    for file_path in files_to_copy:
        # Get relative path from repo root
        rel_path = os.path.relpath(file_path, repo_root)
        dest_path = os.path.join(temp_dir, rel_path)
        
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Replace markdown links
        def replace_link(match):
            text = match.group(1)
            link = match.group(2)
            link_without_anchor = link.split('#')[0]
            anchor = '#' + link.split('#')[1] if '#' in link else ''
            
            if link_without_anchor:
                resolved = resolve_link_path(file_path, link_without_anchor, repo_root)
                if os.path.exists(resolved):
                    rel_from_root = os.path.relpath(resolved, repo_root)
                    new_link = f"/{rel_from_root.replace(os.sep, '/')}".split('.md')[0]
                    links_for_json.append("guides" + new_link)
                    return f"[{text}]({new_link}{anchor})"
            return match.group(0)
        
        updated_content = re.sub(r'\[([^\]]+)\]\(([^)]+\.md)\)', replace_link, content)
        
        with open(dest_path, 'w') as f:
            f.write(updated_content)

    # Write JSON list of links
    create_json_list_of_links(links_for_json, temp_dir)
    
    print(f"Copied {len(files_to_copy)} files to {temp_dir}")
    print("Updated markdown links to use paths for website")

if __name__ == '__main__':
    main()