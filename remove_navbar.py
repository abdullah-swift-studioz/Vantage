import os
import re

def remove_navbar():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Extensions to look for
    extensions = ['.html']
    
    files_processed = 0
    errors = 0

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if not any(file.endswith(ext) for ext in extensions):
                continue
                
            file_path = os.path.join(subdir, file)
            print(f"Processing: {file_path}")
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # backup content
                original_content = content
                
                # Strategy:
                # Find the start of the navbar.
                # Common start patterns:
                # 1. <!-- NEW NAVIGATION SYSTEM ... -->
                # 2. <nav class="navbar">
                
                # We want to find the EARLIEST occurrence of these.
                nav_starts = [
                    m.start() for m in re.finditer(r'<!--\s*NEW NAVIGATION SYSTEM', content, re.IGNORECASE)
                ]
                nav_tag_starts = [
                    m.start() for m in re.finditer(r'<nav\s+class="navbar"', content, re.IGNORECASE)
                ]
                
                all_starts = sorted(nav_starts + nav_tag_starts)
                
                if not all_starts:
                    print(f"  [SKIP] No navbar found in {file}")
                    continue
                
                start_index = all_starts[0]
                
                # Find the end of the area to delete.
                # We assume the content starts with <section, <main, <header, or <div class="container" (if not in nav)
                # We search starting from start_index
                
                # We want to stop at the content. 
                # Common content markers:
                # <section
                # <main
                # <div class="container" (but check if it's not inside nav - actually nav has container too)
                # The hero section usually has class="hero" or is just <section>
                
                # Let's search for <section or <main first.
                content_markers = [
                    m.start() for m in re.finditer(r'<(section|main)', content[start_index:], re.IGNORECASE)
                ]
                
                # Also look for <div class="container" if section/main not found? 
                # Use caution. 'index.html' uses <section class="hero">.
                
                if content_markers:
                    # The marker found is relative to start_index
                    end_offset = content_markers[0]
                    end_index = start_index + end_offset
                    
                    # Check if we are deleting too much?
                    # The removed chunk should contain </nav>
                    deleted_chunk = content[start_index:end_index]
                    
                    if '</nav>' not in deleted_chunk:
                         print(f"  [WARNING] potential mis-indentification. </nav> not found in deletion range for {file}. Aborting change.")
                         continue
                         
                    # Perform deletion
                    new_content = content[:start_index] + content[end_index:]
                    
                    # Cleanup empty lines around the join
                    # This is optional but nice.
                    
                    if new_content != original_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"  [SUCCESS] Removed navbar from {file}")
                        files_processed += 1
                    else:
                        print(f"  [SKIP] Content unchanged for {file}")
                
                else:
                    print(f"  [SKIP] Could not find content start (section/main) in {file}")
                    
            except Exception as e:
                print(f"  [ERROR] Failed to process {file}: {e}")
                errors += 1

    print(f"\nSummary: Processed {files_processed} files with {errors} errors.")

if __name__ == "__main__":
    remove_navbar()
