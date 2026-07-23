import glob, os

html_files = glob.glob('**/*.html', recursive=True)

script_tag = '<script src="/store-switcher.js" defer></script>\n'

count = 0
for filepath in html_files:
    if 'node_modules' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '/store-switcher.js' not in content:
        if '</body>' in content:
            new_content = content.replace('</body>', script_tag + '</body>')
        else:
            new_content = content + script_tag
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Injected store-switcher.js into {count} HTML files!")
