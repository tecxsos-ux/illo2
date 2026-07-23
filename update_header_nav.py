import glob, os

html_files = glob.glob('**/*.html', recursive=True)

old_nav_1 = '<li><a class="rounded-full px-4 py-2 text-sm font-medium transition-colors hover:bg-sand text-body" href="/shop/">Shop</a></li>'
old_nav_2 = '<li><a class="rounded-full px-4 py-2 text-sm font-medium transition-colors hover:bg-sand text-ink underline decoration-coral decoration-2 underline-offset-4" href="/shop/">Shop</a></li>'

industry_link = '<li><a class="rounded-full px-4 py-2 text-sm font-medium transition-colors hover:bg-sand text-body" href="/industry/">Swiss Industry</a></li>'
industry_link_active = '<li><a class="rounded-full px-4 py-2 text-sm font-medium transition-colors hover:bg-sand text-ink underline decoration-coral decoration-2 underline-offset-4" href="/industry/">Swiss Industry</a></li>'

count = 0
for filepath in html_files:
    if 'node_modules' in filepath:
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '/industry/' not in content:
        if 'href="/industry/"' not in content:
            if old_nav_1 in content:
                content = content.replace(old_nav_1, old_nav_1 + industry_link)
            elif old_nav_2 in content:
                content = content.replace(old_nav_2, old_nav_2 + industry_link)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1

print(f"Updated header navigation in {count} HTML files!")
